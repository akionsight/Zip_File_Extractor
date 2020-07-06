from zipfile import ZipFile
import os
import pathlib

def extract_file(file_path, output_folder_path=None):
    with ZipFile(file_path, "r") as file:
        # file.printdir()
        if output_folder_path == None:
            fold = pathlib.Path(file_path).parent
            file.extractall(fold)
        else:
            file.extractall(output_folder_path)


