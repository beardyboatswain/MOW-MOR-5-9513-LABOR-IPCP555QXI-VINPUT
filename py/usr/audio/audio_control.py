#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from usr.dev.dev import ipad_usr, ipad_adm
from lib.audio.AudioControlSymetrix import (FaderControl,
                                            # CrosspointControl,
                                            # SignalPresentMeter,
                                            SignalProbe,
                                            # MuteControl,
                                            PresetControl)

from lib.var.states import sPressed, sReleased, sStates
from lib.utils.system_init import InitModule

import lib.utils.signals as signals

from lib.utils.debugger import debuggerNet as debugger
from usr.var.debug_mode import audio_control_dbg
dbg = debugger(audio_control_dbg, __name__)

from usr.dev.dev import symetrix
from lib.audio.AudioProxySymetrix import AudioProxySymetrix

symetrix_proxy = AudioProxySymetrix(symetrix)


lvlMicInHall = FaderControl(dev=symetrix_proxy,
                            levelRcId=111,
                            muteRcId=121,
                            name="Мicorphones\nin hall",
                            comment="Level at which you hear yourself in hall",
                            minValue=-72)
lvlMicInHall.setMechanics(ipad_adm, 5001, 5002, 5003, 5004, 5005, 5006, 5007)
lvlMicInHall.setMechanics(ipad_usr, 5001, 5002, 5003, 5004, 5005, 5006, 5007)


lvlMediaInHall = FaderControl(dev=symetrix_proxy,
                              levelRcId=114,
                              muteRcId=124,
                              name="Presentation\nin hall",
                              comment="Level at which you hear your presentation",
                              minValue=-72)


lvlMediaInHall.setMechanics(ipad_adm, 5011, 5012, 5013, 5014, 5015, 5016, 5017)
lvlMediaInHall.setMechanics(ipad_usr, 5011, 5012, 5013, 5014, 5015, 5016, 5017)


lvlVCSInHall = FaderControl(dev=symetrix_proxy,
                            levelRcId=113,
                            muteRcId=123,
                            name="Sound of\nmedia",
                            comment="Level at which participants hear call and presentation",
                            minValue=-72)
lvlVCSInHall.setMechanics(ipad_adm, 5021, 5022, 5023, 5024, 5025, 5026, 5027)
lvlVCSInHall.setMechanics(ipad_usr, 5021, 5022, 5023, 5024, 5025, 5026, 5027)


lvlMicInCall = FaderControl(dev=symetrix_proxy,
                            levelRcId=112,
                            muteRcId=122,
                            name="Мicorphones\nin call",
                            comment="Level at which you hear yourself in hall",
                            minValue=-72)
lvlMicInCall.setMechanics(ipad_adm, 5031, 5032, 5033, 5034, 5035, 5036, 5037)
lvlMicInCall.setMechanics(ipad_usr, 5031, 5032, 5033, 5034, 5035, 5036, 5037)

lvlMediaInCall = FaderControl(dev=symetrix_proxy,
                              levelRcId=115,
                              muteRcId=125,
                              name="Presentation\nin call",
                              comment="Level at which you hear yourself in hall",
                              minValue=-72)
lvlMediaInCall.setMechanics(ipad_adm, 5041, 5042, 5043, 5044, 5045, 5046, 5047)
lvlMediaInCall.setMechanics(ipad_usr, 5041, 5042, 5043, 5044, 5045, 5046, 5047)


