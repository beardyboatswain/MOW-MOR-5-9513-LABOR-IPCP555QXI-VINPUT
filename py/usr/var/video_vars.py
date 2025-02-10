#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.video.VideoControl import VideoOutputType, VideoInputType


VIDEO_INPUTS_XTP = {0: {"in": 0,     "name": "NoInput (In0)",               "btnid": 2001, "type": VideoInputType.blank},
                    1: {"in": 1,     "name": "Cisco MAIN\nPeople",          "btnid": 2011, "type": VideoInputType.people},
                    2: {"in": 2,     "name": "Cisco MAIN\nPresentation",    "btnid": 2021, "type": VideoInputType.presentation},
                    3: {"in": 3,     "name": "Cisco RES\nPeople",           "btnid": 2031, "type": VideoInputType.people},
                    4: {"in": 4,     "name": "Cisco RES\nPresentation",     "btnid": 2041, "type": VideoInputType.presentation},
                    5: {"in": 5,     "name": "Zoom\nPeople",                "btnid": 2051, "type": VideoInputType.people},
                    6: {"in": 6,     "name": "Zoom\nPresentation",          "btnid": 2061, "type": VideoInputType.presentation},
                    7: {"in": 7,     "name": "Y.Module",                    "btnid": 2071, "type": VideoInputType.ymodule},
                    8: {"in": 8,     "name": "AppleTV",                     "btnid": 2081, "type": VideoInputType.appletv},
                    9: {"in": 9,     "name": "Epiphan\nIn1",                "btnid": 2091, "type": VideoInputType.pc},
                    10: {"in": 10,   "name": "Epiphan\nIn2",                "btnid": 2101, "type": VideoInputType.pc},
                    11: {"in": 11,   "name": "Spinetix 1",                  "btnid": 2111, "type": VideoInputType.adv},
                    12: {"in": 12,   "name": "Spinetix 2",                  "btnid": 2121, "type": VideoInputType.adv},
                    13: {"in": 13,   "name": "NUC\nIn Rack",                "btnid": 2131, "type": VideoInputType.pc},
                    14: {"in": 14,   "name": "Chat PC",                     "btnid": 2141, "type": VideoInputType.pc},
                    15: {"in": 15,   "name": "Tracking PC",                 "btnid": 2151, "type": VideoInputType.pc},
                    16: {"in": 16,   "name": "Operator\nHatchBox",          "btnid": 2161, "type": VideoInputType.wallplate},
                    17: {"in": 17,   "name": "Tribune\nMain",               "btnid": 2171, "type": VideoInputType.laptop},
                    18: {"in": 18,   "name": "Tribune\nPrompter",           "btnid": 2181, "type": VideoInputType.laptop},
                    19: {"in": 19,   "name": "VMix\nSDI 1",                 "btnid": 2191, "type": VideoInputType.sdi},
                    20: {"in": 20,   "name": "VMix\nSDI 2",                 "btnid": 2201, "type": VideoInputType.sdi},
                    21: {"in": 21,   "name": "iMtrx o1\nActCam",            "btnid": 2211, "type": VideoInputType.camera},
                    22: {"in": 22,   "name": "iMtrx o2",                    "btnid": 2221, "type": VideoInputType.hdmi},
                    23: {"in": 23,   "name": "iMtrx o3",                    "btnid": 2231, "type": VideoInputType.hdmi},
                    24: {"in": 24,   "name": "iMtrx o4",                    "btnid": 2241, "type": VideoInputType.hdmi},
                    25: {"in": 25,   "name": "Input 25",                    "btnid": 2251, "type": VideoInputType.blank},
                    26: {"in": 26,   "name": "Input 26",                    "btnid": 2261, "type": VideoInputType.blank},
                    27: {"in": 27,   "name": "Input 27",                    "btnid": 2271, "type": VideoInputType.blank},
                    28: {"in": 28,   "name": "Input 28",                    "btnid": 2281, "type": VideoInputType.blank},
                    29: {"in": 29,   "name": "Input 29",                    "btnid": 2291, "type": VideoInputType.blank},
                    30: {"in": 30,   "name": "Input 30",                    "btnid": 2301, "type": VideoInputType.blank},
                    31: {"in": 31,   "name": "Input 31",                    "btnid": 2311, "type": VideoInputType.blank},
                    32: {"in": 32,   "name": "Input 32",                    "btnid": 2321, "type": VideoInputType.blank},
                    33: {"in": 33,   "name": "Camera 1",                    "btnid": 2331, "type": VideoInputType.camera},
                    34: {"in": 34,   "name": "Camera 2",                    "btnid": 2341, "type": VideoInputType.camera},
                    35: {"in": 35,   "name": "Camera 3",                    "btnid": 2351, "type": VideoInputType.camera},
                    36: {"in": 36,   "name": "Camera 4",                    "btnid": 2361, "type": VideoInputType.camera},
                    37: {"in": 37,   "name": "Camera 5",                    "btnid": 2371, "type": VideoInputType.camera},
                    38: {"in": 38,   "name": "Camera 6",                    "btnid": 2381, "type": VideoInputType.camera},
                    39: {"in": 39,   "name": "Camera 7",                    "btnid": 2391, "type": VideoInputType.camera},
                    40: {"in": 40,   "name": "Camera 8",                    "btnid": 2401, "type": VideoInputType.camera},
                    41: {"in": 41,   "name": "Operator\nPC 1",              "btnid": 2411, "type": VideoInputType.pc},
                    42: {"in": 42,   "name": "Operator\nPC 2",              "btnid": 2421, "type": VideoInputType.pc},
                    43: {"in": 43,   "name": "VMix\nHDMI 1",                "btnid": 2431, "type": VideoInputType.hdmi},
                    44: {"in": 44,   "name": "VMix\nHDMI 2",                "btnid": 2441, "type": VideoInputType.hdmi},
                    45: {"in": 45,   "name": "HatchBox 1",                  "btnid": 2451, "type": VideoInputType.wallplate},
                    46: {"in": 46,   "name": "HatchBox 2",                  "btnid": 2461, "type": VideoInputType.wallplate},
                    47: {"in": 47,   "name": "HatchBox 3",                  "btnid": 2471, "type": VideoInputType.wallplate},
                    48: {"in": 48,   "name": "HatchBox 4",                  "btnid": 2481, "type": VideoInputType.wallplate},
                    49: {"in": 49,   "name": "HatchBox 5",                  "btnid": 2491, "type": VideoInputType.wallplate},
                    50: {"in": 50,   "name": "HatchBox 6",                  "btnid": 2501, "type": VideoInputType.wallplate},
                    51: {"in": 51,   "name": "HatchBox 7",                  "btnid": 2511, "type": VideoInputType.wallplate},
                    52: {"in": 52,   "name": "HatchBox 8",                  "btnid": 2521, "type": VideoInputType.wallplate},
                    53: {"in": 53,   "name": "Input 53",                    "btnid": 2531, "type": VideoInputType.unplugged},
                    54: {"in": 54,   "name": "Input 54",                    "btnid": 2541, "type": VideoInputType.unplugged},
                    55: {"in": 55,   "name": "Input 55",                    "btnid": 2551, "type": VideoInputType.unplugged},
                    56: {"in": 56,   "name": "Input 56",                    "btnid": 2561, "type": VideoInputType.unplugged},
                    57: {"in": 57,   "name": "Input 57",                    "btnid": 2571, "type": VideoInputType.unplugged},
                    58: {"in": 58,   "name": "Input 58",                    "btnid": 2581, "type": VideoInputType.unplugged},
                    59: {"in": 59,   "name": "Input 59",                    "btnid": 2591, "type": VideoInputType.unplugged},
                    60: {"in": 60,   "name": "Input 60",                    "btnid": 2601, "type": VideoInputType.unplugged},
                    61: {"in": 61,   "name": "Input 61",                    "btnid": 2611, "type": VideoInputType.unplugged},
                    62: {"in": 62,   "name": "Input 62",                    "btnid": 2621, "type": VideoInputType.unplugged},
                    63: {"in": 63,   "name": "Input 63",                    "btnid": 2631, "type": VideoInputType.unplugged},
                    64: {"in": 64,   "name": "Input 64",                    "btnid": 2641, "type": VideoInputType.unplugged},
                    }

