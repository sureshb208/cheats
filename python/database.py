#Python Connector:
!pip show snowflake-connector-python

from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
from pydash.arrays import chunk
import snowflake.connector as sc
import pandas as pd
from your_credentials import sf_pwd #can import os environment as well

# SNOWFLAKE

################### Connect to Snowflake DB #################
conn = sc.connect(
    account = 'server', # abc.us-east-1
    user="username",
    password=sf_pwd,
    role="rolename",
    warehouse="warehouse",
    database="database",
    schema="program"
)

cur = conn.cursor()

# Read table from snowflake
cur.execute(''' SELECT * FROM database.schema.table1 ''')
shp = pd.DataFrame.from_records(iter(cur), columns=[x[0] for x in cur.description]).drop_duplicates()
    
################### Creating engine to push to snowflake ##############
# Fill in your SFlake details here

engine = create_engine(URL(
    account = 'server', # abc.us-east-1
    user="username",
    password=sf_pwd,
    role="rolename",
    warehouse="warehouse",
    database="database",
    schema="program"
))

df.to_sql(target_table, con=engine, index=False,if_exists='append')

'''
if_exists='append' = appends if table exists
if_exists='replace' = replaces the table 
For more refer https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
''''

# ORACLE

_myram_dev = create_engine('oracle://%s:%s@%s' % (__myram_dev_user,__myram_dev_pwd, __myram_dsn),arraysize = 100)

q = '''SELECT * FROM database.schema.table1 '''

response = _myram_dev.execute(q)
cols = _myram_dev.execute(q).keys() # Get default columns
df_oracle = response.fetchall()
df_oracle = pd.DataFrame(np.array(df_oracle),columns=cols)

# TERADATA

_td_engine = create_engine('teradata://%s:%s@%s' % (__user, __pwd, __td_host))

tera_query = "SELECT * FROM database.schema.table1"

# connected_assets_all = pd.read_sql(connected_assets_all_sql, td_engine)
resp = _td_engine.execute(connected_assets_all_sql)
connected_assets_all = resp.fetchall()
connected_assets_all = pd.DataFrame(np.array(connected_assets_all),
                                  columns=[#define your own custom columns here])
