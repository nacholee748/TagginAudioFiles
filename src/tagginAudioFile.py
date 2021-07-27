from pathlib import Path
import eyed3
import csv
import sys
import filetype
import os

try:
    path_Music = Path('C:\\Users\\JORGE\\Music\\')
    #path_Music = Path('C:\\Users\\JORGE\\PycharmProjects\\TagginAudioFiles')

    with open('loveMusic.csv', 'w', newline='') as csvFile:
        fieldsName = ['nameFile','tittle','artist','gender','path']
        writer = csv.DictWriter(csvFile,fieldnames=fieldsName,delimiter="|")
        writer.writeheader()

        for pathFile in path_Music.iterdir():
            print(str(pathFile))
            if os.path.isfile(pathFile):
                typeFile = filetype.guess(str(pathFile))

                nameFile = str(pathFile.name.encode('ascii', 'ignore'),'utf-8')
                path = str(str(pathFile).encode('ascii','ignore'),'utf-8')
                tittle = ''
                artist = ''
                gender = ''

                if typeFile != None:
                    if typeFile.extension == 'mp3':
                        audiofile = eyed3.load(str(pathFile))

                        if audiofile.tag is None:
                            tittle = pathFile.stem
                            artist = ''
                            gender = ''
                        else:
                            tittle = str(audiofile.tag.title.encode('ascii','ignore'),'utf-8') if audiofile.tag.title is not None else ''
                            artist = str(audiofile.tag.artist.encode('ascii','ignore'),'utf-8') if audiofile.tag.artist is not None else ''
                            gender = str(audiofile.tag.genre.name.encode('ascii','ignore'),'utf-8') if audiofile.tag.genre is not None else ''

                writer.writerow({'nameFile': nameFile, 'tittle': tittle, 'artist': artist, 'gender': gender, 'path': path})
except:
    print("Error!!: ", sys.exc_info()[0])