import numpy as np 
import os
from keras.models import Sequential
from keras.layers.convolutional import Convolution3D, Convolution2D, Convolution1D
from keras.layers.convolutional_recurrent import ConvLSTM2D
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import ZeroPadding2D, MaxPooling1D
from keras.layers import Input, Dense, Activation
from keras.models import Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers.recurrent import GRU, LSTM
from keras import backend as K
from keras.optimizers import SGD
from keras.layers.wrappers import TimeDistributed
from keras.utils.io_utils import HDF5Matrix
from keras.preprocessing.sequence import pad_sequences
import sys
path = "D:/Mihir/prog/xampp/htdocs/project/npy/"
file = sys.argv[1]

def create_model(model_type):
	if(model_type=='timedistributedcnn_lstm'):
		seq_size=1366
		nb_features=96
		channels=1

		model = Sequential()
		model.add(TimeDistributed(Convolution1D(32,3,activation='relu'), input_shape=(seq_size,nb_features,channels)))
		model.add(TimeDistributed(Convolution1D(32,3,activation='relu')))
		model.add(TimeDistributed(MaxPooling1D(2,2)))
		model.add(Dropout(0.25))
		
		model.add(TimeDistributed(Convolution1D(64,3, activation='relu')))
		model.add(TimeDistributed(Convolution1D(64,3,activation='relu')))
		model.add(TimeDistributed(MaxPooling1D(2,2)))
		model.add(Dropout(0.25))

		model.add(TimeDistributed(Convolution1D(64,3, activation='relu')))
		model.add(TimeDistributed(Convolution1D(64,3,activation='relu')))
		model.add(TimeDistributed(MaxPooling1D(2,2)))
		model.add(Dropout(0.25))
		# model.summary()
		model.add(TimeDistributed(Flatten()))
		model.add(BatchNormalization())
		model.add(LSTM(128, return_sequences=True))
		model.add(LSTM(128, return_sequences=True))
		model.add(Dropout(0.25))
		model.add(Flatten())
		model.add(Dense(3, activation='sigmoid'))
		#model.summary()
		sgd = SGD( lr = 0.01, decay=1e-6, momentum=0.9, nesterov=True, clipnorm=0.5)
		#plt.title('model accuracy')
		model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['categorical_accuracy'])
		return model		

def testthatshit(path,file):
	model_type='timedistributedcnn_lstm'
	model=create_model(model_type=model_type)
	#model.summary()

	#print('Loading testing data...')

	#x_test=np.load(input_file)
	x_test=np.load(path+file)
	x_test=pad_sequences(x_test,maxlen=1366)
	
	#change current interation number if you want to start from a specific point
	cur_iter = 21
	model_filename = model_type + str(cur_iter)

	#Load existing weights if available
	if os.path.isfile(model_filename):
		#print('Loading weights from file')
		model.load_weights(model_filename)


	#test the network
	#print('Predicting...')
	predictions = model.predict(x_test)
	# print('Saving...')
	print(predictions)
	#print(predictions.shape)
	#np.save('predictions.npy',predictions)
	#test['probability'] = predictions
	#test.to_csv( output_file, columns = ( 't_id', 'probability' ), index = None )



testthatshit(path,file)