#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.video.VideoMatrixXTP import MatrixXTP
from lib.video.VideoMatrixInfobit import MatrixInfobitHxxHAW
from lib.video.VideoControl import VideoControl, VideoOutFastTie


from lib.utils.debugger import debuggerNet as debugger
from usr.var.debug_mode import gui_video_control_dbg
dbg = debugger(gui_video_control_dbg, __name__)

from usr.dev.dev import ipad_adm, ipad_usr, xtp_matrix, infbt_matrix
from usr.var.video_vars import (VIDEO_INPUTS_XTP,
                                VIDEO_OUTPUTS_XTP,
                                VIDEO_OUTPUTS_INFBT,
                                VIDEO_INPUTS_INFBT,
                                LINK_CODEC_CAM,
                                LINK_CODEC_PRES,
                                LINK_LED_MAIN_L_SCREEN,
                                LINK_LED_MAIN_R_SCREEN,
                                LINK_CHAT_SCREEN,
                                LINK_DUPLICATE_SCREEN_A,
                                LINK_DUPLICATE_SCREEN_B,
                                LINK_INPUT_DEEMBD,
                                )

import lib.utils.signals as signals

# todo: сделать виртуальную матрицу, чтобы управлять переключением камер
some_virtual_matrix = MatrixInfobitHxxHAW(infbt_matrix, 4, 4)

# --- XTP Control -----------------------------------------------------------------------
xtp_sw = MatrixXTP(xtp_matrix, inSize=64, outSize=64)
xtp_ctrl_adm = VideoControl(ipad_adm, xtp_sw)

# --- page selecting for output buttons -------------------------------------------------
for iO in VIDEO_OUTPUTS_XTP:
    vO = VIDEO_OUTPUTS_XTP.get(iO)
    xtp_ctrl_adm.addOutputButton(vName=vO.get("name"),
                                 vOutNumber=vO.get("out"),
                                 vBtnBaseID=vO.get("btnid"),
                                 vType=vO.get("type"))

for iI in VIDEO_INPUTS_XTP:
    vI = VIDEO_INPUTS_XTP.get(iI)
    xtp_ctrl_adm.addInputButton(vName=vI.get("name"),
                                vInNumber=vI.get("in"),
                                vBtnBaseID=vI.get("btnid"),
                                vType=vI.get("type"))

xtp_ctrl_adm.addDisplayPopupSelector("215_Video_Displays_PageSelector_PP")

xtp_ctrl_adm.addDisplaysPopupPage(1911, "211_Video_Displays_1_PP")
xtp_ctrl_adm.addDisplaysPopupPage(1912, "212_Video_Displays_2_PP")
xtp_ctrl_adm.addDisplaysPopupPage(1913, "213_Video_Displays_3_PP")
xtp_ctrl_adm.addDisplaysPopupPage(1914, "214_Video_Displays_iMatrix_PP")
xtp_ctrl_adm.addInputsPopupPage(1901, "220_Vdieo_Source_Selection_F_PP")
xtp_ctrl_adm.addInputsPopupPage(1902, "216_Vdieo_Source_Selection_1_PP")
xtp_ctrl_adm.addInputsPopupPage(1903, "217_Vdieo_Source_Selection_2_PP")
xtp_ctrl_adm.addInputsPopupPage(1904, "218_Vdieo_Source_Selection_3_PP")
xtp_ctrl_adm.addInputsPopupPageMechanic(btnCloseSrcPopupID=1001, lblCurrentOutID=1002)


# --- Linked outputs --------------------------------------------------------------------
xtp_ctrl_adm.addConnectedOutputs(mainOut=LINK_CODEC_CAM["main"],
                                 slaveOuts=LINK_CODEC_CAM["slave"],
                                 inclIns=LINK_CODEC_CAM["ins"])
xtp_ctrl_adm.addConnectedOutputs(mainOut=LINK_CODEC_PRES["main"],
                                 slaveOuts=LINK_CODEC_PRES["slave"],
                                 inclIns=LINK_CODEC_PRES["ins"])
