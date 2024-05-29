import os
import matplotlib
from matplotlib.image import imread
matplotlib.use('Agg') # No pictures displayed 
import pylab
import librosa
import librosa.display
import numpy as np
import soundfile as sf

audioDataDir = "audio_data"
audioFiles = os.listdir(audioDataDir)

for i in range(len(audioFiles)):
    save_path = f'mels/mel{i}.jpg' #dont care about full names this cleaner 

    
    image_nparray = imread(save_path)

    print(image_nparray)

    librosa.feature.inverse.mel_to_audio(image_nparray)
    audio_signal = librosa.feature.inverse.mel_to_audio(
        image_nparray, sr=sample_rate, n_fft=n_fft, hop_length=hop_length, window=scipy.signal.hanning)
    print(audio_signal, audio_signal.shape)

    sf.write('test.wav', audio_signal, sample_rate)

