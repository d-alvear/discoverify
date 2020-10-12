import pandas as pd 
import numpy as np
from multiprocessing import Pool
import librosa
import os

def librosa_pipeline(track):

	'''Takes in a song's Spotify track id, locates its audio file, and runs
	the audio file through the librosa feature extraction process. 
	Returns the feature vector as a dict, with track id as the key'''
	
	track_id = str(track).replace("track_","").replace(".wav","")
	
	path = f'data/audio_files/track_{track_id}.wav'

	d = {}
	d['track_id'] = track_id

	#load mp3
	y, sr = librosa.load(path, mono=True, duration=30)

	#feature extraction
	spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
	d['spectral_centroid'] = np.mean(spec_cent)

	spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
	d['spectral_bandwidth'] = np.mean(spec_bw)

	rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
	d['rolloff'] = np.mean(rolloff)

	zcr = librosa.feature.zero_crossing_rate(y)
	d['zero_crossing_rate'] = np.mean(zcr)

	mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
	for i,e in zip(range(1, 21),mfcc):
			d[f'mfcc{i}'] = np.mean(e)

	chroma = ['C', 'C#', 'D','D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
	chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
	for c,p in zip(chroma,chroma_stft):
		d[c] = np.mean(p)
		
	return d


if __name__ == '__main__':
	path = 'data/audio_files'

	files = [filename for filename in os.listdir(path)]
	for i in range(0,len(files),5):
		chunk = files[i:i+5]

		with Pool(4) as pool:
			results = [pool.apply_async(librosa_pipeline, args=(track,)) for track in chunk]
			output = [p.get() for p in results]

			for o in output:
				with open('results.txt','a') as out:
					out.write(str(o) + "," + "\n")