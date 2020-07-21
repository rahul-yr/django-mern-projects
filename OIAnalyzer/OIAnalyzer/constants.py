
"""
created by @rahulreddy
"""


# add index parameters
# TODO needs to implement dynamic one i.e index list handling
index_list  = [['BANKNIFTY','9999'],['NIFTY','10006']]
# index_list  = [['BANKNIFTY','9999']]

# column fields to extract
column_details =['total_oi', 'change_in_oi', 'volume', 'iv', 'ltp', 'net_change', 'bid_quantity',
       'bid_price', 'ask_price', 'ask_quantity', 'strike_price','option_type','processed_timestamp']
# column fields to extract
second_column_details =['script_name', 'processed_timestamp', 'ltp']
# Set to True to fetch only 2weeks expiry data else fetch all the future
#  expires data from the time it executes
TWO_WEEK_EXPIRY_ONLY = True