xtp_ctrl_adm.addConnectedOutputs(mainOut=LINK_LED_MAIN_L_SCREEN["main"],
                                 slaveOuts=LINK_LED_MAIN_L_SCREEN["slave"],
                                 inclIns=LINK_LED_MAIN_L_SCREEN["ins"])
xtp_ctrl_adm.addConnectedOutputs(mainOut=LINK_LED_MAIN_R_SCREEN["main"],
                                 slaveOuts=LINK_LED_MAIN_R_SCREEN["slave"],
                                 inclIns=LINK_LED_MAIN_R_SCREEN["ins"])
xtp_ctrl_adm.addConnectedOutputs(mainOut=LINK_CHAT_SCREEN["main"],
                                 slaveOuts=LINK_CHAT_SCREEN["slave"],
                                 inclIns=LINK_CHAT_SCREEN["ins"])
xtp_ctrl_adm.addConnectedOutputs(mainOut=LINK_DUPLICATE_SCREEN_A["main"],
                                 slaveOuts=LINK_DUPLICATE_SCREEN_A["slave"],
                                 inclIns=LINK_DUPLICATE_SCREEN_A["ins"])
xtp_ctrl_adm.addConnectedOutputs(mainOut=LINK_DUPLICATE_SCREEN_B["main"],
                                 slaveOuts=LINK_DUPLICATE_SCREEN_B["slave"],
                                 inclIns=LINK_DUPLICATE_SCREEN_B["ins"])
xtp_ctrl_adm.addConnectedOutputs(mainOut=LINK_INPUT_DEEMBD["main"],
                                 slaveOuts=LINK_INPUT_DEEMBD["slave"],
                                 inclIns=LINK_INPUT_DEEMBD["ins"])


# --- INFOBIT Control -------------------------------------------------------------------
infbt_ctrl_adm = VideoControl(ipad_adm, xtp_sw)

for iO in VIDEO_OUTPUTS_INFBT:
    vO = VIDEO_OUTPUTS_INFBT.get(iO)
    infbt_ctrl_adm.addOutputButton(vName=vO.get("name"),
                                   vOutNumber=vO.get("out"),
                                   vBtnBaseID=vO.get("btnid"),
                                   vType=vO.get("type")
                                   )

for iI in VIDEO_INPUTS_INFBT:
    vI = VIDEO_INPUTS_INFBT.get(iI)
    dbg.print("Add IN: {}".format(vI))
    infbt_ctrl_adm.addInputButton(vName=vI.get("name"),
                                  vInNumber=vI.get("in"),
                                  vBtnBaseID=vI.get("btnid"),
                                  vType=vI.get("type")
                                  )

infbt_ctrl_adm.addInputsPopupPage(1905, "219_Vdieo_Source_Selection_iMatrix_PP")
infbt_ctrl_adm.addInputsPopupPageMechanic(btnCloseSrcPopupID=1003, lblCurrentOutID=1004)


# --- VCS mode ------------------------------------------------------------------------------------
# --- USR -----------------------------------------------------------------------------------------

usrOTFMainScreen = VideoOutFastTie(UIHost=iPadUsr,
                                   videoControlProxy=kramerSWProxy,
                                   output=videoOutputs.get(1).get("out"),
                                   outputName=videoOutputs.get(1).get("name"),
                                   lblOutputNameID=1701,
                                   lblOutputCurrentInID=1702)
usrOTFMainScreen.addInNames(inNames)
usrOTFMainScreen.addInputButton(vName=videoInputs.get(3).get("name"),
                                vInNumber=videoInputs.get(3).get("in"),
                                vBtnBaseID=1703,
                                vType=videoInputs.get(3).get("type"))
usrOTFMainScreen.addInputButton(vName=videoInputs.get(4).get("name"),
                                vInNumber=videoInputs.get(4).get("in"),
                                vBtnBaseID=1706,
                                vType=videoInputs.get(4).get("type"))

