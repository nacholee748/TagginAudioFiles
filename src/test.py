from pathlib import Path
import eyed3
import csv
import sys
import filetype
import os

pathFile = Path('C:\\Users\\JORGE\\Music\\Vicente Garcia - Te Soñé (Lyric Video)(MP3_160K).mp3')

audiofile = eyed3.load(pathFile)

with open('loveMusic.csv', 'w', newline='') as csvFile:
    fieldsName = ['nameFile', 'tittle', 'artist', 'gender', 'path']
    writer = csv.DictWriter(csvFile, fieldnames=fieldsName)
    writer.writeheader()

    tittle = audiofile.tag.title.encode('ascii', 'ignore') if audiofile.tag.title is not None else ''
    artist = audiofile.tag.artist.encode('ascii', 'ignore') if audiofile.tag.artist is not None else ''
    gender = audiofile.tag.genre.name.encode('ascii', 'ignore') if audiofile.tag.genre is not None else ''

    writer.writerow({'nameFile':'nameFile','tittle':tittle,'artist':artist,'gender':gender,'path':str(pathFile).encode('ascii','ignore')})