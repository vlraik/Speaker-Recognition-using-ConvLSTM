from pydub import AudioSegment
import numpy
import sys
audiopath = "D:/Mihir/prog/xampp/htdocs/project/Audiofiles/"
file = sys.argv[1]
if file.endswith('.mp3'):
	song = AudioSegment.from_mp3(audiopath+file)
	song.export(audiopath+file+'.wav', format='wav')
	print(file+".wav")
else:
	print(file)