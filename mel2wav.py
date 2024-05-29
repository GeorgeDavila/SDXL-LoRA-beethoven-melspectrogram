import os
import matplotlib
from matplotlib.image import imread
matplotlib.use('Agg') # No pictures displayed 
import pylab
import librosa
import librosa.display
import numpy as np

audioDataDir = "audio_data"
audioFiles = os.listdir(audioDataDir)

for i in range(len(audioFiles)):
    save_path = f'mels/mel{i}.jpg' #dont care about full names this cleaner 

    
    image_nparray = imread(save_path)

    print(image_nparray)

    