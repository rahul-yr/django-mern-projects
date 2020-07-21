
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
from requests_futures.sessions import FuturesSession
import extract_exp
import build_urls
import constants
import header_generator
import extractor
import postgres_conf as pgc
import store_to_postgres

start = time.time()

# TODO needs to implement dynamic one i.e index list handling
def extract_and_save_to_postgres(index_details_list):
    k = extract_exp.getAllExpiryDetails(build_urls.getAllOptionURLS(index_details_list))
    
    links = build_urls.getFinalURLS(index_details_list,k)
    records = 0

    with FuturesSession() as session:
        futures = [session.get(links[i],headers = header_generator.getHeaderAttributes()) for i in links]
        for future in futures:
            resp = future.result()
            if str(resp.status_code).strip() == '200':
                df = extractor.table_extractor(resp)
                second_table_list = extractor.second_table_extractor(resp)
                
                for key in links:
                    if(links[key] == str(resp.url).strip()):
                        records += df.shape[0]
                        
                        df['script_name'] = str(key)
                        cols = list(df.columns)
                        cols = [cols[-1]] + cols[:-1]
                        df = df[cols]
                        # df.to_csv('details1.csv',mode='a',header=True,index=False) 
                        store_to_postgres.store_data_to_postgres(df,pgc.POSTGRES_TABLE)

                        # Second Table Configure 
                        second_table_list.insert(0,key)
                        second_table_list=[second_table_list]
                        second_df = pd.DataFrame(second_table_list,columns=constants.second_column_details)
                        store_to_postgres.store_data_to_postgres(second_df,pgc.POSTGRES_SECOND_TABLE)
                        break
            else : 
                print('response code from the websites : '+str(resp.status_code))

        print('Scrapped {} websites with more than {} fields'.format(len(links),records*22))
