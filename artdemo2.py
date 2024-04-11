#!/usr/bin/env python3

import os

import asciipixels
imagen = input("Introduce nombres de archivo: ")
text = asciipixels.image.asciify(os.path.join('misc', imagen), definition=100)
print(text)
