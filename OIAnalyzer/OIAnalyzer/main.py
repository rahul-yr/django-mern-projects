
"""
created by @rahulreddy
"""
import constants
import extract_data
import pytz
from datetime import datetime
import time


def main():
    ist = pytz.timezone('Asia/Calcutta')
    current_time =datetime.now(ist)
    now = current_time.strftime('%H%M')
    if '0900' <= now <= '1600':
        extract_data.extract_and_save_to_postgres(constants.index_list)
    #extract_data.extract_and_save_to_postgres(constants.index_list)
    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    time_taken = end - start
    print('In {} seconds '.format(time_taken))