VIDEO_OUTPUTS_XTP = {1:  {"out": 1,  "name": "Cisco MAIN\nCam",             "btnid": 1011, "type": VideoOutputType.display},
                     2:  {"out": 2,  "name": "Cisco MAIN\nPresentation",    "btnid": 1021, "type": VideoOutputType.display},
                     3:  {"out": 3,  "name": "Cisco RES\nCam",              "btnid": 1031, "type": VideoOutputType.display},
                     4:  {"out": 4,  "name": "Cisco RES\nPresentation",     "btnid": 1041, "type": VideoOutputType.display},
                     5:  {"out": 5,  "name": "Zoom\nCam",                   "btnid": 1051, "type": VideoOutputType.display},
                     6:  {"out": 6,  "name": "Zoom\nPresentation",          "btnid": 1061, "type": VideoOutputType.display},
                     7:  {"out": 7,  "name": "Screen\nLeft 1",              "btnid": 1071, "type": VideoOutputType.display},
                     8:  {"out": 8,  "name": "Screen\nLeft 2",              "btnid": 1081, "type": VideoOutputType.display},
                     9:  {"out": 9,  "name": "Screen\nCentral 1",           "btnid": 1091, "type": VideoOutputType.display},
                     10: {"out": 10, "name": "Screen\nCentral 2",           "btnid": 1101, "type": VideoOutputType.display},
                     11: {"out": 11, "name": "Screen\nRight 1",             "btnid": 1111, "type": VideoOutputType.display},
                     12: {"out": 12, "name": "Screen\nRight 2",             "btnid": 1121, "type": VideoOutputType.display},
                     13: {"out": 13, "name": "BMagic\nCam 1",               "btnid": 1131, "type": VideoOutputType.connector},
                     14: {"out": 14, "name": "BMagic\nCam 2",               "btnid": 1141, "type": VideoOutputType.connector},
                     15: {"out": 15, "name": "BMagic\nCam 3",               "btnid": 1151, "type": VideoOutputType.connector},
                     16: {"out": 16, "name": "BMagic\nCam 4",               "btnid": 1161, "type": VideoOutputType.connector},
                     17: {"out": 17, "name": "BMagic\nCam 5",               "btnid": 1171, "type": VideoOutputType.connector},
                     18: {"out": 18, "name": "BMagic\nCam 6",               "btnid": 1181, "type": VideoOutputType.connector},
                     19: {"out": 19, "name": "BMagic\nCam 7",               "btnid": 1191, "type": VideoOutputType.connector},
                     20: {"out": 20, "name": "BMagic\nCam 8",               "btnid": 1201, "type": VideoOutputType.connector},
                     21: {"out": 21, "name": "iMtrx i1",                    "btnid": 1211, "type": VideoOutputType.connector},
                     22: {"out": 22, "name": "iMtrx i2",                    "btnid": 1221, "type": VideoOutputType.connector},
                     23: {"out": 23, "name": "iMtrx i3",                    "btnid": 1231, "type": VideoOutputType.connector},
                     24: {"out": 24, "name": "iMtrx i4",                    "btnid": 1241, "type": VideoOutputType.connector},
                     25: {"out": 25, "name": "iMtrx i5",                    "btnid": 1251, "type": VideoOutputType.connector},
                     26: {"out": 26, "name": "iMtrx i6",                    "btnid": 1261, "type": VideoOutputType.connector},
                     27: {"out": 27, "name": "iMtrx i7",                    "btnid": 1271, "type": VideoOutputType.connector},
                     28: {"out": 28, "name": "iMtrx i8",                    "btnid": 1281, "type": VideoOutputType.connector},
                     29: {"out": 29, "name": "VMix\nHDMI 1",                "btnid": 1291, "type": VideoOutputType.connector},
                     30: {"out": 30, "name": "VMix\nHDMI 2",                "btnid": 1301, "type": VideoOutputType.connector},
                     31: {"out": 31, "name": "Output 31",                   "btnid": 1311, "type": VideoOutputType.connector},
                     32: {"out": 32, "name": "Output 32",                   "btnid": 1321, "type": VideoOutputType.connector},
                     33: {"out": 33, "name": "Output 33",                   "btnid": 1331, "type": VideoOutputType.connector},
                     34: {"out": 34, "name": "Output 34",                   "btnid": 1341, "type": VideoOutputType.connector},
                     35: {"out": 35, "name": "Output 35",                   "btnid": 1351, "type": VideoOutputType.connector},
                     36: {"out": 36, "name": "Output 36",                   "btnid": 1361, "type": VideoOutputType.connector},
                     37: {"out": 37, "name": "Chat 1",                      "btnid": 1371, "type": VideoOutputType.display},
                     38: {"out": 38, "name": "Chat 2",                      "btnid": 1381, "type": VideoOutputType.display},
                     39: {"out": 39, "name": "Chat 3",                      "btnid": 1391, "type": VideoOutputType.display},
                     40: {"out": 40, "name": "Chat 4",                      "btnid": 1401, "type": VideoOutputType.display},
                     41: {"out": 41, "name": "Column R E",                  "btnid": 1411, "type": VideoOutputType.display},
                     42: {"out": 42, "name": "Column R N",                  "btnid": 1421, "type": VideoOutputType.display},
                     43: {"out": 43, "name": "Column R W",                  "btnid": 1431, "type": VideoOutputType.display},
                     44: {"out": 44, "name": "Column R S",                  "btnid": 1441, "type": VideoOutputType.display},
                     45: {"out": 45, "name": "Column L E",                  "btnid": 1451, "type": VideoOutputType.display},
                     46: {"out": 46, "name": "Column L N",                  "btnid": 1461, "type": VideoOutputType.display},
                     47: {"out": 47, "name": "Column L W",                  "btnid": 1471, "type": VideoOutputType.display},
                     48: {"out": 48, "name": "Column L S",                  "btnid": 1481, "type": VideoOutputType.display},
                     49: {"out": 49, "name": "Oper\nDisplay 1",             "btnid": 1491, "type": VideoOutputType.display},
                     50: {"out": 50, "name": "Oper\nDisplay 2",             "btnid": 1501, "type": VideoOutputType.display},
                     51: {"out": 51, "name": "Oper\nDisplay 3",             "btnid": 1511, "type": VideoOutputType.display},
                     52: {"out": 52, "name": "Oper\nDisplay 4",             "btnid": 1521, "type": VideoOutputType.display},
                     53: {"out": 53, "name": "Output 53",                   "btnid": 1531, "type": VideoOutputType.connector},
                     54: {"out": 54, "name": "Output 54",                   "btnid": 1541, "type": VideoOutputType.connector},
                     55: {"out": 55, "name": "Output 55",                   "btnid": 1551, "type": VideoOutputType.connector},
                     56: {"out": 56, "name": "Output 56",                   "btnid": 1561, "type": VideoOutputType.connector},
                     57: {"out": 57, "name": "Output 57",                   "btnid": 1571, "type": VideoOutputType.connector},
                     58: {"out": 58, "name": "Output 58",                   "btnid": 1581, "type": VideoOutputType.connector},
                     59: {"out": 59, "name": "Output 59",                   "btnid": 1591, "type": VideoOutputType.connector},
                     60: {"out": 60, "name": "Output 60",                   "btnid": 1601, "type": VideoOutputType.connector},
                     61: {"out": 61, "name": "Audio\nDMBD 1",               "btnid": 1611, "type": VideoOutputType.audio},
                     62: {"out": 62, "name": "Audio\nDMBD 2",               "btnid": 1621, "type": VideoOutputType.audio},
                     63: {"out": 63, "name": "Audio\nDMBD 3",               "btnid": 1631, "type": VideoOutputType.audio},
                     64: {"out": 64, "name": "Audio\nDMBD 4",               "btnid": 1641, "type": VideoOutputType.audio},
                     }

