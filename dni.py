#!/usr/bin/env python3

dni=input("Introduzca el número del DNI:")
dni_number=int(dni[0:-1])
table='TRWAGMYFPDXBNJZSQVHLCKE'
letter = table[dni_number%23]
if letter == dni[-1]:
    print("Correct")
else:
    print("Not correct")
