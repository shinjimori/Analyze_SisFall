# -*- coding: utf-8 -*-
import glob, os
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tests.io.test_parquet import df_cross_compat


class AnalyzeSisFall:

	file_list = ""
	activity_list = []

	def __init__(self, path):
		self.path = path
		self.file_list = glob.glob(self.path)
		self.__create_activity_list()
		self.df = self.__convert_list_to_dataframe()

# Private

	def __load_data(self, file_name):
		df = pd.read_csv(file_name, usecols=[1, 2, 3], names={'ax':[1], 'ay':[2], 'az':[3]})
		return df

	def __create_activity_list(self):
		for i, v in enumerate(self.file_list):
			label, ext = os.path.splitext(os.path.basename(v))
			activity, subject, trial = label.split("_")
			self.activity_list.append([v, activity, subject, trial])

	def __convert_list_to_dataframe(self):
		df = pd.DataFrame(self.activity_list, columns={'path':[1], 'subject':[2], 'activity':[3], 'trial':[4]})
		return df

	def __convert_accel(self, df):
		df['ax'] = df['ax'] * 32.0 / 8192.0  # ax * 2 * scale / 2^resolution
		df['ay'] = df['ay'] * 32.0 / 8192.0
		df['az'] = df['az'] * 32.0 / 8192.0
		df['t'] = df.index * 0.005
		return df

	def __sliding_window(self, df, i, window_size):
			return df['ax'][i:i+window_size], df['ay'][i:i+window_size], df['az'][i:i+window_size]

	def __generate_feature_c8(self, df):
		max = 0
		for i, v in enumerate(df['ax']):
			if i < len(df['ax']) - 200:
				axk, ayk, azk = self.__sliding_window(df, i, 200)
				c8 = np.sqrt(np.square(np.std(axk)) + np.square(np.std(azk)))
				if( c8 > max):
					max = c8
		return max

# Public
	def analyze_activities(self):
		for i, path in enumerate(self.df['path']):
			accel = self.__convert_accel(self.__load_data(path))
			c8 = self.__generate_feature_c8(accel)
			#if(c8 >= 100):
			print(path, c8)



if __name__ == '__main__':
	AS = AnalyzeSisFall('C:/Dataset/SisFall_dataset/*/*.txt')
	AS.analyze_activities()