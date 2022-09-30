from dataclasses import replace
import datetime as date
import os
from io import StringIO
import lxml.etree as et
import pandas as pd
import multiprocessing as mp

path_csv_new = './xml_new'
dirlist_csv_news = os.listdir(path_csv_new)


for dirlist_csv_new in dirlist_csv_news:
    print(dirlist_csv_new)
    today = date.date.today()
    today = today.strftime("%m%d")
    now = date.datetime.now()
    now = now.strftime("%m%d_%H_%M_%S_%f")
  
    file_path = path_csv_new + '\\' + dirlist_csv_new
    
    doc_new = et.parse(file_path)
    
    xsl = et.parse('compare.xsl')
    transform = et.XSLT(xsl)
    result_new = str(transform(doc_new))
    print(type(result_new))
    

    df_new = pd.read_csv(StringIO(result_new), thousands=",")

    df_new.to_csv(f'./csv_new/{dirlist_csv_new}.csv',index=False, float_format="%.0f")


#     # s = range(len(dirlist_csv_new))
#     # for i in s:
#     #     aa_new.to_csv(f'./xml_new_csv/{i}_xml_del_out_in_to_csv_new.csv', sep='|',index=False, float_format="%.0f")
        
# # if __name__=='__main__':
# #   pool = mp.Pool()
# #   res_csv_new = pool.map(task_csv_new, dirlist_csv_new)




