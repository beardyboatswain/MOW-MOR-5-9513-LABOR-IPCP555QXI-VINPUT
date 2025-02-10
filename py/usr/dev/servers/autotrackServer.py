#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from extronlib.interface import EthernetServerInterfaceEx
from extronlib.system import ProgramLog
from extronlib.system import Timer, Wait
from extronlib import event
from time import sleep
import re
import time

from lib.utils.debugger import debuggerNet as debugger
from usr.var.debug_mode import autotrackServer_dbg
dbg = debugger(autotrackServer_dbg, __name__)


fbServer = EthernetServerInterfaceEx(44444, 'TCP')
connected = 0


def startServer():
    """Start the server.  Reattempt on failure after 1s."""
    if fbServer.StartListen() != 'Listening':   # Port unavailable
        dbg.print('Port unavailable')
        Wait(1, startServer)


@Timer(1)
def checkTimer(timer, count):
    """
    Check the time since last keepalive received from client. Reconnect if
    necessary.
    """
    global connected
    # If connected and keepalive not received in last 15 seconds,
    # disconnect and listen again.
    if connected and time.monotonic() - connected > 3600 * 24:
        fbServer.Disconnect()
        startServer()
        connected = None


@event(fbServer, 'ReceiveData')
def HandleReceiveData(interface, data):
    global connected
    dbg.print('Rx: {}'.format(data.decode()))

    rxLine = data.decode().upper()

    if (rxLine.find("CTON") > -1):
        dbg.print("Autotraking set to ON: {}".format(rxLine))
    elif (rxLine.find("CTOFF") > -1):
        dbg.print("Autotraking set to OFF: {}".format(rxLine))

    interface.Send("<OK>\n")

    # This simulates a condition where the server has determined to end the
    # session and close the connection.
    if b'end' in data:                  # Disconnect on data
        dbg.print('End signal received.')
        interface.Disconnect()
        startServer()

    # This simulates a keepalive message received from the client.  Check
    # for missed keepalives in checkTimer()
    elif b'ping' in data:               # Record last keepalive time
        connected = time.monotonic()


@event(fbServer, 'Connected')
def HandleClientConnect(interface, state):
    global connected
    dbg.print('Client connected ({}).'.format(interface.IPAddress))
    interface.Send(b'Hello.\n')
    connected = time.monotonic()        # Reset the keepalive time


@event(fbServer, 'Disconnected')
def HandleClientDisconnect(interface, state):
    global connected
    dbg.print('Server/Client disconnected.')
    connected = None                    # Clear the keepalive


startServer()
