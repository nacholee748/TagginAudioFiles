# import requests
# import base64
# from pydub import AudioSegment

# audio_mp3 = AudioSegment.from_mp3(audio)
# audio_mp3.export("audio.wav",format="wav")

#Convert to BASE64
# with open(audio, 'rb') as fileObj:
#     image_data = fileObj.read()
#     payload = base64.b64encode(image_data)



# payload = str(payload[0:400000],'utf-8')
# payload = audio_base64

# GlobalToBase64()
# response = GlobalToFile_2(payload,"./audio_short.mp3")


#########################
import librosa
import soundfile
# import matplotlib.pyplot as plt
import numpy as np
import base64
import requests

audio = "./audio.mp3"

signal, fs = librosa.load(audio, sr=44100, duration=3)


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
