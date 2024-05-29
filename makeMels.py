import os
import matplotlib
matplotlib.use('Agg') # No pictures displayed 
import pylab
import librosa
import librosa.display
import numpy as np

audioDataDir = "audio_data"
audioFiles = os.listdir(audioDataDir)

for i in range(len(audioFiles)):
    sig, fs = librosa.load(f"{audioDataDir}/{audioFiles[i]}")   
    # make pictures name 
    save_path = f'mels/mel{i}.jpg' #dont care about full names this cleaner 

    pylab.axis('off') # no axis
    pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
    S = librosa.feature.melspectrogram(y=sig, sr=fs)
    fig = librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
    pylab.close()

    print(np.array(S))