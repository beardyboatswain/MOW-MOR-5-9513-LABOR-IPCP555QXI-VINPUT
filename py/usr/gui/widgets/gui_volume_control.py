from extronlib import event, Version
from extronlib.device import eBUSDevice, ProcessorDevice, UIDevice
from extronlib.interface import (CircuitBreakerInterface, ContactInterface,
    DigitalInputInterface, DigitalIOInterface, EthernetClientInterface,
    EthernetServerInterfaceEx, FlexIOInterface, IRInterface, PoEInterface,
    RelayInterface, SerialInterface, SWACReceptacleInterface, SWPowerInterface,
    VolumeInterface)
from extronlib.ui import Button, Knob, Label, Level
from extronlib.system import Clock, MESet, Timer, Wait

import lib.utils.signals as signals
from lib.var.states import *
from usr.dev.dev import ipad_adm, ipad_usr
from AudioControls import FaderControl, CrosspointControl, SignalPresent

from lib.utils.debugger import debugger
from usr.var.debug_mode import gui_volume_control_dbg
dbg = debugger(gui_volume_control_dbg, __name__)

# KARAOKE MUTE _______________________________________________________________________________________________
faderMicKaraoke = FaderControl(ipad_adm, instancetag='LVL_KARAOKE', channel='1', name='Караоке') 
faderMicKaraoke.setMechanics(433, 434, 435, 436, 437, 438, -50, 0, 1)

faderMicKaraoke = FaderControl(ipad_usr, instancetag='LVL_KARAOKE', channel='1', name='Караоке') 
faderMicKaraoke.setMechanics(433, 434, 435, 436, 437, 438, -50, 0, 1)


# Уровни громкости _____________________________________________________________
faderVcsMic = FaderControl(ipad_adm, instancetag='LVL_MIC_TO_VCS', channel='1', name='Микро-\nфоны\nв ВКС') 
faderVcsMic.setMechanics(313, 314, 315, 316, 317, 318, -100, 12, 1)

faderVcsCont = FaderControl(ipad_adm, instancetag='LVL_CONTENT_TO_VCS', channel='1', name='Контент\nв ВКС') 
faderVcsCont.setMechanics(319, 320, 321, 322, 323, 324, -100, 12, 1)

faderACMedia = FaderControl(ipad_adm, instancetag='LVL_PROG_MEDIA', channel='1', name='Контент\nв Зал') 
faderACMedia.setMechanics(325, 326, 327, 328, 329, 330, -100, 12, 1)

faderACTrub = FaderControl(ipad_adm, instancetag='LVL_PROG_VCS', channel='1', name='ВКС\nв Зал') 
faderACTrub.setMechanics(331, 332, 333, 334, 335, 336, -100, 12, 1)

faderACMic = FaderControl(ipad_adm,  instancetag='LVL_PROG_MICS', channel='1', name='Микро-\nфоны\nв Зал') 
faderACMic.setMechanics(337, 338, 339, 340, 341, 342, -100, 12, 1)



faderVcsMicUsr = FaderControl(ipad_usr, instancetag='LVL_MIC_TO_VCS', channel='1', name='Микро-\nфоны\nв ВКС') 
faderVcsMicUsr.setMechanics(313, 314, 315, 316, 317, 318, -100, 12, 1)

faderVcsContUsr = FaderControl(ipad_usr, instancetag='LVL_CONTENT_TO_VCS', channel='1', name='Контент\nв ВКС') 
faderVcsContUsr.setMechanics(319, 320, 321, 322, 323, 324, -100, 12, 1)

faderACMediaUsr = FaderControl(ipad_usr, instancetag='LVL_PROG_MEDIA', channel='1', name='Контент\nв Зал') 
faderACMediaUsr.setMechanics(325, 326, 327, 328, 329, 330, -100, 12, 1)

faderACTrubUsr = FaderControl(ipad_usr, instancetag='LVL_PROG_VCS', channel='1', name='ВКС\nв Зал') 
faderACTrubUsr.setMechanics(331, 332, 333, 334, 335, 336, -100, 12, 1)

faderACMicUsr = FaderControl(ipad_usr, instancetag='LVL_PROG_MICS', channel='1', name='Микро-\nфоны\nв Зал') 
faderACMicUsr.setMechanics(337, 338, 339, 340, 341, 342, -100, 12, 1)



# faderStgMonitors = FaderControl(iPadAdm, devicenumber='2', instanceid='536', channel='1', name='Мониторы\nСцены\n(Микрофоны)') 
# faderStgMonitors.setMechanics(349, 350, 351, 352, 353, 354, -100, 12, 1)


