#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from usr.dev.dev import ipad_adm, ipad_usr

from lib.utils.system_init import InitModule

from lib.power.powerSony import LCDSonyEthernet
from lib.power.DevicePower import MultiDevicePower

from usr.dev.dev import (bravia_chat_1_interface,
                         bravia_chat_2_interface,
                         bravia_chat_3_interface,
                         bravia_chat_4_interface,
                         bravia_clmn_l1_interface,
                         bravia_clmn_l2_interface,
                         bravia_clmn_l3_interface,
                         bravia_clmn_l4_interface,
                         bravia_clmn_r1_interface,
                         bravia_clmn_r2_interface,
                         bravia_clmn_r3_interface,
                         bravia_clmn_r4_interface,
                         bravia_cart_1_interface,
                         bravia_cart_2_interface)


bravia_chat_1 = LCDSonyEthernet(bravia_chat_1_interface)
bravia_chat_2 = LCDSonyEthernet(bravia_chat_2_interface)
bravia_chat_3 = LCDSonyEthernet(bravia_chat_3_interface)
bravia_chat_4 = LCDSonyEthernet(bravia_chat_4_interface)
bravia_clmn_l1 = LCDSonyEthernet(bravia_clmn_l1_interface)
bravia_clmn_l2 = LCDSonyEthernet(bravia_clmn_l2_interface)
bravia_clmn_l3 = LCDSonyEthernet(bravia_clmn_l3_interface)
bravia_clmn_l4 = LCDSonyEthernet(bravia_clmn_l4_interface)
bravia_clmn_r1 = LCDSonyEthernet(bravia_clmn_r1_interface)
bravia_clmn_r2 = LCDSonyEthernet(bravia_clmn_r2_interface)
bravia_clmn_r3 = LCDSonyEthernet(bravia_clmn_r3_interface)
bravia_clmn_r4 = LCDSonyEthernet(bravia_clmn_r4_interface)
bravia_cart_1 = LCDSonyEthernet(bravia_cart_1_interface)
bravia_cart_2 = LCDSonyEthernet(bravia_cart_2_interface)


bravia_chat_all = MultiDevicePower()
bravia_chat_all.addDevice(bravia_chat_1,
                          bravia_chat_2,
                          bravia_chat_3,
                          bravia_chat_4)
bravia_clmn_l_all = MultiDevicePower()
bravia_clmn_l_all.addDevice(bravia_clmn_l1,
                            bravia_clmn_l2,
                            bravia_clmn_l3,
                            bravia_clmn_l4)
bravia_clmn_r_all = MultiDevicePower()
bravia_clmn_r_all.addDevice(bravia_clmn_r1,
                            bravia_clmn_r2,
                            bravia_clmn_r3,
                            bravia_clmn_r4)
bravia_cart_all = MultiDevicePower()
bravia_cart_all.addDevice(bravia_cart_1,
                          bravia_cart_2)

# todo: проверить все кнопки переключения питания на админском айпаде
bravia_chat_1.setMechanics(uiHost=ipad_adm, btnTglPowerId=931)
bravia_chat_2.setMechanics(uiHost=ipad_adm, btnTglPowerId=932)
bravia_chat_3.setMechanics(uiHost=ipad_adm, btnTglPowerId=933)
bravia_chat_4.setMechanics(uiHost=ipad_adm, btnTglPowerId=934)
bravia_clmn_l1.setMechanics(uiHost=ipad_adm, btnTglPowerId=935)
bravia_clmn_l2.setMechanics(uiHost=ipad_adm, btnTglPowerId=936)
bravia_clmn_l3.setMechanics(uiHost=ipad_adm, btnTglPowerId=937)
bravia_clmn_l4.setMechanics(uiHost=ipad_adm, btnTglPowerId=938)
bravia_clmn_r1.setMechanics(uiHost=ipad_adm, btnTglPowerId=939)
bravia_clmn_r2.setMechanics(uiHost=ipad_adm, btnTglPowerId=940)
bravia_clmn_r3.setMechanics(uiHost=ipad_adm, btnTglPowerId=941)
bravia_clmn_r4.setMechanics(uiHost=ipad_adm, btnTglPowerId=942)
bravia_cart_1.setMechanics(uiHost=ipad_adm, btnTglPowerId=943)
bravia_cart_2.setMechanics(uiHost=ipad_adm, btnTglPowerId=944)

bravia_chat_all.addPowerTglBtn(ipad_adm, 945)
bravia_chat_all.addPowerTglBtn(ipad_adm, 945)
bravia_clmn_l_all.addPowerTglBtn(ipad_usr, 946)
bravia_clmn_l_all.addPowerTglBtn(ipad_usr, 946)
bravia_clmn_r_all.addPowerTglBtn(ipad_adm, 947)
bravia_clmn_r_all.addPowerTglBtn(ipad_usr, 947)

InitModule(__name__)
