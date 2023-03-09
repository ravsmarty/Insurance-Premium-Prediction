import pandas as pd
import numpy as np
import os,sys
from Insurance.exception import InsuranceException
from Insurance.config import mongo_client
from Insurance.logger import logging


def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    try:
      
       logging.info(f"reading data from database {database_name} and collection :{collection_name}")
       df =pd.DataFrame(mongo_cleint[database_name][collection_name].find())
       logging.info(f"find columns {df.columns}")
       if "_id"  in df.columns:
          logging.info(f"dropping columns _id")
          df =df.drop("_id", axis=1)  
       logging.info(f"toltal rows and columns {df.shape}")
       return df

    except Exception as e:
        raise InsuranceException(e, sys)


