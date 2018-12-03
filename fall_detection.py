# -*- coding: utf-8 -*-
import glob
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tests.io.test_parquet import df_cross_compat


class AnalyzeSisFall:

	file_path = ""
	activity_list = []

	def __init__(self, path, window):
		self.path = path
		self.window = window
		self.file_path = glob.glob(self.path)
		self.__generate_activity_label_from_path()
		self.df_activity = self.__create_activity_dataframe()

	@staticmethod
	def __create_acceleration_dataframe(file_path):
		df_accel = pd.read_csv(file_path, usecols=[1, 2, 3], names={'ax':[1], 'ay':[2], 'az':[3]})
		return df_accel

	@staticmethod
	def __convert_to_accel(df):
		df['ax'] = df['ax'] * 32.0 / 8192.0  # ax * 2 * scale / 2^resolution
		df['ay'] = df['ay'] * 32.0 / 8192.0
		df['az'] = df['az'] * 32.0 / 8192.0
		df['t'] = df.index * 0.005
		return df

# Private

	def __generate_activity_label_from_path(self):
		for i, v in enumerate(self.file_path):
			label, ext = os.path.splitext(os.path.basename(v))
			activity, subject, trial = label.split("_")
			self.activity_list.append([v, activity, subject, trial])

	def __create_activity_dataframe(self):
		df_activity = pd.DataFrame(self.activity_list, columns={'path':[1], 'activity':[2], 'subject':[3], 'trial':[4]})
		return df_activity

	def __sliding_window(self, df, i):
			return df['ax'][i:i+self.window], df['ay'][i:i+self.window], df['az'][i:i+self.window]

	def __generate_c8_feature(self, df):
		max_c8 = 0
		for i, v in enumerate(df['ax']):
			if i < len(df['ax']) - self.window:
				axk, ayk, azk = self.__sliding_window(df, i)
				c8 = np.sqrt(np.var(axk) + np.var(azk))
				if c8 > max_c8:
					max_c8 = c8
		return max_c8

	def __generate_c9_feature(self, df):
		max_c9 = 0
		for i, v in enumerate(df['ax']):
			if i < len(df['ax']) - self.window:
				axk, ayk, azk = self.__sliding_window(df, i)
				c9 = np.sqrt(np.var(axk) +np.var(ayk) + np.var(azk))
				if c9 > max_c9:
					max_c9 = c9
		return max_c9

# Public
	def analyze_activities(self):
		f = open('C:/Dataset/RESULT/C8_result.txt', 'a', encoding='utf-8')
		for i, path in enumerate(self.df_activity['path']):
			# C8 is calculated from raw AD, so convert}_accel should not be used.
			# accel = self.__convert_accel(self.__load_data(path))
			accel = self.__create_acceleration_dataframe(path)
			c8 = self.__generate_c8_feature(accel)
			output = self.df_activity['activity'][i] + ',' + self.df_activity['subject'][i] + ',' + self.df_activity['trial'][i] + ',' + str(c8) + '\n'
			f.write(output)
		f.close()


if __name__ == '__main__':
	AS = AnalyzeSisFall('C:/Dataset/SisFall_dataset/*/*.txt', 200)
	AS.analyze_activities()