"""
# --- Mic Uldx IN LEVELS -----------------------------------------------------------------------
lvlInUlxdMic1 = FaderControl(dev=biampProxy,
                             instancetag="LvlInMic1Ulxd",
                             channel=1,
                             name="",
                             comment="",
                             minValue=-80)
lvlInUlxdMic1.setMechanics(iPadAdm, 5111, 5112, 5113, 5114, 5115)

lvlInUlxdMic2 = FaderControl(dev=biampProxy,
                             instancetag="LvlInMic2Ulxd",
                             channel=1,
                             name="",
                             comment="",
                             minValue=-80)
lvlInUlxdMic2.setMechanics(iPadAdm, 5121, 5122, 5123, 5124, 5125)

lvlInUlxdMic3 = FaderControl(dev=biampProxy,
                             instancetag="LvlInMic3Ulxd",
                             channel=1,
                             name="",
                             comment="",
                             minValue=-80)
lvlInUlxdMic3.setMechanics(iPadAdm, 5131, 5132, 5133, 5134, 5135)

lvlInUlxdMic4 = FaderControl(dev=biampProxy,
                             instancetag="LvlInMic4Ulxd",
                             channel=1,
                             name="",
                             comment="",
                             minValue=-80)
lvlInUlxdMic4.setMechanics(iPadAdm, 5141, 5142, 5143, 5144, 5145)

# --- MXW IN LEVELS -------------------------------------------------------------------------------
lvlInMxwMic1 = FaderControl(dev=biampProxy,
                            instancetag="LvlInMic1MXW",
                            channel=1,
                            name="",
                            comment="",
                            minValue=-80)
lvlInMxwMic1.setMechanics(iPadAdm, 5211, 5212, 5213, 5214, 5215)

lvlInMxwMic2 = FaderControl(dev=biampProxy,
                            instancetag="LvlInMic2MXW",
                            channel=1,
                            name="",
                            comment="",
                            minValue=-80)
lvlInMxwMic2.setMechanics(iPadAdm, 5221, 5222, 5223, 5224, 5225)

lvlInMxwMic3 = FaderControl(dev=biampProxy,
                            instancetag="LvlInMic3MXW",
                            channel=1,
                            name="",
                            comment="",
                            minValue=-80)
lvlInMxwMic3.setMechanics(iPadAdm, 5231, 5232, 5233, 5234, 5235)

lvlInMxwMic4 = FaderControl(dev=biampProxy,
                            instancetag="LvlInMic4MXW",
                            channel=1,
                            name="",
                            comment="",
                            minValue=-80)
lvlInMxwMic4.setMechanics(iPadAdm, 5241, 5242, 5243, 5244, 5245)

lvlInMxwMic5 = FaderControl(dev=biampProxy,
                            instancetag="LvlInMic5MXW",
                            channel=1,
                            name="",
                            comment="",
                            minValue=-80)
lvlInMxwMic5.setMechanics(iPadAdm, 5251, 5252, 5253, 5254, 5255)

lvlInMxwMic6 = FaderControl(dev=biampProxy,
                            instancetag="LvlInMic6MXW",
                            channel=1,
                            name="",
                            comment="",
                            minValue=-80)
lvlInMxwMic6.setMechanics(iPadAdm, 5261, 5262, 5263, 5264, 5265)

lvlInMxwMic7 = FaderControl(dev=biampProxy,
                            instancetag="LvlInMic7MXW",
                            channel=1,
                            name="",
                            comment="",
                            minValue=-80)
lvlInMxwMic7.setMechanics(iPadAdm, 5271, 5272, 5273, 5274, 5275)

lvlInMxwMic8 = FaderControl(dev=biampProxy,
                            instancetag="LvlInMic8MXW",
                            channel=1,
                            name="",
                            comment="",
                            minValue=-80)
lvlInMxwMic8.setMechanics(iPadAdm, 5281, 5282, 5283, 5284, 5285)

# for i in biampProxy.levels:
#     print(i)
#     print(biampProxy.levels[i])


# --- OTHER INPUT LEVELS --------------------------------------------------------------------------

lvlInCisco = FaderControl(dev=biampProxy,
                          instancetag="LvlInCodecCisco",
                          channel=1,
                          name="",
                          comment="",
                          minValue=-80)
lvlInCisco.setMechanics(iPadAdm, 5301, 5302, 5303, 5304, 5305)

lvlInZoom = FaderControl(dev=biampProxy,
                         instancetag="LvlInPcZoom",
                         channel=1,
                         name="",
                         comment="",
                         minValue=-80)
lvlInZoom.setMechanics(iPadAdm, 5311, 5312, 5313, 5314, 5315)

lvlInDeembeder = FaderControl(dev=biampProxy,
                              instancetag="LvlInMedia",
                              channel=1,
                              name="",
                              comment="",
                              minValue=-80)
lvlInDeembeder.setMechanics(iPadAdm, 5321, 5322, 5323, 5324, 5325)

# --- OTHER OUTPUT LEVELS --------------------------------------------------------------------------

lvlOutFront = FaderControl(dev=biampProxy,
                           instancetag="LvlOutFront",
                           channel=1,
                           name="",
                           comment="",
                           minValue=-80)
lvlOutFront.setMechanics(iPadAdm, 5451, 5452, 5453, 5454, 5455)

lvlOutSub = FaderControl(dev=biampProxy,
                         instancetag="LvlOutSub",
                         channel=1,
                         name="",
                         comment="",
                         minValue=-80)
lvlOutSub.setMechanics(iPadAdm, 5461, 5462, 5463, 5464, 5465)

lvlOutMonitor = FaderControl(dev=biampProxy,
                             instancetag="LvlOutMonitor",
                             channel=1,
                             name="",
                             comment="",
                             minValue=-80)
lvlOutMonitor.setMechanics(iPadAdm, 5471, 5472, 5473, 5474, 5475)

lvlOutCelilingHall = FaderControl(dev=biampProxy,
                                  instancetag="LvlOutCell",
                                  channel=1,
                                  name="",
                                  comment="",
                                  minValue=-80)
lvlOutCelilingHall.setMechanics(iPadAdm, 5481, 5482, 5483, 5484, 5485)

'''
crOne = CrosspointControl(ui=iPadAdm,
                          dev=biampProxy,
                          instancetag="MM_MAIN",
                          name="_1-1",
                          points=((1, 1), ))
crOne.setMechanics(5701)

crTwo = CrosspointControl(ui=iPadAdm,
                          dev=biampProxy,
                          instancetag="MM_MAIN",
                          name="_2-2\n_2-3",
                          points=((2, 2), (2, 3)))
crTwo.setMechanics(5702)

crThree = CrosspointControl(ui=iPadAdm,
                            dev=biampProxy,
                            instancetag="MM_MAIN",
                            name="_3-3\n_4-4\n_5-5",
                            points=((3, 3), (4, 4), (5, 5)))
crThree.setMechanics(5703)
'''

spmMicS1 = SignalPresentMeter(ui=iPadAdm,
                              dev=biampProxy,
                              instancetag="SPM_RF_MICS",
                              channel=1,
                              name="S1")
spmMicS1.setMechanics(5751)

spmMicS2 = SignalPresentMeter(ui=iPadAdm,
                              dev=biampProxy,
                              instancetag="SPM_RF_MICS",
                              channel=2,
                              name="S2")
spmMicS2.setMechanics(5752)

spmMicS3 = SignalPresentMeter(ui=iPadAdm,
                              dev=biampProxy,
                              instancetag="SPM_RF_MICS",
                              channel=3,
                              name="S3")
spmMicS3.setMechanics(5753)

spmMicS4 = SignalPresentMeter(ui=iPadAdm,
                              dev=biampProxy,
                              instancetag="SPM_RF_MICS",
                              channel=4,
                              name="S4")
spmMicS4.setMechanics(5754)

spmMicH5 = SignalPresentMeter(ui=iPadAdm,
                              dev=biampProxy,
                              instancetag="SPM_RF_MICS",
                              channel=5,
                              name="H5")
spmMicH5.setMechanics(5755)

spmMicH6 = SignalPresentMeter(ui=iPadAdm,
                              dev=biampProxy,
                              instancetag="SPM_RF_MICS",
                              channel=6,
                              name="H6")
spmMicH6.setMechanics(5756)

spmMicH7 = SignalPresentMeter(ui=iPadAdm,
                              dev=biampProxy,
                              instancetag="SPM_RF_MICS",
                              channel=7,
                              name="H7")
spmMicH7.setMechanics(5757)

spmMicH8 = SignalPresentMeter(ui=iPadAdm,
                              dev=biampProxy,
                              instancetag="SPM_RF_MICS",
                              channel=8,
                              name="H8")
spmMicH8.setMechanics(5758)

spmMicH9 = SignalPresentMeter(ui=iPadAdm,
                              dev=biampProxy,
                              instancetag="SPM_RF_MICS",
                              channel=9,
                              name="H9")
spmMicH9.setMechanics(5759)

spmMicH10 = SignalPresentMeter(ui=iPadAdm,
                               dev=biampProxy,
                               instancetag="SPM_RF_MICS",
                               channel=10,
                               name="H10")
spmMicH10.setMechanics(5760)

spmMicH11 = SignalPresentMeter(ui=iPadAdm,
                               dev=biampProxy,
                               instancetag="SPM_RF_MICS",
                               channel=11,
                               name="H11")
spmMicH11.setMechanics(5761)

spmMicH12 = SignalPresentMeter(ui=iPadAdm,
                               dev=biampProxy,
                               instancetag="SPM_RF_MICS",
                               channel=12,
                               name="H12")
spmMicH12.setMechanics(5762)

mOneG = MuteControl(dev=biampProxy,
                    instancetag="M_SYSTEM_MUTE",
                    channel=1,
                    name="System\nMute",
                    comment="Mute all input and\noutput levels")
mOneG.setMechanics(iPadAdm, 5851, 5852, 5853)

mOneG = MuteControl(dev=biampProxy,
                    instancetag="LVL_KARAOKE",
                    channel=1,
                    name="Karaoke",
                    comment="Disable suppression\nof presenation audio\nby mics")
mOneG.setMechanics(iPadAdm, 5861, 5862, 5863)

"""


