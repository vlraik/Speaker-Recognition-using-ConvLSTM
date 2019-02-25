import librosa
import numpy as np
import os
from matplotlib import pyplot as plt
import sys
audiopath = "D:/Mihir/prog/xampp/htdocs/project/Audiofiles/"
plotpath="D:/Mihir/prog/xampp/htdocs/project/img/"
file = sys.argv[1]

feats=[]
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

if file.endswith(".wav"):
	#print(file)
	mel_feat = preproc_input(audiopath+file)
	feats.append(mel_feat)

feats = np.array(feats)
feats = np.swapaxes(feats,1,3)


#print(feats.shape)
np.save("D:/Mihir/prog/xampp/htdocs/project/npy/"+file,feats)


ims=feats
#ims=np.load('timedistx.npy')
ims=ims[0,:,:,0]

plt.figure(figsize=(20,20))
plt.imshow(np.transpose(ims), origin="lower", aspect="auto", cmap="jet", interpolation="none")
plt.colorbar()
#print(len(np.transpose(ims[0,:])))
timebins, freqbins = np.shape(ims)
plt.xlabel("time (s)")
plt.ylabel("frequency (hz)")
plt.xlim([0, timebins-1])
plt.ylim([0, freqbins])

'''
xlocs = np.float32(np.linspace(0, timebins-1, 5))
plt.xticks(xlocs, ["%.02f" % l for l in ((xlocs*10/timebins)+(0.5*2**10))/44100])
ylocs = np.int16(np.round(np.linspace(0, freqbins-1, 10)))
plt.yticks(ylocs, ["%.02f" % 96 for i in ylocs])
'''
plt.savefig(plotpath+file+'.png', bbox_inches="tight")
plt.clf()