import os
import glob
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from shutil import copyfile
import shutil

file_path_old = './csv_old'
print(file_path_old)
os.chdir(file_path_old)
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, sep='|') for f in all_filenames ])
#export to csv
combined_csv.to_csv("combined_old_csv.csv",sep='|', index=False, float_format="%.0f")
shutil.copyfile('combined_old_csv.csv', '../combined_old_csv.csv')