usrOTFAdditionslScreen = VideoOutFastTie(UIHost=iPadUsr,
                                         videoControlProxy=kramerSWProxy,
                                         output=videoOutputs.get(2).get("out"),
                                         outputName=videoOutputs.get(2).get("name"),
                                         lblOutputNameID=1709,
                                         lblOutputCurrentInID=1710)
usrOTFAdditionslScreen.addInNames(inNames)
usrOTFAdditionslScreen.addInputButton(vName=videoInputs.get(3).get("name"),
                                      vInNumber=videoInputs.get(3).get("in"),
                                      vBtnBaseID=1711,
                                      vType=videoInputs.get(3).get("type"))
usrOTFAdditionslScreen.addInputButton(vName=videoInputs.get(4).get("name"),
                                      vInNumber=videoInputs.get(4).get("in"),
                                      vBtnBaseID=1714,
                                      vType=videoInputs.get(4).get("type"))

usrOTFChatScreen = VideoOutFastTie(UIHost=iPadUsr,
                                   videoControlProxy=kramerSWProxy,
                                   output=videoOutputs.get(4).get("out"),
                                   outputName=videoOutputs.get(4).get("name"),
                                   lblOutputNameID=1717,
                                   lblOutputCurrentInID=1718)
usrOTFChatScreen.addInNames(inNames)
usrOTFChatScreen.addInputButton(vName=videoInputs.get(3).get("name"),
                                vInNumber=videoInputs.get(3).get("in"),
                                vBtnBaseID=1719,
                                vType=videoInputs.get(3).get("type"))
usrOTFChatScreen.addInputButton(vName=videoInputs.get(4).get("name"),
                                vInNumber=videoInputs.get(4).get("in"),
                                vBtnBaseID=1722,
                                vType=videoInputs.get(4).get("type"))
usrOTFChatScreen.addInputButton(vName=videoInputs.get(9).get("name"),
                                vInNumber=videoInputs.get(9).get("in"),
                                vBtnBaseID=1725,
                                vType=videoInputs.get(9).get("type"))

# --- ADM -----------------------------------------------------------------------------------------
admOTFMainScreen = VideoOutFastTie(UIHost=iPadAdm,
                                   videoControlProxy=kramerSWProxy,
                                   output=videoOutputs.get(1).get("out"),
                                   outputName=videoOutputs.get(1).get("name"),
                                   lblOutputNameID=1701,
                                   lblOutputCurrentInID=1702)
admOTFMainScreen.addInNames(inNames)
admOTFMainScreen.addInputButton(vName=videoInputs.get(3).get("name"),
                                vInNumber=videoInputs.get(3).get("in"),
                                vBtnBaseID=1703,
                                vType=videoInputs.get(3).get("type"))
admOTFMainScreen.addInputButton(vName=videoInputs.get(4).get("name"),
                                vInNumber=videoInputs.get(4).get("in"),
                                vBtnBaseID=1706,
                                vType=videoInputs.get(4).get("type"))

admOTFAdditionslScreen = VideoOutFastTie(UIHost=iPadAdm,
                                         videoControlProxy=kramerSWProxy,
                                         output=videoOutputs.get(2).get("out"),
                                         outputName=videoOutputs.get(2).get("name"),
                                         lblOutputNameID=1709,
                                         lblOutputCurrentInID=1710)
admOTFAdditionslScreen.addInNames(inNames)
admOTFAdditionslScreen.addInputButton(vName=videoInputs.get(3).get("name"),
                                      vInNumber=videoInputs.get(3).get("in"),
                                      vBtnBaseID=1711,
                                      vType=videoInputs.get(3).get("type"))
admOTFAdditionslScreen.addInputButton(vName=videoInputs.get(4).get("name"),
                                      vInNumber=videoInputs.get(4).get("in"),
                                      vBtnBaseID=1714,
                                      vType=videoInputs.get(4).get("type"))

