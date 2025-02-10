#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib.error
import urllib.request

from extronlib.system import Timer

quuppa_ip = "10.213.142.57"
quuppa_port = 8080

resp = urllib.request.urlopen("http://{}:{}/qpe/getTagPosition?version=2".format(quuppa_ip, quuppa_port))

quuppaAnswer = resp.read()
quuppaPositions = json.loads(quuppaAnswer.decode("utf-8"))

jsonFile = open(".\\py\\quuppa\\getTagPosition.json", "w")
jsonFile.write(json.dumps(quuppaPositions, indent=2))
jsonFile.close()
