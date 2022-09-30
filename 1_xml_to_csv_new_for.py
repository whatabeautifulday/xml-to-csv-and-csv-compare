from dataclasses import replace
import datetime as date
import os
from io import StringIO
import lxml.etree as et
import pandas as pd
import multiprocessing as mp

path_csv_new = './xml_new'
dirlist_csv_news = os.listdir(path_csv_new)
# dirlist_csv_new = os.listdir(path_csv_new)
# def task_csv_new(dirlist_csv_new):
#     print(dirlist_csv_new)

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
    

    # col_names = ["DOC_TEMP_ID",	"DOC_TEMP_DESC",	"TIMESTAMP",	"RELEASE_DATE",	"BUSINESS_PARTNER_ID",	"BUSINESS_PARTNER_NAME",	"EXPIRATION_DATE",	"COMMISSION_CONTRACT",	"TEMPLATE_ID",	"POLICY_ID",	"TAX_ID",	"CORR_TYPE",	"CORR_KEY",	"SOURCE_SYSTEM",	"SOURCBUSINESS_PARTNER_IDE_SYSTEM",	"CORR_REQ_CREATION_DATE",	"CORR_TYPE.1",	"CORR_KEY.1",	"BUSINESS_PARTNER",	"CC_NUM",	"CD_TITLE",	"CLIENT",	"PARTNER",	"TYPE",	"BPKIND",	"BU_GROUP",	"SOURCE",	"TITLE",	"FOUND_DAT",	"LIQUID_DAT",	"LOCATION_1",	"LOCATION_2",	"LOCATION_3",	"NAME_LAST",	"NAME1_TEXT",	"XSEXF",	"MARST",	"EMPLO",	"JOBGR",	"NATIO",	"PERSNUMBER",	"XUBNAME",	"BU_LANGU",	"BIRTHDT",	"DEATHDT",	"PERNO",	"CHILDREN",	"MEM_HOUSE",	"MC_NAME1",	"CRUSR",	"CRDAT",	"CRTIM",	"CHUSR",	"CHDAT",	"CHTIM",	"PARTNER_GUID",	"ADDRCOMM",	"TD_SWITCH",	"VALID_FROM",	"VALID_TO",	"VALID_TO.1",	"VALID_FROM.1",	"PARTNER.1",	"ADDRNUMBER",	"DATE_FROM",	"ADDRESS_GUID",	"ADDR_VALID_FROM",	"ADDR_VALID_TO",	"ADDR_MOVE_DATE",	"CITY1",	"CITY2",	"POST_CODE1",	"STREET",	"STR_SUPPL3",	"COUNTRY",	"TIME_ZONE",	"LANGU_CREA",	"VALID_FROM.2",	"VALID_TO.2",	"ARCHIVE_FLAG",	"PRINT_FLAG",	"PRINT_BATCH_FLAG",	"PIP_FLAG",	"SOURCE_SYSTEM.1",	"CD_PRINT_DATE",	"CD_VTREF",	"CD_ADRS_CODE",	"CD_CURRENCY",	"CD_ISSUE_DATE",	"CD_CBR_NUM",	"CD_SSP_PHONE",	"CD_MODE_PREMIUM",	"CD_UNDER_PAY",	"CD_OVER_PAY",	"CD_TOP_UP",	"CD_DIVIDEND",	"CD_CHK_CASH",	"CD_AGENCY_NAME1",	"CD_AGENT_PHONE1",	"CD_AGENT_NAME1",	"CD_AGENT_CODE1",	"CD_PREMIUM_UNIT",	"CD_POLICY_TYPE",	"CD_POLICY_TNAME",	"CD_INSURED_PRSN",	"CD_PLAN_NAME",	"CD_PYMNT_TIME",	"CD_MAIN_CVRG",	"CD_RIDER_CVRG",	"CD_TOTAL_SUM_UP",	"CD_COLCTR_CODE",	"CD_COLCTN_DATE",	"CD_POLCY_PHONE",	"CD_PYMNT_COUNT",	"CD_PYMNT_YEAR",	"CD_PLCY_BEGIN_DATE",	"CD_CYCLE_DATE",	"CD_LX_DAY",	"CD_DEPART_NAME",	"CD_PAYLOAN_DAY",	"CD_REPTNR_BPYT",	"CD_BP_ADDRESS",	"CD_CURRENCY_NAME",	"CD_RISK_FROM_TIME",	"CD_RISK_TO_TIME",	"CD_TIME",	"MAIL_TYPE"]
    df_new = pd.read_csv(StringIO(result_new), thousands=",")

    df_new.to_csv(f'./csv_new/{dirlist_csv_new}.csv',index=False, float_format="%.0f")


#     # s = range(len(dirlist_csv_new))
#     # for i in s:
#     #     aa_new.to_csv(f'./xml_new_csv/{i}_xml_del_out_in_to_csv_new.csv', sep='|',index=False, float_format="%.0f")
        
# # if __name__=='__main__':
# #   pool = mp.Pool()
# #   res_csv_new = pool.map(task_csv_new, dirlist_csv_new)




