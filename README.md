# SDXL-LoRA-beethoven-melspectrogram

SDXL LoRAs can produce great image results. But can they produce coherent music by generating mel spectrograms(basically image versions of songs)? That's what we're experimenting with here.

- Replicate API: https://replicate.com/georgedavila/sdxl-beethoven-spectrograms-lora
- Model: https://huggingface.co/GDavila/sdxl-beethoven-spectrograms

Trigger word: SPECTROGRAM

## Make Spectrograms

Place audio data in directory `audio_data` and run `python makeMels.py` to create spectrograms which will be placed in `mels` directory. 

## Training
Zip `mels` directory and use [sdxl-lora-customize-training](https://replicate.com/zylim0702/sdxl-lora-customize-training) for easy lora training. 


### References 

- Data sourced from https://www.chosic.com/free-music/beethoven/
- https://github.com/OmarMedhat22/Sound-Classification-Mel-Spectrogram/blob/master/mel%20spectrogram.ipynb
- https://importchris.medium.com/how-to-create-understand-mel-spectrograms-ff7634991056
- https://stackoverflow.com/questions/60365904/reconstructing-audio-from-a-melspectrogram-has-some-clipping-with-librosa
- https://librosa.org/doc/main/generated/librosa.feature.inverse.mel_to_audio.html#librosa.feature.inverse.mel_to_audio

## Results

- Prompt: "A SPECTROGRAM image", No Negative Prompt, link to example
![res1](results/res1.png)

- Prompt: "A SPECTROGRAM image", Negative Prompt: "fuzzy, lone pixels", link to example
![res2](results/res2.png)