"""
# --------------------------------------------------------------------------------------------------------------
@signals.on(signals=["ActiveCodec", ])
def activeCodecSignalHandler(signal, params):
    dbg.print("ACTIVE CODEC SIGNAL: {} - {}".format(signal, params.get("codec")))
    if (signal == "ActiveCodec"):
        if (params.get("codec") == "zoom"):
            modePresets.call(5)
        elif (params.get("codec") == "cisco"):
            modePresets.call(4)
"""

spm_mic_S01 = SignalProbe(dev=symetrix_proxy, rcId=401, uiHost=ipad_adm, btnId=5751)
spm_mic_S02 = SignalProbe(dev=symetrix_proxy, rcId=402, uiHost=ipad_adm, btnId=5752)
spm_mic_S03 = SignalProbe(dev=symetrix_proxy, rcId=403, uiHost=ipad_adm, btnId=5753)
spm_mic_S04 = SignalProbe(dev=symetrix_proxy, rcId=404, uiHost=ipad_adm, btnId=5754)
spm_mic_S05 = SignalProbe(dev=symetrix_proxy, rcId=405, uiHost=ipad_adm, btnId=5755)
spm_mic_S06 = SignalProbe(dev=symetrix_proxy, rcId=406, uiHost=ipad_adm, btnId=5756)
spm_mic_S07 = SignalProbe(dev=symetrix_proxy, rcId=407, uiHost=ipad_adm, btnId=5757)
spm_mic_S08 = SignalProbe(dev=symetrix_proxy, rcId=408, uiHost=ipad_adm, btnId=5758)
spm_mic_H09 = SignalProbe(dev=symetrix_proxy, rcId=409, uiHost=ipad_adm, btnId=5759)
spm_mic_H10 = SignalProbe(dev=symetrix_proxy, rcId=410, uiHost=ipad_adm, btnId=5760)
spm_mic_H11 = SignalProbe(dev=symetrix_proxy, rcId=411, uiHost=ipad_adm, btnId=5761)
spm_mic_H12 = SignalProbe(dev=symetrix_proxy, rcId=412, uiHost=ipad_adm, btnId=5762)
spm_mic_H13 = SignalProbe(dev=symetrix_proxy, rcId=413, uiHost=ipad_adm, btnId=5763)
spm_mic_H14 = SignalProbe(dev=symetrix_proxy, rcId=414, uiHost=ipad_adm, btnId=5764)
spm_mic_H15 = SignalProbe(dev=symetrix_proxy, rcId=415, uiHost=ipad_adm, btnId=5765)
spm_mic_H16 = SignalProbe(dev=symetrix_proxy, rcId=416, uiHost=ipad_adm, btnId=5766)
spm_mic_H17 = SignalProbe(dev=symetrix_proxy, rcId=417, uiHost=ipad_adm, btnId=5767)
spm_mic_H18 = SignalProbe(dev=symetrix_proxy, rcId=418, uiHost=ipad_adm, btnId=5768)
spm_mic_H19 = SignalProbe(dev=symetrix_proxy, rcId=419, uiHost=ipad_adm, btnId=5769)
spm_mic_H20 = SignalProbe(dev=symetrix_proxy, rcId=420, uiHost=ipad_adm, btnId=5770)
spm_mic_H21 = SignalProbe(dev=symetrix_proxy, rcId=421, uiHost=ipad_adm, btnId=5771)
spm_mic_H22 = SignalProbe(dev=symetrix_proxy, rcId=422, uiHost=ipad_adm, btnId=5772)
spm_mic_H23 = SignalProbe(dev=symetrix_proxy, rcId=423, uiHost=ipad_adm, btnId=5773)
spm_mic_H24 = SignalProbe(dev=symetrix_proxy, rcId=422, uiHost=ipad_adm, btnId=5774)


audio_presets_control = PresetControl(symetrix_proxy)


InitModule(__name__)
