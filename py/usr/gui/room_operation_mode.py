#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.gui.RoomOperationMode import RoomOperationMode
from usr.dev.dev import ipad_adm, ipad_usr

from usr.gui.pages.pages_popups import (usr_main_screen_control_pp_name,
                                        usr_additional_screen_control_pp_name,
                                        usr_chat_screen_control_pp_name,
                                        usr_main_screen_control_cinema_pp_name,
                                        usr_audio_control_vcs_pp_name,
                                        usr_audio_control_cinema_pp_name,
                                        usr_cam_control_show_pp_name,
                                        usr_av_defaults_pp_name)
from usr.dev.dev import (tvone_left,
                         tvone_center,
                         tvone_right)
from usr.lcds.lcd_control import (bravia_chat_1,
                                  bravia_chat_2,
                                  bravia_chat_3,
                                  bravia_chat_4,
                                  bravia_clmn_l1,
                                  bravia_clmn_l2,
                                  bravia_clmn_l3,
                                  bravia_clmn_l4,
                                  bravia_clmn_r1,
                                  bravia_clmn_r2,
                                  bravia_clmn_r3,
                                  bravia_clmn_r4,
                                  bravia_cart_1,
                                  bravia_cart_2,
                                  bravia_clmn_r_all,
                                  bravia_clmn_l_all,
                                  bravia_chat_all,
                                  bravia_cart_all)

from usr.power.system_power import room_sys_power
from usr.video.video_control import xtp_ctrl_adm, videoControlImatrixAdm
from usr.audio.audio_control import audio_presets_control
from lib.gui.SplashScreen import SplashScreen
from usr.codec.codec_control import codec_main, codec_reserv

from lib.utils.system_init import InitModule


room_mode = RoomOperationMode()
room_mode.addMode(uiHost=ipad_usr,
                  oModeName=RoomOperationMode.omVCS,
                  oModeComment="Conference or presentation",
                  btnModeSetID=101,
                  btnModeNameID=102,
                  btnModeCommentID=103)
room_mode.addMode(uiHost=ipad_usr,
                  oModeName=RoomOperationMode.omCinema,
                  oModeComment="Relax after work",
                  btnModeSetID=104,
                  btnModeNameID=105,
                  btnModeCommentID=106)
room_mode.addMode(uiHost=ipad_adm,
                  oModeName=RoomOperationMode.omVCS,
                  oModeComment="Conference or presentation",
                  btnModeSetID=101,
                  btnModeNameID=102,
                  btnModeCommentID=103)
room_mode.addMode(uiHost=ipad_adm,
                  oModeName=RoomOperationMode.omCinema,
                  oModeComment="Relax after work",
                  btnModeSetID=104,
                  btnModeNameID=105,
                  btnModeCommentID=106)

room_mode.addPopups(oMode=RoomOperationMode.omVCS,
                    uiHost=ipad_usr,
                    popups=[usr_main_screen_control_pp_name,
                            usr_additional_screen_control_pp_name,
                            usr_chat_screen_control_pp_name,
                            usr_audio_control_vcs_pp_name,
                            usr_cam_control_show_pp_name,
                            usr_av_defaults_pp_name])

room_mode.addPopups(oMode=RoomOperationMode.omCinema,
                    uiHost=ipad_usr,
                    popups=[usr_main_screen_control_cinema_pp_name,
                            usr_audio_control_cinema_pp_name,
                            usr_av_defaults_pp_name])

room_mode.addPopups(oMode=RoomOperationMode.omVCS,
                    uiHost=ipad_adm,
                    popups=[usr_main_screen_control_pp_name,
                            usr_additional_screen_control_pp_name,
                            usr_chat_screen_control_pp_name,
                            usr_audio_control_vcs_pp_name,
                            usr_cam_control_show_pp_name,
                            usr_av_defaults_pp_name])

room_mode.addPopups(oMode=RoomOperationMode.omCinema,
                    uiHost=ipad_adm,
                    popups=[usr_main_screen_control_cinema_pp_name,
                            usr_audio_control_cinema_pp_name,
                            usr_av_defaults_pp_name])


# --- Show Slaplash on changing mode --------------------------------------------------------------
modeSplashScreen = SplashScreen(ipad_usr, "998_Splash_MP", 10004, 10005)
room_mode.addScript(RoomOperationMode.omVCS, modeSplashScreen.show, "Setting up room mode", 5)
room_mode.addScript(RoomOperationMode.omCinema, modeSplashScreen.show, "Setting up room mode", 5)

# --- POWER ON and OFF ----------------------------------------------------------------------------
room_sys_power.addPowerOnScript(room_mode.setMode, RoomOperationMode.omVCS)

