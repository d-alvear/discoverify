 CREATE TABLE IF NOT EXISTS metadata (
        track_id VARCHAR(22) PRIMARY KEY,
        track_name TEXT NOT NULL,
        artist TEXT NOT NULL,
        artist_id VARCHAR(22) NOT NULL,
        genre_1 TEXT NOT NULL,
        genre_2 TEXT,
        genre_3 TEXT
        );
		
CREATE TABLE IF NOT EXISTS spotify_features (
        id VARCHAR(22) PRIMARY KEY,
        danceability NUMERIC,
        energy NUMERIC,
        loudness NUMERIC,
        speechiness NUMERIC,
        acousticness NUMERIC,
        instrumentalness NUMERIC,
        liveness NUMERIC,
        valence NUMERIC,
        tempo NUMERIC,
        
        FOREIGN KEY (id) REFERENCES metadata (track_id)
        );
		
 CREATE TABLE IF NOT EXISTS librosa_features (
        track_id VARCHAR(22) PRIMARY KEY,
        spectral_centroid NUMERIC,
        spectral_bandwidth NUMERIC,
        rolloff NUMERIC,
        zero_crossing_rate NUMERIC,
        mfcc1 NUMERIC,
        mfcc2 NUMERIC,
        mfcc3 NUMERIC,
        mfcc4 NUMERIC,
        mfcc5 NUMERIC,
        mfcc6 NUMERIC,
        mfcc7 NUMERIC,
        mfcc8 NUMERIC,
        mfcc9 NUMERIC,
        mfcc10 NUMERIC,
        mfcc11 NUMERIC,
        mfcc12 NUMERIC,
        mfcc13 NUMERIC,
        mfcc14 NUMERIC,
        mfcc15 NUMERIC,
        mfcc16 NUMERIC,
        mfcc17 NUMERIC,
        mfcc18 NUMERIC,
        mfcc19 NUMERIC,
        mfcc20 NUMERIC,
        C NUMERIC,
        "C#" NUMERIC,
        D NUMERIC,
        "D#" NUMERIC,
        E NUMERIC,
        F NUMERIC,
        "F#" NUMERIC,
        G NUMERIC,
        "G#" NUMERIC,
        A NUMERIC,
        "A#" NUMERIC,
        B NUMERIC,

        FOREIGN KEY (track_id) REFERENCES metadata (track_id)
        );