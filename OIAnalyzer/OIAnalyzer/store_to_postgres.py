
from sqlalchemy import create_engine
import postgres_conf as pgc

def store_data_to_postgres(df,table_name):
    try:
        engine = create_engine('postgresql://'+pgc.POSTGRES_USER+':'+pgc.POSTGRES_PASSWORD+'@'+pgc.POSTGRES_HOST+':'+pgc.POSTGRES_PORT+'/'+pgc.POSTGRES_DB_NAME)
        df.to_sql(table_name,engine,index=False,if_exists='append')
    except Exception as e:
        print(e)
    