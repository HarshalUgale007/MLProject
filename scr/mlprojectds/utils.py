import sys
import os
from scr.mlprojectds.exception import CustomException
from scr.mlprojectds.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()


host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")


def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established: %s", mydb)
        df=pd.read_sql_query("SELECT * FROM college.students;",mydb)
        print(df.head())
        
        return df
        
        
    except Exception as ex:
        raise CustomException(ex)