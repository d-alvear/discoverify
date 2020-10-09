import pandas as pd 
import numpy as np
from multiprocessing import Pool
import librosa
import time

def librosa_pipeline(track_id):

	'''Takes in a song's Spotify track id, locates its audio file, and runs
	the audio file through the librosa feature extraction process. 
	Returns the feature vector as a dict, with track id as the key'''
	
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
	with Pool(4) as pool:
		sample = ['00aU27MSKcDLw7cwdoxnek', '00Ci0EXS4fNPnkTbS6wkOh', '0aeIg30ygRdW6zUCmAdgzO',
				'0cNJ3huiV99wvUN1tmQLTL', '0DW8r8w96IoIsxqqV2VNXf', '0rXrWanGm9AaXVMrG3A35S']

		# features = []
		
		start = time.time()
		res = pool.map_async(librosa_pipeline, sample)
		pool.close()
		pool.join()
		out = res.get()
		end = time.time()
		print(f"Map Async: {end-start}")

	with Pool(4) as pool:
		
		start = time.time()
		results = [pool.apply_async(librosa_pipeline, args=(track,)) for track in sample]
		output = [p.get() for p in results]
		end = time.time()
		print(f"Apply Async: {end-start}")


		# features.extend(out)