VIDEO_INPUTS_INFBT = {1: {"in": 1,   "name": "Cam A",           "btnid": 2651, "type": VideoInputType.camera},
                      2: {"in": 2,   "name": "Cam B",           "btnid": 2661, "type": VideoInputType.camera},
                      3: {"in": 3,   "name": "Cam C",           "btnid": 2671, "type": VideoInputType.camera},
                      4: {"in": 4,   "name": "Cam D",           "btnid": 2681, "type": VideoInputType.camera},
                      }

VIDEO_OUTPUTS_INFBT = {1: {"out": 1,  "name": "Active Cam",     "btnid": 1651, "type": VideoOutputType.display},
                       2: {"out": 2,  "name": "XTP In22",       "btnid": 1661, "type": VideoOutputType.display},
                       3: {"out": 3,  "name": "XTP In23",       "btnid": 1671, "type": VideoOutputType.display},
                       4: {"out": 4,  "name": "XTP In24",       "btnid": 1681, "type": VideoOutputType.display},
                       }

# todo: перенести связанные выходы в отдельный механизм???
LINK_CODEC_CAM = {"main": 1, "slave": [3, 5], "ins": [0, 21, 22, 23, 24, 33, 34, 35, 36, 37, 38, 39, 40]}
LINK_CODEC_PRES = {"main": 7, "slave": [9, 11], "ins": [0, 16, 17, 18, 41, 42, 45, 46, 47, 48, 49, 50, 51, 52]}
LINK_LED_MAIN_L_SCREEN = {"main": 9, "slave": [11], "ins": None}
LINK_LED_MAIN_R_SCREEN = {"main": 10, "slave": [7], "ins": None}
LINK_CHAT_SCREEN = {"main": 37, "slave": [38, 39, 40], "ins": None}
LINK_DUPLICATE_SCREEN_A = {"main": 41, "slave": [43, 45, 47], "ins": None}
LINK_DUPLICATE_SCREEN_B = {"main": 42, "slave": [44, 46, 48], "ins": None}

# todo: как быть со связанными линиями де-эмбеддера в режиме кино???
LINK_INPUT_DEEMBD = {"main": 7, "slave": [61], "ins": [0, 16, 17, 18, 41, 42, 45, 46, 47, 48, 49, 50, 51, 52]}
