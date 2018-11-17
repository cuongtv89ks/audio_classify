
import os
import pandas as pd
import librosa
import librosa.display
import glob
import matplotlib.pyplot as plt

data, sampling_rate = librosa.load('audio_classify_dataset/train/Train/2022.wav')

plt.figure(figsize=(12,4))

librosa.display.waveplot(data, sr=sampling_rate)


