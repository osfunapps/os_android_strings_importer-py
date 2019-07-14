Introduction
------------
This project's aim is to translate back the xlsx file made in  
[os_android_strings_extractor-py](https://github.com/osfunapps/os_android_strings_extractor-py) to a strings.xml file you can use on your Android project.    


## Installation
Install via pip:

    pip install os_android_strings_importer

## Usage       
    
Just point to the .xlsx file and add the output directory:

    import os_android_strings_importer.StringsImporter as si
    
    si.run('/path/to/xlsx/file.xlsx', '/path/to/output/dir')

## Links
[os_android_strings_extractor-py](https://github.com/osfunapps/os_android_strings_extractor-py) -> turn the strings.xml file to a helpful xlsx file and send it to translators.    


## Licence
MIT