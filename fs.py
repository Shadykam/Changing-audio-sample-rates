import os
from pydub import AudioSegment
import librosa
from scipy.io import wavfile

for filename in os.listdir('train'):

    if filename.endswith('.wav'):
        print (filename)
        audio_data = filename
        x , sr = librosa.load(audio_data)
        print(type(x), type(sr))
        librosa.load(audio_data, sr=16000)
        print (filename)


