#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.utils.system_init import InitModule
from extronlib import event, Version
from extronlib.device import ProcessorDevice, UIDevice
from extronlib.interface import (EthernetClientInterface,
                                 EthernetServerInterfaceEx,
                                 SerialInterface)

import lib.helpers.ConnectionHandler as ConnectionHandler
import lib.helpers.AutoEthernetConnection as AECon
import lib.helpers.AutoSerialConnection as ASCon

from lib.utils.ipcputils import IPDev

import lib.drv.gs.gs_extr_matrix_XTPIICrossPointSeries_v1_12_0_1 as xtpCP
import lib.drv.gs.gs_pana_camera_AW_HE_UE_Series_v1_6_1_1 as panasonicAWHEcam
import lib.drv.gs.gs_syme_dsp_Radius_NX_Series_v1_0_2_0 as symetrixRadius
import lib.drv.gs.tv1_vprocessor_C3_540_503_v1_3_1_0 as tvOneCorio


mIPCP = ProcessorDevice("SRB-BLG-0-33-SRBIJA-IPCP250")
ipad_adm = UIDevice("SRB-BLG-0-33-SRBIJA-IPAD-ADM")
ipad_usr = UIDevice("SRB-BLG-0-33-SRBIJA-IPAD-USR")
ipads = [ipad_adm, ipad_usr]

# --- ip addresses ----------------------------------------------------------------------
quuppa_ip = IPDev("10.213.142.57", 8080)

cam_1_ip = IPDev("10.213.142.43", 80, "admin", "12345")
cam_2_ip = IPDev("10.213.142.44", 80, "admin", "12345")
cam_3_ip = IPDev("10.213.142.45", 80, "admin", "12345")
cam_4_ip = IPDev("10.213.142.46", 80, "admin", "12345")
cam_5_ip = IPDev("10.213.142.47", 80, "admin", "12345")
cam_6_ip = IPDev("10.213.142.48", 80, "admin", "admin")
cam_7_ip = IPDev("10.213.142.49", 80, "admin", "12345")
cam_8_ip = IPDev("10.213.142.50", 80, "admin", "12345")


xtp_matrix_ip = IPDev("10.213.142.13", 23, "admin", "XXXXXXX")

# todo: уточнить криды подключения
infbt_matrix_ip = IPDev("10.213.142.52", 23, "admin", "admin")

symetrix_ip = IPDev("10.213.142.14", 48631, "", "")

# todo: уточнить криды подключения
tvone_left_ip = IPDev("10.213.142.35", 10001, "admin", "adminpw")
tvone_center_ip = IPDev("10.213.142.36", 10001, "admin", "adminpw")
tvone_right_ip = IPDev("10.213.142.37", 10001, "admin", "adminpw")

# todo: уточнить криды подключения
epiphan_ip = IPDev("10.213.142.43", 23, "admin", "password")

# todo: уточнить порты инжекции на xtp
bravia_chat_1_ip = IPDev("10.213.142.13", 4001)   # tribune
bravia_chat_2_ip = IPDev("10.213.142.13", 4002)   # door to stage
bravia_chat_3_ip = IPDev("10.213.142.13", 4003)   # door to hall
bravia_chat_4_ip = IPDev("10.213.142.13", 4004)   # window
bravia_clmn_l1_ip = IPDev("10.213.142.13", 4005)   # window
bravia_clmn_l2_ip = IPDev("10.213.142.13", 4006)   # window
bravia_clmn_l3_ip = IPDev("10.213.142.13", 4007)   # window
bravia_clmn_l4_ip = IPDev("10.213.142.13", 4008)   # window
bravia_clmn_r1_ip = IPDev("10.213.142.13", 4009)   # window
bravia_clmn_r2_ip = IPDev("10.213.142.13", 4010)   # window
bravia_clmn_r3_ip = IPDev("10.213.142.13", 4011)   # window
bravia_clmn_r4_ip = IPDev("10.213.142.13", 4012)   # window
bravia_cart_1_ip = IPDev("10.213.142.13", 4013)   # cart 1
bravia_cart_2_ip = IPDev("10.213.142.13", 4014)   # cart 2

