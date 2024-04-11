#!/usr/bin/env python3

import sounddevice
from scipy.io.wavfile import write

# File name for recording
filename = input("Introduce el nombre del archivo de audio: ")
# Tiemspan to record (seconds)
timespan = 10
# Souund samples per second
samples_second = 44100

print("Recording... ", end='')
sound = sounddevice.rec(timespan * samples_second, samplerate=samples_second, channels=2)
sounddevice.wait()
write(filename, samples_second, sound)
print(f"done, saved in {filename}.")