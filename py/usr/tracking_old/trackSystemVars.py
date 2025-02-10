#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# todo: sent all data in this file to json!

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


trackTagsProperties = {
    "a4da22e61302": {"tagName": "SRT_01", "micID": 1, "presetID": 901},
    "a4da22e612c3": {"tagName": "SRT_02", "micID": 2, "presetID": 902},
    "a4da22e61301": {"tagName": "SRT_03", "micID": 3, "presetID": 903},
    "a4da22e612fa": {"tagName": "SRT_04", "micID": 4, "presetID": 904},
    "a4da22e6131a": {"tagName": "SRT_05", "micID": 5, "presetID": 905},
    "a4da22e612b4": {"tagName": "SRT_06", "micID": 6, "presetID": 906},
    "a4da22e612fc": {"tagName": "SRT_07", "micID": 7, "presetID": 907},
    "a4da22e6136b": {"tagName": "SRT_08", "micID": 8, "presetID": 908},
    "a4da22e612db": {"tagName": "SRT_09", "micID": 9, "presetID": 909},
    "a4da22e612ed": {"tagName": "SRT_10", "micID": 10, "presetID": 910},
    "a4da22e61337": {"tagName": "SRT_11", "micID": 11, "presetID": 911},
    "a4da22e6133e": {"tagName": "SRT_12", "micID": 12, "presetID": 912},
    "a4da22e61346": {"tagName": "SRT_13", "micID": 13, "presetID": 913},
    "a4da22e6132a": {"tagName": "SRT_14", "micID": 14, "presetID": 914},
    "a4da22e6133b": {"tagName": "SRT_15", "micID": 15, "presetID": 915},
    "a4da22e56d02": {"tagName": "SRT_16", "micID": 16, "presetID": 916},
    "a4da22e56d0b": {"tagName": "SRT_17", "micID": 17, "presetID": 917},
    "a4da22e56cf6": {"tagName": "SRT_18", "micID": 18, "presetID": 918},
    "a4da22e56cf0": {"tagName": "SRT_19", "micID": 19, "presetID": 919},
    "a4da22e612e7": {"tagName": "SRT_20", "micID": 20, "presetID": 920},
    "a4da22e612f5": {"tagName": "SRT_21", "micID": 21, "presetID": 921},
    "a4da22e56cee": {"tagName": "SRT_22", "micID": 22, "presetID": 922},
    "a4da22e612d7": {"tagName": "SRT_23", "micID": 23, "presetID": 923},
    "a4da22e612c9": {"tagName": "SRT_24", "micID": 24, "presetID": 924},
    "a4da22e612ac": {"tagName": "SRT_25", "micID": 25, "presetID": 925}
}

trackZonesProperties = {
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

trackCamProperties = {
    1: {"direction": "N", "coords": (5860, 50, 2360)},
    2: {"direction": "N", "coords": (12180, 50, 2356)},
    3: {"direction": "S", "coords": (11840, 4990, 2780)},
    4: {"direction": "S", "coords": (9270, 9830, 2185)},
    5: {"direction": "S", "coords": (8760, 9830, 2185)},
    6: {"direction": "S", "coords": (5900, 4970, 2785)},
    7: {"direction": "W", "coords": (15840, 5570, 2356)},
    8: {"direction": "E", "coords": (50, 5590, 2364)}
}
