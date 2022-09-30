import datetime as date
import os
from io import StringIO
import lxml.etree as et
import pandas as pd
import multiprocessing as mp
import glob
import tkinter as tk
from tkinter import filedialog

path_csv_old = './xml_replace_old'
dirlist_csv_old = os.listdir(path_csv_old)

def task_csv_old(dirlist_csv_old):
    print(dirlist_csv_old)

    today = date.date.today()
    today = today.strftime("%m%d")
    now = date.datetime.now()
    now = now.strftime("%m%d_%H_%M_%S_%f")
  
    file_path = path_csv_old + '\\' + dirlist_csv_old
    doc_old = et.parse(file_path)
    xsl = et.parse('compare2.xsl')
    transform = et.XSLT(xsl)
    result_old = str(transform(doc_old))
    df_old = pd.read_csv(StringIO(result_old))

    df_old.to_csv(f'./csv_old/{dirlist_csv_old}.csv',index=False, float_format="%.2f")
    # s = range(len(dirlist_csv_old))
    # for i in s:
    #     aa_old.to_csv(f'./xml_old_csv/{i}_xml_del_out_in_to_csv_old.csv', sep='|',index=False, float_format="%.0f")
        
if __name__=='__main__':
  pool = mp.Pool()
  res_csv_old = pool.map(task_csv_old, dirlist_csv_old)




