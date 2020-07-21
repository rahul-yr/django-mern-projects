
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'rajesh'
POSTGRES_DB_NAME = 'postgres'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5432'
POSTGRES_TABLE = 'option_chain'
POSTGRES_SECOND_TABLE = 'option_underlying_price'


# CREATE TABLE option_chain
# (
#   script_name text NOT NULL,
#   processed_timestamp TIMESTAMP without time zone NOT NULL,
#   total_oi bigint,
#   change_in_oi bigint,
#   volume bigint,
#   iv numeric,
#   ltp numeric,
#   net_change numeric,
#   bid_quantity bigint,
#   bid_price numeric,
#   ask_price numeric,
#   ask_quantity bigint,
#   strike_price bigint,
#   option_type text NOT NULL,
#   created_ts timestamp without time zone not null default now(),
#   primary key (script_name,processed_timestamp,option_type,strike_price))


# CREATE TABLE option_underlying_price
# (
#   script_name text NOT NULL,
#   processed_timestamp TIMESTAMP without time zone NOT NULL,
#   ltp numeric,
#   created_ts timestamp without time zone not null default now(),
#   primary key (script_name,processed_timestamp))