room_sys_power.addPowerOffScript(tvone_left.Set, "PresetRecall", "1")
room_sys_power.addPowerOffScript(tvone_center.Set, "PresetRecall", "1")
room_sys_power.addPowerOffScript(tvone_right.Set, "PresetRecall", "1")
room_sys_power.addPowerOffScript(bravia_chat_all.set_power, "Off")
room_sys_power.addPowerOffScript(bravia_clmn_l_all.set_power, "Off")
room_sys_power.addPowerOffScript(bravia_clmn_r_all.set_power, "Off")
room_sys_power.addPowerOffScript(bravia_cart_all.set_power, "Off")

# --- Room Mode Scripts ---------------------------------------------------------------------------
room_mode.addScript(RoomOperationMode.omVCS, tvone_left.Set, 'PresetRecall', '2')
room_mode.addScript(RoomOperationMode.omVCS, tvone_center.Set, 'PresetRecall', '2')
room_mode.addScript(RoomOperationMode.omVCS, tvone_right.Set, 'PresetRecall', '2')
room_mode.addScript(RoomOperationMode.omVCS, bravia_chat_all.set_power, "On")
room_mode.addScript(RoomOperationMode.omVCS, bravia_clmn_l_all.set_power, "On")
room_mode.addScript(RoomOperationMode.omVCS, bravia_clmn_r_all.set_power, "On")
room_mode.addScript(RoomOperationMode.omVCS, bravia_cart_all.set_power, "On")

room_mode.addScript(RoomOperationMode.omVCS, tvone_left.Set, 'PresetRecall', '1')
room_mode.addScript(RoomOperationMode.omVCS, tvone_center.Set, 'PresetRecall', '3')
room_mode.addScript(RoomOperationMode.omVCS, tvone_right.Set, 'PresetRecall', '1')
room_mode.addScript(RoomOperationMode.omCinema, bravia_chat_all.set_power, "Off")
room_mode.addScript(RoomOperationMode.omCinema, bravia_clmn_l_all.set_power, "Off")
room_mode.addScript(RoomOperationMode.omCinema, bravia_clmn_r_all.set_power, "Off")
room_mode.addScript(RoomOperationMode.omCinema, bravia_cart_all.set_power, "Off")

# --- Switching video on changing mode ------------------------------------------------------------
# todo: проверить все входы и выходы, тут пока неправильная нумерация
room_mode.addScript(RoomOperationMode.omVCS, xtp_ctrl_adm.switch, 14, 6)          # Cisco Main People to Main Screen Left
room_mode.addScript(RoomOperationMode.omVCS, xtp_ctrl_adm.switch, 15, 7)          # Cisco Main Presentation to Main Screen Right
room_mode.addScript(RoomOperationMode.omVCS, xtp_ctrl_adm.switch, 6, 1)           # act cam to codec
room_mode.addScript(RoomOperationMode.omVCS, xtp_ctrl_adm.switch, 7, 17)          # Embedder to codec (Active Present)
room_mode.addScript(RoomOperationMode.omVCS, xtp_ctrl_adm.switch, 32, 16)          # Tribune to emd/de-ebd (to Active Present)
room_mode.addScript(RoomOperationMode.omVCS, xtp_ctrl_adm.switch, 45, 37)          # chat pc to bravias

room_mode.addScript(RoomOperationMode.omVCS, xtp_ctrl_adm.switch, 1, 29)          # Cam to seamless switcher
room_mode.addScript(RoomOperationMode.omVCS, xtp_ctrl_adm.switch, 2, 30)          # Cam to seamless switcher
room_mode.addScript(RoomOperationMode.omVCS, xtp_ctrl_adm.switch, 3, 31)          # Cam to seamless switcher
room_mode.addScript(RoomOperationMode.omVCS, xtp_ctrl_adm.switch, 4, 32)          # Cam to seamless switcher
room_mode.addScript(RoomOperationMode.omVCS, xtp_ctrl_adm.switch, 5, 33)          # Cam to seamless switcher
room_mode.addScript(RoomOperationMode.omVCS, xtp_ctrl_adm.switch, 5, 33)          # Cam to seamless switcher
room_mode.addScript(RoomOperationMode.omVCS, videoControlImatrixAdm.switch, 1, 5)       # Cam to seamless switcher

room_mode.addScript(RoomOperationMode.omCinema, xtp_ctrl_adm.switch, 14, 17)      # MAIN LED Screen To Active Presentstion
room_mode.addScript(RoomOperationMode.omCinema, xtp_ctrl_adm.switch, 32, 12)      # MAIN LED Screen To Apple TV

# --- Switching Symetrix preset on changing mode --------------------------------------------------
room_mode.addScript(RoomOperationMode.omVCS, audio_presets_control.call, 995)
room_mode.addScript(RoomOperationMode.omCinema, audio_presets_control.call, 996)

# --- Waking up cisco codec on changing mode ------------------------------------------------------
room_mode.addScript(RoomOperationMode.omVCS, codec_main.set, 'Standby', "Deactivate")
room_mode.addScript(RoomOperationMode.omVCS, codec_reserv.set, 'Standby', "Deactivate")


InitModule(__name__)

