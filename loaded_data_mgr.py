import pandas as pd
import loaded_data
import os

def setFilePnt(file_paths):
    file_names = []
    for idx, file_path in enumerate(file_paths[0]):
        file_names.append(os.path.basename(file_path))

    print(file_names)