# Входные уровни громкости _____________________________________________________________
faderInStgLeftLuc = FaderControl(ipad_adm, instancetag='LVL_IN_VCS', channel='1', name='ВКС') 
faderInStgLeftLuc.setMechanics(355, 356, 357, 358, 359, 360, -100, 12, 1)

faderInStgRightLuc = FaderControl(ipad_adm, instancetag='LVL_IN_TRIBUNE', channel='1', name='Ноутбук\nна\nТрибуне') 
faderInStgRightLuc.setMechanics(361, 362, 363, 364, 365, 366, -100, 12, 1)

faderInTribLaptop = FaderControl(ipad_adm, instancetag='LVL_IN_OPER_MJACK', channel='1', name='mJack\nу Опера-\nтора') 
faderInTribLaptop.setMechanics(367, 368, 369, 370, 371, 372, -100, 12, 1)


# Микшер и микрофоны _____________________________________________________________
faderMXW = FaderControl(ipad_adm, instancetag='LVL_IN_MIC_MXW', channel='1', name='MXW') 
faderMXW.setMechanics(385, 386, 387, 388, 389, 390, -100, 12, 1)

faderMicWired = FaderControl(ipad_adm, instancetag='LVL_IN_MIC_WIRED', channel='1', name='Провод-\nные') 
faderMicWired.setMechanics(391, 392, 393, 394, 395, 396, -100, 12, 1)

faderMicRadio1 = FaderControl(ipad_adm, instancetag='LVL_IN_MIC_RF', channel='1', name='Радио 1') 
faderMicRadio1.setMechanics(397, 398, 399, 400, 401, 402, -100, 12, 1)

faderMicRadio2 = FaderControl(ipad_adm, instancetag='LVL_IN_MIC_RF', channel='2', name='Радио 2') 
faderMicRadio2.setMechanics(403, 404, 405, 406, 407, 408, -100, 12, 1)

faderMicRadio3 = FaderControl(ipad_adm, instancetag='LVL_IN_MIC_RF', channel='3', name='Радио 3') 
faderMicRadio3.setMechanics(409, 410, 411, 412, 413, 414, -100, 12, 1)

faderMicRadio4 = FaderControl(ipad_adm, instancetag='LVL_IN_MIC_RF', channel='4', name='Радио 4') 
faderMicRadio4.setMechanics(415, 416, 417, 418, 419, 420, -100, 12, 1)

faderMicRadio5 = FaderControl(ipad_adm, instancetag='LVL_IN_MIC_RF', channel='5', name='Радио 5') 
faderMicRadio5.setMechanics(421, 422, 423, 424, 425, 426, -100, 12, 1)

faderMicRadio6 = FaderControl(ipad_adm, instancetag='LVL_IN_MIC_RF', channel='6', name='Радио 6') 
faderMicRadio6.setMechanics(427, 428, 429, 430, 431, 432, -100, 12, 1)




# Микс в АС зала _____________________________________________________________________________________________
cpHallRadio = CrosspointControl(ipad_adm, instancetag='SM_PROG_MICS', inputs=['1'], outputs=['1'], name='Paдио\nМикрофоны')
cpHallRadio.setMechanics(451)
cpHallMXW = CrosspointControl(ipad_adm, instancetag='SM_PROG_MICS', inputs=['2'], outputs=['1'], name='MXW\nМикрофоны')
cpHallMXW.setMechanics(452)
cpHallWired = CrosspointControl(ipad_adm, instancetag='SM_PROG_MICS', inputs=['3'], outputs=['1'], name='Проводные\nМикрофоны')
cpHallWired.setMechanics(453)

cpHallVcs = CrosspointControl(ipad_adm, instancetag='SM_PROG_MEDIA', inputs=['3','4'], outputs=['3','4'], stereo=True, name='ВКС')
cpHallVcs.setMechanics(454)
cpHallTribLaptop = CrosspointControl(ipad_adm, instancetag='SM_PROG_SOURCES', inputs=['1','2'], outputs=['1','2'], stereo=True, name='Ноутбук\nна Трибуне')
cpHallTribLaptop.setMechanics(455)
cpHallOpPC = CrosspointControl(ipad_adm,  instancetag='SM_PROG_SOURCES', inputs=['3','4'], outputs=['1','2'], stereo=True, name='Компьютер\nОператора')
cpHallOpPC.setMechanics(456)


