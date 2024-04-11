#!/usr/bin/env python3

from zipfile import ZipFile
archivo = input("Introduce el nombre del archivo zip sin extensión: ")+".zip"
with ZipFile(archivo) as zipfile:
    # List files in zipfile
    files_in_zipfile = zipfile.namelist()
    print(files_in_zipfile)
    # Extract files in zipfile
    zipfile.extractall()
