
"""
created by @rahulreddy
"""


# multiple urls

base_url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?'


"""[Returns all expires urls]

Returns:
    [dict] -- [e.g: 'index' : 'dynamic_url']
    takes input as e.g 
    index_list  = [['BANKNIFTY','9999'],['10006','NIFTY'],['NIFTYIT','10005']]
    from constant

 TODO Make index_list as Dynamic list and pass to getAllExpires
"""
def getAllOptionURLS(index_list_items):
    all_expiries_urls = {}
    for index_data in index_list_items:
        build_url = "symbolCode=-"+index_data[1]+"&symbol="+index_data[0]+"&symbol="+index_data[0]+"&instrument=OPTIDX&date=-&segmentLink=17&segmentLink=17"
        all_expiries_urls[index_data[0]] = base_url+build_url

    return all_expiries_urls

"""[returns all the final links as list]

Returns:
    [dict BANKNIFTY_02JAN2019 : url ] -- [takes 2 inputs
    e.g
        index_list_items = index_list  = [['BANKNIFTY','9999'],['NIFTY','10006'],['NIFTYIT','10005']]
        expires_list dictonary = output of extract_exp.getAllExpiryDetails function
        ]
"""
def getFinalURLS(index_list_items,expires_list):
    all_final_links={}
    for index_data in index_list_items:
        expires = expires_list[index_data[0]]
        for exp in expires:
            build_url = "symbolCode=-"+index_data[1]+"&symbol="+index_data[0]+"&symbol="+index_data[0]+"&instrument=OPTIDX&date="+exp+"&segmentLink=17&segmentLink=17"
            all_final_links[index_data[0]+'_'+exp] = base_url+build_url
    
    return all_final_links
