
import os
import pandas as pd
import librosa
import librosa.display
import glob
import matplotlib.pyplot as plt
plt.interactive(False)

#data, sampling_rate = librosa.load('audio_classify_dataset/train/Train/2022.wav')
#plt.figure(figsize=(12,4))
#librosa.display.waveplot(data, sr=sampling_rate)
#plt.show()

train_data_dir = '/audio_classify_dataset/train'
test_data_dir = 'audio_classify_dataset/test'

train = pd.read_csv(os.path.join(train_data_dir, 'train.csv'))
test = pd.read_csv(os.path.join(test_data_dir, 'test.csv'))

test['Class'] = 