from glob import glob
import pandas as pd
import os

import g_data

def setLogDf(file_paths):
    for idx, file_path in enumerate(file_paths):

        is_log_data_type = False
        for data_type in g_data.list_log_data_type:
            if data_type in file_path:
                is_log_data_type = True
                break
        
        if True == is_log_data_type:
            g_data.df_dict_log_data[data_type] = pd.read_csv(file_path)

        if len(g_data.df_dict_log_data) == len(g_data.list_log_data_type):
            g_data.is_log_loaded = True

def initGlobalData():
    if True == g_data.is_log_loaded:
        is_all_data_has_same_frm_len = True
        len_first_data_frm_len = len(g_data.df_dict_log_data[g_data.list_log_data_type[0]])

        for idx in list(range(1, len(g_data.list_log_data_type))):
            if len(g_data.df_dict_log_data[g_data.list_log_data_type[idx]]) != len_first_data_frm_len:
                is_all_data_has_same_frm_len = False

        if True == is_all_data_has_same_frm_len:
            g_data.frm_len = len_first_data_frm_len