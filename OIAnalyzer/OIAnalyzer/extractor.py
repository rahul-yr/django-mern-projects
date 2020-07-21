
"""
created by @rahulreddy
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from influxdb import DataFrameClient
from pytz import timezone
from datetime import datetime
import constants
import re

def second_table_extractor(page):
    soup_data = BeautifulSoup(page.content, 'html.parser')
    table_cls_2 = soup_data.find('table',attrs={'width':'100%'})
    req_row = table_cls_2.find_all('tr')
    td_columns_data = req_row[0].find_all('td')
    td_span = td_columns_data[1].find_all('span')
    second_table = []
  
    time_extract =str(BeautifulSoup(str(td_span[1]), 'html.parser').get_text())
    time_extract=time_extract.replace('As on ','')
    time_extract = time_extract.strip()
    datetime_object = datetime.strptime(time_extract, '%b %d, %Y %H:%M:%S IST')
    second_table.append(str(datetime_object))
    # Implement Index Extractor
    index_extractor_value =str(BeautifulSoup(str(td_span[0]), 'html.parser').get_text())
    temp = re.findall(r'\d+', index_extractor_value) 
    s = '.'
    s = s.join(temp)
    second_table.append(s)
    
    # Implemented Index Extractor    
    return second_table

def dataTypeMapper(index,td_columns):
    try:
        data = str(BeautifulSoup(str(td_columns[index]), 'html.parser').get_text()).strip()
        if(data.__eq__('-')):
            return
        else:
            return (float(data.replace(',','')))
    except:
        print("Exception occured due to invalid indexing")

def time_extractor(soup_data):
    table_cls_2 = soup_data.find('table',attrs={'width':'100%'})
    req_row = table_cls_2.find_all('tr')
    td_columns_data = req_row[0].find_all('td')
    td_span = td_columns_data[1].find_all('span')
    time_extract =str(BeautifulSoup(str(td_span[1]), 'html.parser').get_text())
    time_extract=time_extract.replace('As on ','')
    time_extract = time_extract.strip()
    datetime_object = datetime.strptime(time_extract, '%b %d, %Y %H:%M:%S IST')
    return datetime_object

def table_extractor(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    extracted_time = time_extractor(soup)
    table_cls_2 = soup.find('table',id="octable")
    req_row = table_cls_2.find_all('tr')
    
    listOfAllRecords=[]
    for row_number, tr_nos in enumerate(req_row):
        # This ensures that we use only the rows with values
        if row_number <= 1 or row_number == len(req_row)-1:
            continue
        callRecords = []
        putRecords = []
        td_columns = tr_nos.find_all('td')
        # print(len(td_columns))
        if (len(td_columns) == 23):
            for i in range(1,11):  
                callRecords.append(dataTypeMapper(i,td_columns))
            callRecords.append(dataTypeMapper(11,td_columns))
            callRecords.append("CE")
            callRecords.append(str(extracted_time))

            for i in range(21 ,15,-1):
                putRecords.append(dataTypeMapper(i,td_columns))
            for i in range(12,16):
                putRecords.append(dataTypeMapper(i,td_columns))
            putRecords.append(dataTypeMapper(11,td_columns))
            putRecords.append("PE")
            putRecords.append(str(extracted_time))

        listOfAllRecords.append(callRecords)
        listOfAllRecords.append(putRecords)

    new_df=pd.DataFrame(listOfAllRecords,columns=constants.column_details)
    
    cols = list(new_df.columns)
    cols = [cols[-1]] + cols[:-1]
    new_df = new_df[cols]

    return new_df

# new_df = table_extractor()

# new_df.to_csv('file123.csv',header=True,index=True) 