# cpOpWired = CrosspointControl(iPadAdm, devicenumber='2', instanceid='533', inputs=['1'], outputs=['1'], name='Проводные\nМикрофоны')
# # Микс Оператору _____________________________________________________________________________________________
# cpOpRadio = CrosspointControl(iPadAdm, devicenumber='2', instanceid='533', inputs=['2'], outputs=['1'], name='Радио\nМикрофоны')
# cpOpWired.setMechanics(461)
# cpOpRadio.setMechanics(462)
# cpOpRadioP = CrosspointControl(iPadAdm, devicenumber='2', instanceid='533', inputs=['3'], outputs=['1'], name='Петличные\nМикрофоны')
# cpOpRadioP.setMechanics(463)
# cpOpMixConsole = CrosspointControl(iPadAdm, devicenumber='2', instanceid='533', inputs=['4'], outputs=['1'], name='Микшерный\nПульт')
# cpOpMixConsole.setMechanics(464)
# cpOpTribLaptop = CrosspointControl(iPadAdm, devicenumber='2', instanceid='531', inputs=['2','3'], outputs=['1'], name='Ноутбук\nна Трибуне')
# cpOpTribLaptop.setMechanics(465)
# cpOpOpPC = CrosspointControl(iPadAdm, devicenumber='2', instanceid='531', inputs=['4','5'], outputs=['1'], name='Компьютер\nОператора')
# cpOpOpPC.setMechanics(466)
# cpOpStgLeftLuk = CrosspointControl(iPadAdm, devicenumber='2', instanceid='531', inputs=['6','7'], outputs=['1'], name='Сцена\nЛевый Люк')
# cpOpStgLeftLuk.setMechanics(467)
# cpOpStgRightLuk = CrosspointControl(iPadAdm, devicenumber='2', instanceid='531', inputs=['8','9'], outputs=['1'], name='Сцена\nПравый Люк')
# cpOpStgRightLuk.setMechanics(468)
# cpOpVcs = CrosspointControl(iPadAdm, devicenumber='2', instanceid='531', inputs=['10','11'], outputs=['1'], name='ВКС')
# cpOpVcs.setMechanics(469)


# Наличие сигнала _____________________________________________________________________________________________

spmMXWMic = SignalPresent(ipad_adm, instancetag='SPM_MXW_MICS', channel='1', name='MXWMics')
spmMXWMic.setMechanics(501)

spmWireMics = SignalPresent(ipad_adm, instancetag='SPM_WIRE_MICS', channel='1', name='WireMics')
spmWireMics.setMechanics(502)

spmRFMic1 = SignalPresent(ipad_adm, instancetag='TRACKING_SPM', channel='1', name='RFMic1')
spmRFMic1.setMechanics(503)
spmRFMic2 = SignalPresent(ipad_adm, instancetag='TRACKING_SPM', channel='2', name='RFMic2')
spmRFMic2.setMechanics(504)
spmRFMic3 = SignalPresent(ipad_adm, instancetag='TRACKING_SPM', channel='3', name='RFMic3')
spmRFMic3.setMechanics(505)
spmRFMic4 = SignalPresent(ipad_adm, instancetag='TRACKING_SPM', channel='4', name='RFMic4')
spmRFMic4.setMechanics(506)
spmRFMic5 = SignalPresent(ipad_adm, instancetag='TRACKING_SPM', channel='5', name='RFMic5')
spmRFMic5.setMechanics(507)
spmRFMic6 = SignalPresent(ipad_adm, instancetag='TRACKING_SPM', channel='6', name='RFMic6')
spmRFMic6.setMechanics(508)

# Синхронизировать матрицы
# btnSynchroHallToOper = Button(iPadAdm, 450)

# def synchroHallToOper():
#     cpOpWired.setValue(cpHallWired.getValue())
#     cpOpRadio.setValue(cpHallRadio.getValue())
#     cpOpRadioP.setValue(cpHallRadioP.getValue())
#     cpOpMixConsole.setValue(cpHallMixConsole.getValue())
#     cpOpTribLaptop.setValue(cpHallTribLaptop.getValue())
#     cpOpOpPC.setValue(cpHallOpPC.getValue())
#     cpOpStgLeftLuk.setValue(cpHallStgLeftLuk.getValue())
#     cpOpStgRightLuk.setValue(cpHallStgRightLuk.getValue())
#     cpOpVcs.setValue(cpHallVcs.getValue())

# @event(btnSynchroHallToOper, sStates)
# def btnSynchroHallToOperHandler(btn, state):
#     if (state == sPressed):
#         btn.SetState(1)
#     elif (state == sReleased):
#         btn.SetState(0)
#         synchroHallToOper()


# Вернуть исходные настройки __________________________________________________
btnAlarmaSound = Button(ipad_adm, 90)

@event(btnAlarmaSound, sStates)
def btnSynchroHallToOperHandler(btn, state):
    if (state == sPressed):
        btn.SetState(1)
    elif (state == sReleased):
        btn.SetState(0)
        signals.emit('*', signal='biamp_preset_recall', params={'Preset':'1'})    


def Initialize():
   print("<{}> imported!".format(__name__))

Initialize()
