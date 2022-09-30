import xml.etree.ElementTree as ET
import glob
from xml.etree import ElementTree
import datetime as date
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os

today = date.date.today()
today = today.strftime("%m%d")

root = tk.Tk()
root.withdraw()

file_path = './xml_old'

xml_files_old = glob.glob(file_path + '\*.*')
xml_filename_olds = next(os.walk(file_path))[2]

xml_element_tree_old = None

#多的xml合併成一個
for file,filename in zip(xml_files_old,xml_filename_olds):
    print(file)
    data = ElementTree.parse(file).getroot()
    # print(ElementTree.tostring(data))
    data_old = ElementTree.tostring(data)
    # print(xml_result)
    data_old = str(data_old, encoding='utf-8')

    data_old = data_old.replace(u'\uFFFD', "?")
    data_old = data_old.replace(':', '_')
    data_old = data_old.replace('version="1.0"', '')
    data_old = data_old.replace(',', '')

    #     #取代
    fp = open(f'./xml_replace_old/{filename}.xml', 'w')
    fp.write(data_old)
    fp.close()