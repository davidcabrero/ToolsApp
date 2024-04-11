#!/usr/bin/env python3

import pyqrcode

url= input("Introdue URL: ")
qr = pyqrcode.create(url)
qr.png("gsyc.png", scale=5)