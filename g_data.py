
def init():
    global list_log_data_type
    global df_dict_log_data
    global is_log_loaded
    global frm_len

    list_log_data_type = ["trk", "ego", "dtct"]
    df_dict_log_data = dict()
    is_log_loaded = False
    frm_len = int(0)