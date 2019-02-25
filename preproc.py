import librosa
import numpy as np
import os
import sys
#audiopaths = ['english000.wav','english001.wav','english002.wav','english003.wav','english004.wav','spanish000.wav','spanish001.wav','spanish002.wav','spanish003.wav','spanish004.wav']
file = sys.argv[1]
feats = []

def preproc_input(audio_path):
	sr = 12000
	n_fft = 512
	n_mels = 96
	hop_length = 256
	duration = 29.12

	src, sr = librosa.load(audio_path, sr=sr)
	n_sample = src.shape[0]
	n_sample_wanted = int(duration * sr)

	if n_sample < n_sample_wanted:
		src = np.hstack((src, np.zeros((int(duration * sr) - n_sample,))))
	elif n_sample > n_sample_wanted:  
		src = src[(n_sample - n_sample_wanted) // 2:
				  (n_sample + n_sample_wanted) // 2]

	logam = librosa.logamplitude
	melgram = librosa.feature.melspectrogram
	x = logam(melgram(y=src, sr=sr, hop_length=hop_length,n_fft=n_fft, n_mels=n_mels) ** 2,ref_power=1.0)

	x = np.expand_dims(x, axis=0)
	return x
'''
for audio in audiopaths:
	mel_feat = preproc_input(audio)
	feats.append(mel_feat)
'''
if file.endswith(".wav"):
	print(file)
	mel_feat = preproc_input(file)
	feats.append(mel_feat)

feats = np.array(feats)
np.save('crnnx.npy',feats)
feats = np.swapaxes(feats,1,3)
feats = np.swapaxes(feats,1,2)
y = np.zeros(5)
y = np.append(y,np.ones(5))
print(feats.shape)


np.save('samplex.npy',feats)
np.save('sampley.npy',y)