admOTFChatScreen = VideoOutFastTie(UIHost=iPadAdm,
                                   videoControlProxy=kramerSWProxy,
                                   output=videoOutputs.get(4).get("out"),
                                   outputName=videoOutputs.get(4).get("name"),
                                   lblOutputNameID=1717,
                                   lblOutputCurrentInID=1718)
admOTFChatScreen.addInNames(inNames)
admOTFChatScreen.addInputButton(vName=videoInputs.get(3).get("name"),
                                vInNumber=videoInputs.get(3).get("in"),
                                vBtnBaseID=1719,
                                vType=videoInputs.get(3).get("type"))
admOTFChatScreen.addInputButton(vName=videoInputs.get(4).get("name"),
                                vInNumber=videoInputs.get(4).get("in"),
                                vBtnBaseID=1722,
                                vType=videoInputs.get(4).get("type"))
admOTFChatScreen.addInputButton(vName=videoInputs.get(9).get("name"),
                                vInNumber=videoInputs.get(9).get("in"),
                                vBtnBaseID=1725,
                                vType=videoInputs.get(9).get("type"))


# --- Cinema mode ---------------------------------------------------------------------------------
# --- USR -----------------------------------------------------------------------------------------
"""
usrOTFMainScreenCinema = VideoOutFastTie(UIHost=iPadUsr,
                                         videoControlProxy=kramerSWProxy,
                                         output=videoOutputs.get(1).get("out"),
                                         outputName=videoOutputs.get(1).get("name"),
                                         lblOutputNameID=1728,
                                         lblOutputCurrentInID=1729)
usrOTFMainScreenCinema.addInNames(inNames)
usrOTFMainScreenCinema.addInputButton(vName=videoInputs.get(1).get("name"),
                                      vInNumber=videoInputs.get(1).get("in"),
                                      vBtnBaseID=1730,
                                      vType=videoInputs.get(1).get("type"))
usrOTFMainScreenCinema.addInputButton(vName=videoInputs.get(2).get("name"),
                                      vInNumber=videoInputs.get(2).get("in"),
                                      vBtnBaseID=1733,
                                      vType=videoInputs.get(2).get("type"))
usrOTFMainScreenCinema.addInputButton(vName=videoInputs.get(15).get("name"),
                                      vInNumber=videoInputs.get(15).get("in"),
                                      vBtnBaseID=1736,
                                      vType=videoInputs.get(15).get("type"))
usrOTFMainScreenCinema.addInputButton(vName=videoInputs.get(16).get("name"),
                                      vInNumber=videoInputs.get(16).get("in"),
                                      vBtnBaseID=1739,
                                      vType=videoInputs.get(16).get("type"))

# --- ADM -----------------------------------------------------------------------------------------
admOTFMainScreenCinema = VideoOutFastTie(UIHost=iPadAdm,
                                         videoControlProxy=kramerSWProxy,
                                         output=videoOutputs.get(1).get("out"),
                                         outputName=videoOutputs.get(1).get("name"),
                                         lblOutputNameID=1728,
                                         lblOutputCurrentInID=1729)
admOTFMainScreenCinema.addInNames(inNames)
admOTFMainScreenCinema.addInputButton(vName=videoInputs.get(1).get("name"),
                                      vInNumber=videoInputs.get(1).get("in"),
                                      vBtnBaseID=1730,
                                      vType=videoInputs.get(1).get("type"))
admOTFMainScreenCinema.addInputButton(vName=videoInputs.get(2).get("name"),
                                      vInNumber=videoInputs.get(2).get("in"),
                                      vBtnBaseID=1733,
                                      vType=videoInputs.get(2).get("type"))
admOTFMainScreenCinema.addInputButton(vName=videoInputs.get(15).get("name"),
                                      vInNumber=videoInputs.get(15).get("in"),
                                      vBtnBaseID=1736,
                                      vType=videoInputs.get(15).get("type"))
admOTFMainScreenCinema.addInputButton(vName=videoInputs.get(16).get("name"),
                                      vInNumber=videoInputs.get(16).get("in"),
                                      vBtnBaseID=1739,
                                      vType=videoInputs.get(16).get("type"))
"""
