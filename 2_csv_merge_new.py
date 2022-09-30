import os
import glob
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from shutil import copyfile
import shutil

file_path_new = './csv_new'
print(file_path_new)
os.chdir(file_path_new)
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, sep='|') for f in all_filenames ])
#export to csv
combined_csv.to_csv("combined_new_csv.csv",sep='|', index=False, float_format="%.0f")
shutil.copyfile('combined_new_csv.csv', '../combined_new_csv.csv')