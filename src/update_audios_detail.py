from pathlib import Path
import eyed3
import csv
import sys
import filetype
import os


try:
    # path_Music = Path('C:\\Users\\JORGE\\Music\\')
    path_Music = Path('C:\\Users\\JORGE\\PycharmProjects\\TagginAudioFiles')
    pathFile = Path('C:\\Users\\JORGE\\PycharmProjects\\TagginAudioFiles\\audio.mp3')

    for pathFile in path_Music.iterdir():
        typeFile = filetype.guess(str(pathFile))
        # print(str(pathFile))
        if os.path.isfile(pathFile):
            if typeFile != None:
                if typeFile.extension == 'mp3':
                    type(pathFile)
                    print(str(pathFile))

except:
    print("Error!!: ", sys.exc_info()[0])
