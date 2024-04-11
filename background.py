#!/usr/bin/env python3

import os

import rembg

dir = 'misc'
input = input("Introduce nombre de archivo: ")
output = input + '-nobg.jpg'

ipath = os.path.join(dir, input)
opath = os.path.join(dir, output)

with open(ipath, 'rb') as ifile:
    with open(opath, 'wb') as ofile:
        image = ifile.read()
        image_nobg = rembg.remove(image)
        ofile.write(image_nobg)