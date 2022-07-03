import enum_g_config


def init():
    global cartesian_coord_unit_dist
    global disp_opt_ground
    global disp_opt_path
    global disp_opt_dtct
    global disp_opt_obj
    global disp_opt_fov
    global disp_opt_vector

    cartesian_coord_scale_factor = float(0.0)

    disp_opt_ground = enum_g_config.EnumDispOpt.DISPLAY
    disp_opt_path   = enum_g_config.EnumDispOpt.HIDE
    disp_opt_vector = enum_g_config.EnumDispOpt.DISPLAY

    disp_opt_dtct = [enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE   ]

    disp_opt_obj =  [enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE   ]

    disp_opt_fov = [enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE, \
                     enum_g_config.EnumDispOpt.HIDE   ]