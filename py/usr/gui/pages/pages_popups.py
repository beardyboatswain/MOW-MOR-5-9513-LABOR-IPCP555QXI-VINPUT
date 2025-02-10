#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.utils.system_init import InitModule

from usr.dev.dev import ipad_adm, ipad_usr

# --- page defenitions --------------------------------------------------------
adm_top_menu_pp_name = "001_TopMenu_PP"

usr_main_screen_control_pp_name = "103_MainScreen_Control_PP"
usr_additional_screen_control_pp_name = "104_AdditionalScreen_Control_PP"
usr_chat_screen_control_pp_name = "105_ChatScreen_Control_PP"
usr_main_screen_control_cinema_pp_name = "106_MainScreen_Cinema_Control_PP"

usr_room_mode_vcs_pp_name = "111_RoomMode_VCS_PP"
usr_room_mode_cinema_pp_name = "112_RoomMode_Cinema_PP"

usr_audio_control_vcs_pp_name = "101_AudioControl_VCS_PP"
usr_audio_control_cinema_pp_name = "102_AudioControl_Cinema_PP"

usr_av_defaults_pp_name = "113_AV_Defaults_PP"
usr_cam_control_show_pp_name = "114_CamControl_Show_PP"

usr_locker_mp_name = "997_Locker_MP"

# --- room mode widgets -------------------------------------------------------
ipad_usr.ShowPopup(usr_room_mode_vcs_pp_name)
ipad_usr.ShowPopup(usr_room_mode_cinema_pp_name)
ipad_adm.ShowPopup(usr_room_mode_vcs_pp_name)
ipad_adm.ShowPopup(usr_room_mode_cinema_pp_name)

# --- ADM spcific -------------------------------------------------------------
ipad_adm.ShowPopup(adm_top_menu_pp_name)

# --- USR spcific -------------------------------------------------------------


InitModule(__name__)