# todo: уточнить как управляем светом
malight_ip = IPDev("10.213.142.62", 1234)

aten_pdu_1_ip = IPDev("10.213.142.64", 23, 'teladmin', 'telpassword')
aten_pdu_2_ip = IPDev("10.213.142.65", 23, 'teladmin', 'telpassword')
aten_pdu_3_ip = IPDev("10.213.142.66", 23, 'teladmin', 'telpassword')
aten_pdu_4_ip = IPDev("10.213.142.67", 23, 'teladmin', 'telpassword')
aten_pdu_5_ip = IPDev("10.213.142.68", 23, 'teladmin', 'telpassword')
aten_pdu_6_ip = IPDev("10.213.142.69", 23, 'teladmin', 'telpassword')

# --- VIDEO -----------------------------------------------------------------------------
# Extron XTP
xtp_keepalive_query_command = "ExecutiveMode"
xtp_keepalive_query_qualifier = None
xtp_interface = xtpCP.EthernetClass(Hostname=xtp_matrix_ip.ip,
                                    IPPort=xtp_matrix_ip.port,
                                    Model='XTP II CrossPoint 6400',
                                    Protocol='TCP')
xtp_interface.deviceUsername = xtp_matrix_ip.login
xtp_interface.devicePassword = xtp_matrix_ip.password
xtp_matrix = ConnectionHandler.GetConnectionHandler(Interface=xtp_interface,
                                                    keepAliveQuery=xtp_keepalive_query_command,
                                                    keepAliveQueryQualifier=xtp_keepalive_query_qualifier,
                                                    DisconnectLimit=10000,
                                                    pollFrequency=10,
                                                    connectRetryTime=1)

# Infobit iMatrix
infbt_poll_command = ""
infbt_matrix = AECon.AutoEthernetConnection(host=infbt_matrix_ip.ip,
                                            ipport=infbt_matrix_ip.port,
                                            pollstring=infbt_poll_command,
                                            pollfrequency=30)

# TvOne Corio
tvone_keepalive_query_command = "SystemStatus"
tvone_keepalive_query_qualifier = None

tvone_left_interface = tvOneCorio.EthernetClass(tvone_left_ip.ip, tvone_left_ip.port, Model="C3-503")
tvone_left_interface.deviceUsername = tvone_left_ip.login
tvone_left_interface.devicePassword = tvone_left_ip.password
tvone_left = ConnectionHandler.GetConnectionHandler(Interface=tvone_left_interface,
                                                    keepAliveQuery="SystemStatus",
                                                    keepAliveQueryQualifier=None,
                                                    DisconnectLimit=1000000,
                                                    pollFrequency=5,
                                                    connectRetryTime=1)

tvone_center_interface = tvOneCorio.EthernetClass(tvone_center_ip.ip, tvone_center_ip.port, Model="C3-503")
tvone_center_interface.deviceUsername = tvone_center_ip.login
tvone_center_interface.devicePassword = tvone_center_ip.password
tvone_center = ConnectionHandler.GetConnectionHandler(Interface=tvone_center_interface,
                                                      keepAliveQuery="SystemStatus",
                                                      keepAliveQueryQualifier=None,
                                                      DisconnectLimit=1000000,
                                                      pollFrequency=5,
                                                      connectRetryTime=1)

tvone_right_interface = tvOneCorio.EthernetClass(tvone_right_ip.ip, tvone_right_ip.port, Model="C3-503")
tvone_right_interface.deviceUsername = tvone_right_ip.login
tvone_right_interface.devicePassword = tvone_right_ip.password
tvone_right = ConnectionHandler.GetConnectionHandler(Interface=tvone_right_interface,
                                                     keepAliveQuery="SystemStatus",
                                                     keepAliveQueryQualifier=None,
                                                     DisconnectLimit=1000000,
                                                     pollFrequency=5,
                                                     connectRetryTime=1)

