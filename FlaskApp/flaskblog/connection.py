from sqlalchemy import create_engine
import pandas as pd


#connection with postgres
engine = create_engine('postgresql://postgres:Tippete123@localhost:5432/se4g')
#reading the tables 
codes_sql= pd.read_sql_table('codes',engine)

