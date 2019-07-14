import os_tools.XmlFileHandler as xh
import os_tools.FileHandler as fh
import os_tools.Tools as tools
import os_tools.StringUtils as su


##################################################################################
#
# just the StringsImporter boiler plate script
#
##################################################################################


def build_strings_dict(xlsx_path, logger):
    """
    Will return a dictionary containing all of the strings in the xlsx file.
    The dictionary will look like so:
    {
        "French": {"app_name': "C'est ma vie", "capital": "C"est ma vie", "add_tab": "Jours de la semaine"},
        "German": {"app_name": "Berufe\n", "capital": "Der Weg zur Post", "add_tab":},
        "Hindi": {"app_name": "शब्दावली", "capital": "देशों", "add_tab": "कंबोडिया"}
    }
    """
    from pyexcel_xlsx import get_data
    import json
    raw_workbook_data = get_data(xlsx_path, start_row=3, start_column=5, column_limit=1)
    # data_values = get_data(xlsx_path, start_row=3, end_row=len(output_dict),start_column=1, column_limit=1)

    raw_workbook_dict = json.loads(str(json.dumps(raw_workbook_data)))
    # dict_values = json.loads(str(json.dumps(data_values)))
    xlsx_dict = {}

    # start the workbooks loop
    for language in raw_workbook_dict.keys():
        language_dict = {}

        # scrape the codes list
        codes_list = list(filter(None, raw_workbook_dict[language]))

        # scrape the translated words list
        translated_words_data = get_data(xlsx_path, start_row=3, start_column=1, column_limit=1)[language]
        translated_words_list = translated_words_data[0:len(codes_list)]
        logger.info('Parsing ' + language)
        # loop on all of the codes list (the rightest column)
        for i in range(len(codes_list)):
            if translated_words_list[i] is None or not translated_words_list[i]:
                logger.warning('Seems like the string name \'' + codes_list[i][0] + '\' didn\'t got translated to ' + language + '. Would you like to continue? [yes]')
                to_continue = tools.ask_for_input('')
                if not su.str2bool(to_continue):
                    logger.info('Exiting')
                    return

            else:
                language_dict[codes_list[i][0]] = translated_words_list[i][0]

        xlsx_dict[language] = language_dict
    return xlsx_dict


# will turn the xlsx dictionary to strings.xml files
def xlsx_dict_to_strings_file(xlsx_dict, output_dir, logger):
    logger.info('All of the languages parsed successfully. Creating the strings.xml files')
    for language in xlsx_dict.keys():
        language_output_dir = output_dir + '/' + language
        fh.create_dir(language_output_dir)
        output_file = language_output_dir + '/' + 'strings.xml'
        xml = xh.create_xml_file('resources', output_file)
        language_dict = xlsx_dict[language]
        for key, val in language_dict.items():
            xh.add_node(xml, 'string', {'name': key}, val)
        xh.save_xml_file(xml, output_file, True)
        logger.info('The ' + language + ' language file created successfully in:\n ' + output_file)