tvone_left.Connect()
tvone_center.Connect()
tvone_right.Connect()


# --- CAMs ------------------------------------------------------------------------------
cam1 = panasonicAWHEcam.HTTPClass(cam_1_ip.ip, cam_1_ip.port, "admin", "12345", "AW-UE40WEJ")
cam2 = panasonicAWHEcam.HTTPClass(cam_2_ip.ip, cam_1_ip.port, "admin", "12345", "AW-UE40WEJ")
cam3 = panasonicAWHEcam.HTTPClass(cam_3_ip.ip, cam_1_ip.port, "admin", "12345", "AW-UE40WEJ")
cam4 = panasonicAWHEcam.HTTPClass(cam_4_ip.ip, cam_1_ip.port, "admin", "12345", "AW-UE40WEJ")
cam5 = panasonicAWHEcam.HTTPClass(cam_5_ip.ip, cam_1_ip.port, "admin", "12345", "AW-UE40WEJ")
cam6 = panasonicAWHEcam.HTTPClass(cam_6_ip.ip, cam_1_ip.port, "admin", "12345", "AW-UE40WEJ")
cam7 = panasonicAWHEcam.HTTPClass(cam_7_ip.ip, cam_1_ip.port, "admin", "12345", "AW-UE40WEJ")
cam8 = panasonicAWHEcam.HTTPClass(cam_8_ip.ip, cam_1_ip.port, "admin", "12345", "AW-UE40WEJ")


# --- AUDIO -----------------------------------------------------------------------------
symetrixPollString = "GS2 124\x0d\x0a"
symetrix = AECon.AutoEthernetConnection(host=symetrix_ip.ip,
                                        ipport=symetrix_ip.port,
                                        pollstring=symetrixPollString,
                                        pollfrequency=20)

# --- Cisco Codecs ----------------------------------------------------------------------
cisco_main = ASCon.AutoSerialConnection(host=mIPCP, port='COM1', baud=115200)
cisco_reserv = ASCon.AutoSerialConnection(host=mIPCP, port='COM2', baud=115200)

# --- LCDs ------------------------------------------------------------------------------
bravia_chat_1_interface = AECon.AutoEthernetConnection(host=bravia_chat_1_ip.ip,
                                                       ipport=bravia_chat_1_ip.port,
                                                       pollstring="",
                                                       pollfrequency=30,
                                                       reconnect_interval=1)
bravia_chat_2_interface = AECon.AutoEthernetConnection(host=bravia_chat_2_ip.ip,
                                                       ipport=bravia_chat_2_ip.port,
                                                       pollstring="",
                                                       pollfrequency=30,
                                                       reconnect_interval=1)
bravia_chat_3_interface = AECon.AutoEthernetConnection(host=bravia_chat_3_ip.ip,
                                                       ipport=bravia_chat_3_ip.port,
                                                       pollstring="",
                                                       pollfrequency=30,
                                                       reconnect_interval=1)
bravia_chat_4_interface = AECon.AutoEthernetConnection(host=bravia_chat_4_ip.ip,
                                                       ipport=bravia_chat_4_ip.port,
                                                       pollstring="",
                                                       pollfrequency=30,
                                                       reconnect_interval=1)
bravia_clmn_l1_interface = AECon.AutoEthernetConnection(host=bravia_clmn_l1_ip.ip,
                                                        ipport=bravia_clmn_l1_ip.port,
                                                        pollstring="",
                                                        pollfrequency=30,
                                                        reconnect_interval=1)
bravia_clmn_l2_interface = AECon.AutoEthernetConnection(host=bravia_clmn_l2_ip.ip,
                                                        ipport=bravia_clmn_l2_ip.port,
                                                        pollstring="",
                                                        pollfrequency=30,
                                                        reconnect_interval=1)
bravia_clmn_l3_interface = AECon.AutoEthernetConnection(host=bravia_clmn_l3_ip.ip,
                                                        ipport=bravia_clmn_l3_ip.port,
                                                        pollstring="",
                                                        pollfrequency=30,
                                                        reconnect_interval=1)
