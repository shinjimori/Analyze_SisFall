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

	def __convert_accel(self, data_frame):
		data_frame['ax'] = data_frame['ax'] * 32.0 / 8192.0  # ax * 2 * scale / 2^resolution
		data_frame['ay'] = data_frame['ay'] * 32.0 / 8192.0
		data_frame['az'] = data_frame['az'] * 32.0 / 8192.0
		data_frame['t'] = data_frame.index * 0.005
		return data_frame

# Public
	def analyze_activities(self):
		for i, path in enumerate(self.df['path']):
			accel = self.__convert_accel(self.__load_data(path))
			#
			# Call fall detection
			#
			print(accel.head(5))
			print(accel.tail(5))


if __name__ == '__main__':
	AS = AnalyzeSisFall('C:/Dataset/SisFall_dataset/*/*.txt')
	AS.analyze_activities()