import os_android_strings_importer.StringsImporterBp as bp
import os_tools.LoggerHandler as loggerHandler


##################################################################################
#
# this module meant to turn a formatted xlsx file, back to strings.xml file with
# the translated text as xml values
#
##################################################################################

def run(xlsx_path, output_dir):
    """
    Will turn a .xlsx file to a strings.xml file/s.
    Make sure your that all of your workbooks, inside of the xlsx file, have all of the code values (you don't have to translate all of words though).
    Args:
        param xlsx_path: your xlsx file
        param output_dir:  the directory in which the output will be made
    """
    logger = loggerHandler.Logger(__file__)
    xlsx_dict = bp.build_strings_dict(xlsx_path, logger)
    bp.xlsx_dict_to_strings_file(xlsx_dict, output_dir, logger)


