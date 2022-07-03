import enum_g_data

def init():
    global list_log_data_type
    global df_dict_log_data
    global is_log_loaded
    global frm_len
    global cur_frm

    list_log_data_type = [enum_g_data.ListLogDataType.EGO, \
                          enum_g_data.ListLogDataType.DTCT, \
                          enum_g_data.ListLogDataType.TRK]
    df_dict_log_data = dict()
    is_log_loaded = False
    frm_len = int(0)
    cur_frm = int(0)