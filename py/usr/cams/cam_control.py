from extronlib import event
from extronlib.ui import Button

from lib.var.states import sStates, sPressed, sReleased
from lib.utils.system_init import InitModule
from lib.camera.CameraControl import CameraControlProcessor, CameraControlPanel
from lib.camera.CameraPanasonic import CameraControlPanasonic

from usr.dev.dev import ipad_adm, ipad_usr, cam_1_ip, cam_2_ip, cam_3_ip, cam_4_ip, cam_5_ip, cam_6_ip, cam_7_ip, cam_8_ip

# todo: тут нужна будет виртуальная матрица,
# todo: так как управлять переключением придется сразу на двух матрицах
from usr.video.video_control import some_virtual_matrix

cam_1 = CameraControlPanasonic(id=1, ip=cam_1_ip.ip, port=cam_1_ip.port, username=cam_1_ip.login, password=cam_1_ip.password)
cam_2 = CameraControlPanasonic(id=2, ip=cam_2_ip.ip, port=cam_2_ip.port, username=cam_2_ip.login, password=cam_2_ip.password)
cam_3 = CameraControlPanasonic(id=3, ip=cam_3_ip.ip, port=cam_3_ip.port, username=cam_3_ip.login, password=cam_3_ip.password)
cam_4 = CameraControlPanasonic(id=4, ip=cam_4_ip.ip, port=cam_4_ip.port, username=cam_4_ip.login, password=cam_4_ip.password)
cam_5 = CameraControlPanasonic(id=5, ip=cam_5_ip.ip, port=cam_5_ip.port, username=cam_5_ip.login, password=cam_5_ip.password)
cam_6 = CameraControlPanasonic(id=6, ip=cam_6_ip.ip, port=cam_6_ip.port, username=cam_6_ip.login, password=cam_6_ip.password)
cam_7 = CameraControlPanasonic(id=7, ip=cam_7_ip.ip, port=cam_7_ip.port, username=cam_7_ip.login, password=cam_7_ip.password)
cam_8 = CameraControlPanasonic(id=8, ip=cam_8_ip.ip, port=cam_8_ip.port, username=cam_8_ip.login, password=cam_8_ip.password)


roomCamProcessor = CameraControlProcessor(firstPreset=4101, presetNumber=82)
roomCamProcessor.addCamera(cam_1, 33)
roomCamProcessor.addCamera(cam_2, 34)
roomCamProcessor.addCamera(cam_3, 35)
roomCamProcessor.addCamera(cam_4, 36)
roomCamProcessor.addCamera(cam_5, 37)
roomCamProcessor.addCamera(cam_6, 38)
roomCamProcessor.addCamera(cam_7, 59)
roomCamProcessor.addCamera(cam_8, 60)
roomCamProcessor.addCamSwitcher(some_virtual_matrix)
roomCamProcessor.addCamSwitcherActiveCamOutput([11, 15, 17])

admCamController = CameraControlPanel(uiHost=ipad_adm, camProcessor=roomCamProcessor)
admCamController.addCameraSelector(firstCamBtnId=4001)
admCamController.addDPad(upBtnId=4011, downBtnId=4012, leftBtnId=4013, rightBtnId=4014, teleBtnId=4015, wideBtnId=4016)
admCamController.addPresetButtons(presetSavedProbeID=4100)

usrCamController = CameraControlPanel(uiHost=ipad_usr, camProcessor=roomCamProcessor)
usrCamController.addCameraSelector(firstCamBtnId=4001)
usrCamController.addDPad(upBtnId=4011, downBtnId=4012, leftBtnId=4013, rightBtnId=4014, teleBtnId=4015, wideBtnId=4016)
usrCamController.addPresetButtons(presetSavedProbeID=4100)


# --- USR CAM POPUP and PRESETS ------------------------------------------------------------------------------------
btnCamControlShowPPMainID = 107
btnCamControlShowPPNameID = 108
btnCamControlShowPPCommentID = 109
btnCamControlShowPPNameText = "Camera\nControl"
btnCamControlShowPPCommentText = "Setting up cameras view for call"
btnCamControlClosePP = 110
ppNameCamControl = "115_CamControl_PP"

btnCamControlShowPPMainUsr = Button(ipad_usr, btnCamControlShowPPMainID)
btnCamControlShowPPNameUsr = Button(ipad_usr, btnCamControlShowPPNameID)
btnCamControlShowPPNameUsr.SetText(btnCamControlShowPPNameText)
btnCamControlShowPPCommentUsr = Button(ipad_usr, btnCamControlShowPPCommentID)
btnCamControlShowPPCommentUsr.SetText(btnCamControlShowPPCommentText)

btnCamControlShowPPMainAdm = Button(ipad_adm, btnCamControlShowPPMainID)
btnCamControlShowPPNameAdm = Button(ipad_adm, btnCamControlShowPPNameID)
btnCamControlShowPPNameAdm.SetText(btnCamControlShowPPNameText)
btnCamControlShowPPCommentAdm = Button(ipad_adm, btnCamControlShowPPCommentID)
btnCamControlShowPPCommentAdm.SetText(btnCamControlShowPPCommentText)

btnPresetUsrPPShow = [btnCamControlShowPPMainUsr,
                      btnCamControlShowPPNameUsr,
                      btnCamControlShowPPCommentUsr,
                      btnCamControlShowPPMainAdm,
                      btnCamControlShowPPNameAdm,
                      btnCamControlShowPPCommentAdm]

btnCamControlClosePPUsr = Button(ipad_usr, btnCamControlClosePP)
btnCamControlClosePPAdm = Button(ipad_adm, btnCamControlClosePP)

btnPresetUsrPPClose = [btnCamControlClosePPUsr, btnCamControlClosePPAdm]


@event(btnPresetUsrPPShow, sStates)
def btnPresetUsrPPShowEventHandler(btn: Button, state: str):
    if (state == sPressed):
        for iBtn in btnPresetUsrPPShow:
            iBtn.SetState(1)
    elif (state == sReleased):
        for iBtn in btnPresetUsrPPShow:
            iBtn.SetState(0)
            ipad_usr.ShowPopup(ppNameCamControl)
            ipad_adm.ShowPopup(ppNameCamControl)


@event(btnPresetUsrPPClose, sStates)
def btnPresetUsrPPCloseEventHandler(btn: Button, state: str):
    if (state == sPressed):
        for iBtn in btnPresetUsrPPClose:
            iBtn.SetState(1)
    elif (state == sReleased):
        for iBtn in btnPresetUsrPPClose:
            iBtn.SetState(0)
            ipad_usr.HidePopup(ppNameCamControl)
            ipad_adm.HidePopup(ppNameCamControl)


InitModule(__name__)
