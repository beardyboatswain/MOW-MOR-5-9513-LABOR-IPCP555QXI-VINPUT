#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.utils.system_init import InitModule

from lib.codec.ciscoRoomKit import ciscoRoomKitSerial as ciscoRKS

from usr.dev.dev import cisco_main, cisco_reserv

codec_main = ciscoRKS(dev=cisco_main)
codec_reserv = ciscoRKS(dev=cisco_reserv)


InitModule(__name__)
