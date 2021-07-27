from pathlib import Path
import eyed3
import csv
import sys
import filetype
import os

try:
    path_Music = Path('C:\\Users\\JORGE\\Music\\')
    #path_Music = Path('C:\\Users\\JORGE\\PycharmProjects\\TagginAudioFiles')

    pathFile = Path('C:\\Users\\JORGE\\Music\\audio.mp3')
    audiofile = eyed3.load(str(pathFile))

    eyed3.load()


except:
    print("Error: ", sys.exc_info()[0])
