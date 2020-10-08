from secret import *
import re
import pandas as pd
import numpy as np
import psycopg2 as pg
from psycopg2 import Error
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import requests
from sklearn.metrics.pairwise import cosine_similarity

client_credentials_manager = SpotifyClientCredentials(client_id=spotify_credentials['client_id'],client_secret=spotify_credentials['client_secret'])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#=============================== SQL Utils ====================================#
conn = pg.connect(database=sql_credentials['database'],
                  user=sql_credentials['user'], 
                  password=sql_credentials['password'],
                  host=sql_credentials['host'])

def run_query(q,conn):
	'''a function that takes a SQL query as an argument
	and returns a pandas dataframe of that query'''
	with conn:
		try:
			cur = conn.cursor()
			cur.execute(q)
			return pd.read_sql(q, conn)

		except (Exception, pg.Error) as e:
			print(e)
			try:
				cur.close()
				cur = conn.cursor()
				cur.execute(q)
				return pd.read_sql(q, conn)

			except:
				conn.close()
				conn = pg.connect(database=sql_credentials['database'],
								  user=sql_credentials['user'], 
								  password=sql_credentials['password'],
								  host=sql_credentials['host'])
				cur = conn.cursor()
				cur.execute(q)
				return pd.read_sql(q, conn)
	cur.close()