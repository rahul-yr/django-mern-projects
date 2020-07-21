
"""
created by @rahulreddy
"""

import requests
from bs4 import BeautifulSoup
import header_generator
from build_urls import getAllOptionURLS
import constants
import request_url
from datetime import datetime,timedelta
import pytz

"""[returns all expiry details]
    takes 2 input  index_urls = {index1:url1 , index2:url2}
    input function : getAllOptionURLS from build_urls.py

Returns:
    [dictionay items] -- [e.g : 'INDEX' : ['27XXXXX',']]
"""
def getAllExpiryDetails(index_urls,request_headers = header_generator.getHeaderAttributes()):
    all_expiries_details = {}
    for key in index_urls:
        page = requests.get(index_urls[key],headers=request_headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        select_class = soup.find('select',attrs={'id' :'date','class':'goodTextBox'})
        req_row = select_class.find_all('option')
        expires = []
        for row_number, tr_nos in enumerate(req_row):
            if row_number == 0:
                continue
            data = str(BeautifulSoup(str(tr_nos), 'html.parser').get_text()).strip()
            # Filter Two Week Expireys Only
            if constants.TWO_WEEK_EXPIRY_ONLY == True:
                expiry_date = datetime.strptime(data.strip(), '%d%b%Y').date()
                ist = pytz.timezone('Asia/Calcutta')
                currentdate =datetime.now(ist).date()
                if ((expiry_date-currentdate) <= timedelta(days=14)) :
                    expires.append(data)
            else:
                expiry_date = datetime.strptime(data.strip(), '%d%b%Y').date()
                ist = pytz.timezone('Asia/Calcutta')
                currentdate =datetime.now(ist).date()
                if (currentdate <= expiry_date) :
                    expires.append(data)
        if len(expires) > 0:
            all_expiries_details[key] = expires
    return all_expiries_details

