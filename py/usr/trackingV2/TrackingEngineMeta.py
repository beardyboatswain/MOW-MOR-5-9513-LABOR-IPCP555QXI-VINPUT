#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Callable
from abc import ABCMeta, abstractmethod


class TrackingEngineMeta(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.fbCallbackFunctions = list()

    @abstractmethod
    def addCallbackForUpdateTagData(self, fbCallbackFunction: Callable[[dict,], None]) -> None:
        """
        Add function for tag data feedback
        fbCallbackFunction gets param:
        tagData:dict - data for tags {str tag id: {"id": str, "name": str, "zone": str, "coords": (float, float, float)}}
        """
        pass

    @abstractmethod
    def startTracking(self) -> None:
        """
        Execute tag polling
        """
        pass

    @abstractmethod
    def stopTracking(self) -> None:
        """
        Stop tag polling
        """
        pass

    @abstractmethod
    def setTracking(self, state: bool) -> None:
        """
        Set traking on (state=True) or off (state=False)
        """
        pass
