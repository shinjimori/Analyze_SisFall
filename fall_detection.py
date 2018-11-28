# -*- coding: utf-8 -*-
import glob, os
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tests.io.test_parquet import df_cross_compat

if __name__ == '__main__':
   file_list = glob.glob("C:/Dataset/SisFall_dataset/*/*.txt")
   print(len(file_list))
   df_sample = pd.read_csv('C:\Dataset\SisFall_dataset\SA01\D01_SA01_R01.txt', sep=',', names=('Ax_0', 'Ay_0', 'Az_0', 'Gx', 'Gy', 'Gz', 'Ax_1', 'Ay_1', 'Az_1'))
   print(df_sample)