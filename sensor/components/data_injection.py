
import pandas as pd 
import numpy as np
import os
from sensor.entity import config_entity
from sklearn.model_selection import train_test_split



class DataInjection:

    def __init__(self,data_injection_cofig:config_entity.DataInjectionConfig) :
        self.data_injection_cofig = config_entity.DataInjectionConfig

    def initiate_data_injection(self,data_injection_config=config_entity.DataInjectionConfig):

        df = pd.DataFrame("aps_failure_training_set1 (1).csv")
        df.replace(to_replace="na",value=np.NAN,inplace=True)
        feature_store_dir = os.path.dirname(self.data_injection_cofig.feature_store_path)
        os.makedirs(feature_store_dir,exist_ok = True)
        df.to_csv(feature_store_dir,index=False,header=True)

        train_df,test_df = train_test_split(df,test_size=self.data_injection_cofig.test_size,random_state=42)

        os.makedirs(self.data_injection_cofig.train_file_path,exist_ok=True)
        os.makedirs(self.data_injection_cofig.test_file_path,exist_ok=True)

        train_df.to_csv(self.data_injection_cofig.train_file_path)
        test_df.to_csv(self.data_injection_cofig.test_file_path)
