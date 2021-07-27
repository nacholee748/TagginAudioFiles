#########################
import librosa
from numpy import lib
import soundfile
import matplotlib.pyplot as plt
import numpy as np
import base64
import requests
from pathlib import Path, PureWindowsPath

# path_Music = Path('C:\\Users\\JORGE\\Music\\')
audio = Path("C:\\Users\\JORGE\\PycharmProjects\\TagginAudioFiles\\audio.mp3")
audio1 = Path("audioWma.wma")
pathFile = Path('C:\\Users\\JORGE\\Documents\\Projects\\TagginAudioFiles\\docs\\audios\\audio.mp3')

#Check it, for read audios with Librosa
#https://github.com/librosa/librosa/issues/945

p = PureWindowsPath('c:/Users/JORGE/PycharmProjects/TagginAudioFiles/docs/audios/audio.mp3')
p = PureWindowsPath('./docs/audios/wavFile.wav')

file_audio = librosa.ex(p)

signal, fs = librosa.load(path=p, sr=44100, duration=3)

signal = np.array([int(sample * 32767) for sample in signal], dtype=np.int16)
encoded = base64.b64encode(signal)
encoded = str(encoded, 'utf-8')
#########################

payload = encoded

headers = {
    'content-type': "text/plain",
    'x-rapidapi-key': "aea98de148msh11855ec8e4fc207p19f533jsn5a84cb918d30",
    'x-rapidapi-host': "shazam.p.rapidapi.com"
    }

url = "https://shazam.p.rapidapi.com/songs/detect"
response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
