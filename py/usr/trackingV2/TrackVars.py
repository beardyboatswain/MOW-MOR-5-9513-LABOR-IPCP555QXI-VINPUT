#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --- debug control ---------------------------------------------------------------------
trackQuuppa_dbg = "no"
TrackSystem_dbg = "time"

# todo: save all data in this file to json!

x = "x_pos"
y = "y_pos"
z = "z_pos"
d = "direction"


roomDimensions = {
    412: {x: 8150, y: 11800, z: 4000},
    413: {x: 7730, y: 11800, z: 4000},
    400: {x: 7730 + 8150, y: 11800, z: 4000},
}

roomSize = (16085, 11715, 4000)
roomSizeA = (8150, 11715, 4000)
roomSizeB = (7935, 11715, 4000)

camPosition = {
    412: {1: (5317, 5268, 2600), 3: (6352, 130, 2038)},
    413: {2: (9919, 5935, 2600), 4: (15995, 8141, 2327)},
}

micHeight = 1300

xOffset = 0
yOffset = 0

# rcId - фактически привязывает канал микрофона к метке. rdId - control id для детектора сигнала на Symetrix
trTagsProperties = {
    "a4da22e61302": {"tagName": "SRT_01", "micId": 1, "micName": "S1", "presetId": 4108, "rcId": 8001, "lblMicNameId": 4251, "btnStateId": 4301, "btnModePreserId": 4351, "btnModeZoneId": 4401, "btnModeCoordsId": 4451, "btnProbeId": 4601},
    "a4da22e612c3": {"tagName": "SRT_02", "micId": 2, "micName": "S2", "presetId": 4109, "rcId": 8002, "lblMicNameId": 4252, "btnStateId": 4302, "btnModePreserId": 4352, "btnModeZoneId": 4402, "btnModeCoordsId": 4452, "btnProbeId": 4602},
    "a4da22e61301": {"tagName": "SRT_03", "micId": 3, "micName": "S3", "presetId": 4110, "rcId": 8003, "lblMicNameId": 4253, "btnStateId": 4303, "btnModePreserId": 4353, "btnModeZoneId": 4403, "btnModeCoordsId": 4453, "btnProbeId": 4603},
    "a4da22e612fa": {"tagName": "SRT_04", "micId": 4, "micName": "S4", "presetId": 4111, "rcId": 8004, "lblMicNameId": 4254, "btnStateId": 4304, "btnModePreserId": 4354, "btnModeZoneId": 4404, "btnModeCoordsId": 4454, "btnProbeId": 4604},
    "a4da22e6131a": {"tagName": "SRT_05", "micId": 5, "micName": "S5", "presetId": 4112, "rcId": 8005, "lblMicNameId": 4255, "btnStateId": 4305, "btnModePreserId": 4355, "btnModeZoneId": 4405, "btnModeCoordsId": 4455, "btnProbeId": 4605},
    "a4da22e612b4": {"tagName": "SRT_06", "micId": 6, "micName": "S6", "presetId": 4113, "rcId": 8006, "lblMicNameId": 4256, "btnStateId": 4306, "btnModePreserId": 4356, "btnModeZoneId": 4406, "btnModeCoordsId": 4456, "btnProbeId": 4606},
    "a4da22e612fc": {"tagName": "SRT_07", "micId": 7, "micName": "S7", "presetId": 4114, "rcId": 8007, "lblMicNameId": 4257, "btnStateId": 4307, "btnModePreserId": 4357, "btnModeZoneId": 4407, "btnModeCoordsId": 4457, "btnProbeId": 4607},
    "a4da22e6136b": {"tagName": "SRT_08", "micId": 8, "micName": "S8", "presetId": 4115, "rcId": 8008, "lblMicNameId": 4258, "btnStateId": 4308, "btnModePreserId": 4358, "btnModeZoneId": 4408, "btnModeCoordsId": 4458, "btnProbeId": 4608},
    "a4da22e612db": {"tagName": "SRT_09", "micId": 9, "micName": "H9", "presetId": 4116, "rcId": 8009, "lblMicNameId": 4259, "btnStateId": 4309, "btnModePreserId": 4359, "btnModeZoneId": 4409, "btnModeCoordsId": 4459, "btnProbeId": 4609},
    "a4da22e612ed": {"tagName": "SRT_10", "micId": 10, "micName": "H10", "presetId": 4117, "rcId": 8010, "lblMicNameId": 4260, "btnStateId": 4310, "btnModePreserId": 4360, "btnModeZoneId": 4410, "btnModeCoordsId": 4460, "btnProbeId": 4610},
    "a4da22e61337": {"tagName": "SRT_11", "micId": 11, "micName": "H11", "presetId": 4118, "rcId": 8011, "lblMicNameId": 4261, "btnStateId": 4311, "btnModePreserId": 4361, "btnModeZoneId": 4411, "btnModeCoordsId": 4461, "btnProbeId": 4611},
    "a4da22e6133e": {"tagName": "SRT_12", "micId": 12, "micName": "H12", "presetId": 4119, "rcId": 8012, "lblMicNameId": 4262, "btnStateId": 4312, "btnModePreserId": 4362, "btnModeZoneId": 4412, "btnModeCoordsId": 4462, "btnProbeId": 4612},
    "a4da22e61346": {"tagName": "SRT_13", "micId": 13, "micName": "H13", "presetId": 4120, "rcId": 8013, "lblMicNameId": 4263, "btnStateId": 4313, "btnModePreserId": 4363, "btnModeZoneId": 4413, "btnModeCoordsId": 4463, "btnProbeId": 4613},
    "a4da22e6132a": {"tagName": "SRT_14", "micId": 14, "micName": "H14", "presetId": 4121, "rcId": 8014, "lblMicNameId": 4264, "btnStateId": 4314, "btnModePreserId": 4364, "btnModeZoneId": 4414, "btnModeCoordsId": 4464, "btnProbeId": 4614},
    "a4da22e6133b": {"tagName": "SRT_15", "micId": 15, "micName": "H15", "presetId": 4122, "rcId": 8015, "lblMicNameId": 4265, "btnStateId": 4315, "btnModePreserId": 4365, "btnModeZoneId": 4415, "btnModeCoordsId": 4465, "btnProbeId": 4615},
    "a4da22e56d02": {"tagName": "SRT_16", "micId": 16, "micName": "H16", "presetId": 4123, "rcId": 8016, "lblMicNameId": 4266, "btnStateId": 4316, "btnModePreserId": 4366, "btnModeZoneId": 4416, "btnModeCoordsId": 4466, "btnProbeId": 4616},
    "a4da22e56d0b": {"tagName": "SRT_17", "micId": 17, "micName": "H17", "presetId": 4124, "rcId": 8017, "lblMicNameId": 4267, "btnStateId": 4317, "btnModePreserId": 4367, "btnModeZoneId": 4417, "btnModeCoordsId": 4467, "btnProbeId": 4617},
    "a4da22e56cf6": {"tagName": "SRT_18", "micId": 18, "micName": "H18", "presetId": 4125, "rcId": 8018, "lblMicNameId": 4268, "btnStateId": 4318, "btnModePreserId": 4368, "btnModeZoneId": 4418, "btnModeCoordsId": 4468, "btnProbeId": 4618},
    "a4da22e56cf0": {"tagName": "SRT_19", "micId": 19, "micName": "H19", "presetId": 4126, "rcId": 8019, "lblMicNameId": 4269, "btnStateId": 4319, "btnModePreserId": 4369, "btnModeZoneId": 4419, "btnModeCoordsId": 4469, "btnProbeId": 4619},
    "a4da22e612e7": {"tagName": "SRT_20", "micId": 20, "micName": "H20", "presetId": 4127, "rcId": 8020, "lblMicNameId": 4270, "btnStateId": 4320, "btnModePreserId": 4370, "btnModeZoneId": 4420, "btnModeCoordsId": 4470, "btnProbeId": 4620},
    "a4da22e612f5": {"tagName": "SRT_21", "micId": 21, "micName": "H21", "presetId": 4128, "rcId": 8021, "lblMicNameId": 4271, "btnStateId": 4321, "btnModePreserId": 4371, "btnModeZoneId": 4421, "btnModeCoordsId": 4471, "btnProbeId": 4621},
    "a4da22e56cee": {"tagName": "SRT_22", "micId": 22, "micName": "H22", "presetId": 4129, "rcId": 8022, "lblMicNameId": 4272, "btnStateId": 4322, "btnModePreserId": 4372, "btnModeZoneId": 4422, "btnModeCoordsId": 4472, "btnProbeId": 4622},
    "a4da22e612d7": {"tagName": "SRT_23", "micId": 23, "micName": "H23", "presetId": 4130, "rcId": 8023, "lblMicNameId": 4273, "btnStateId": 4323, "btnModePreserId": 4373, "btnModeZoneId": 4423, "btnModeCoordsId": 4473, "btnProbeId": 4623},
    "a4da22e612c9": {"tagName": "SRT_24", "micId": 24, "micName": "H24", "presetId": 4131, "rcId": 8024, "lblMicNameId": 4274, "btnStateId": 4324, "btnModePreserId": 4374, "btnModeZoneId": 4424, "btnModeCoordsId": 4474, "btnProbeId": 4624},
    # "a4da22e612ac": {"tagName": "SRT_25", "micId": 25, "micName": "S", "presetId": 4132, "rcId": 8025, "btnProbeId": 4625}
}

