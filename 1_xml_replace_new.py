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

file_path = './xml_new'

xml_files_new = glob.glob(file_path + '\*.*')
xml_filename_news = next(os.walk(file_path))[2]

xml_element_tree_new = None

#多的xml合併成一個
for file,filename in zip(xml_files_new,xml_filename_news):
    print(file)
    data = ElementTree.parse(file).getroot()
    # print(ElementTree.tostring(data))
    data_new = ElementTree.tostring(data)
    # print(xml_result)
    data_new = str(data_new, encoding='utf-8')

    data_new = data_new.replace(u'\uFFFD', "?")
    data_new = data_new.replace(':', '_')
    data_new = data_new.replace('version="1.0"', '')
    data_new = data_new.replace(',', '')

    #     #取代
    fp = open(f'./xml_replace_new/{filename}.xml', 'w')
    fp.write(data_new)
    fp.close()