bravia_clmn_l4_interface = AECon.AutoEthernetConnection(host=bravia_clmn_l4_ip.ip,
                                                        ipport=bravia_clmn_l4_ip.port,
                                                        pollstring="",
                                                        pollfrequency=30,
                                                        reconnect_interval=1)
bravia_clmn_r1_interface = AECon.AutoEthernetConnection(host=bravia_clmn_r1_ip.ip,
                                                        ipport=bravia_clmn_r1_ip.port,
                                                        pollstring="",
                                                        pollfrequency=30,
                                                        reconnect_interval=1)
bravia_clmn_r2_interface = AECon.AutoEthernetConnection(host=bravia_clmn_r2_ip.ip,
                                                        ipport=bravia_clmn_r2_ip.port,
                                                        pollstring="",
                                                        pollfrequency=30,
                                                        reconnect_interval=1)
bravia_clmn_r3_interface = AECon.AutoEthernetConnection(host=bravia_clmn_r3_ip.ip,
                                                        ipport=bravia_clmn_r3_ip.port,
                                                        pollstring="",
                                                        pollfrequency=30,
                                                        reconnect_interval=1)
bravia_clmn_r4_interface = AECon.AutoEthernetConnection(host=bravia_clmn_r4_ip.ip,
                                                        ipport=bravia_clmn_r4_ip.port,
                                                        pollstring="",
                                                        pollfrequency=30,
                                                        reconnect_interval=1)
bravia_cart_1_interface = AECon.AutoEthernetConnection(host=bravia_cart_1_ip.ip,
                                                       ipport=bravia_cart_1_ip.port,
                                                       pollstring="",
                                                       pollfrequency=30,
                                                       reconnect_interval=1)
bravia_cart_2_interface = AECon.AutoEthernetConnection(host=bravia_cart_2_ip.ip,
                                                       ipport=bravia_cart_2_ip.port,
                                                       pollstring="",
                                                       pollfrequency=30,
                                                       reconnect_interval=1)

# --- PDU ??? ---------------------------------------------------------------------------
aten_pdu_1_connection = AECon.AutoEthernetConnection(host=aten_pdu_1_ip.ip,
                                                     ipport=aten_pdu_1_ip.port,
                                                     login=aten_pdu_1_ip.login,
                                                     password=aten_pdu_1_ip.password,
                                                     buffer_delay=0.2)
aten_pdu_2_connection = AECon.AutoEthernetConnection(host=aten_pdu_2_ip.ip,
                                                     ipport=aten_pdu_2_ip.port,
                                                     login=aten_pdu_2_ip.login,
                                                     password=aten_pdu_2_ip.password,
                                                     buffer_delay=0.2)
aten_pdu_3_connection = AECon.AutoEthernetConnection(host=aten_pdu_3_ip.ip,
                                                     ipport=aten_pdu_3_ip.port,
                                                     login=aten_pdu_3_ip.login,
                                                     password=aten_pdu_3_ip.password,
                                                     buffer_delay=0.2)
aten_pdu_4_connection = AECon.AutoEthernetConnection(host=aten_pdu_4_ip.ip,
                                                     ipport=aten_pdu_4_ip.port,
                                                     login=aten_pdu_4_ip.login,
                                                     password=aten_pdu_4_ip.password,
                                                     buffer_delay=0.2)
aten_pdu_5_connection = AECon.AutoEthernetConnection(host=aten_pdu_5_ip.ip,
                                                     ipport=aten_pdu_5_ip.port,
                                                     login=aten_pdu_5_ip.login,
                                                     password=aten_pdu_5_ip.password,
                                                     buffer_delay=0.2)
aten_pdu_6_connection = AECon.AutoEthernetConnection(host=aten_pdu_6_ip.ip,
                                                     ipport=aten_pdu_6_ip.port,
                                                     login=aten_pdu_6_ip.login,
                                                     password=aten_pdu_6_ip.password,
                                                     buffer_delay=0.2)


InitModule(__name__)