trZonesProperties = {
    "zLeftBackCenter": {"camID": 7, "zoneHeightOffset": 0},
    "zCenter": {"camID": 2, "zoneHeightOffset": 0},
    "zRightBackCenter": {"camID": 8, "zoneHeightOffset": 0},
    "zStage": {"camID": 5, "zoneHeightOffset": 207},
    "zRightBack": {"camID": 1, "zoneHeightOffset": 0},
    "zEntrance": {"camID": 2, "zoneHeightOffset": 0},
    "zPreStage": {"camID": 1, "zoneHeightOffset": 0},
    "zSpreaker": {"camID": 3, "zoneHeightOffset": 207},
    "zLeftBack": {"camID": 2, "zoneHeightOffset": 0},
    "zLeftForward": {"camID": 2, "zoneHeightOffset": 0},
}

trCamProperties = {
    1: {"direction": "N", "coords": (5860, 50, 2360)},
    2: {"direction": "N", "coords": (12180, 50, 2356)},
    3: {"direction": "S", "coords": (11840, 4990, 2780)},
    4: {"direction": "S", "coords": (9270, 9830, 2185)},
    5: {"direction": "S", "coords": (8760, 9830, 2185)},
    6: {"direction": "S", "coords": (5900, 4970, 2785)},
    7: {"direction": "W", "coords": (15840, 5570, 2356)},
    8: {"direction": "E", "coords": (50, 5590, 2364)}
}
