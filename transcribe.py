#!/usr/bin/env python3

import os

import whisper

model = whisper.load_model('tiny')
archivo = input("Introduce nombre de archivo: ")
transcription = model.transcribe(os.path.join('misc', archivo))
print(transcription['text'])