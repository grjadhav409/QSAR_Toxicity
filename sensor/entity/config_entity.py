import os
import sys
import datetime

DATABAASE_NAME = "aps"
COLLECTION_NAME = "sensor"
TEST_SIZE = 0.2
FEATURE_FILE_NAME = "sensor.csv"
SPLIT_FILE_NAME = "train_test_split"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"


class TrainingPipelineConfig:

    def __init__(self):

            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%d%m%Y__%H%M%S')}")

class DataInjectionConfig:

    def __init__(self, training_pipeline_config:TrainingPipelineConfig):

        self.database_name = DATABAASE_NAME
        self.collection_name = COLLECTION_NAME
        self.data_injection_directory = os.path.join(training_pipeline_config.artifact_dir,"data_injection")
        self.feature_store_path = os.path.join(self.data_injection_directory,"feature",FEATURE_FILE_NAME)
        self.train_file_path = os.path.join(self.data_injection_directory,SPLIT_FILE_NAME,TRAIN_FILE_NAME)
        self.test_file_path = os.path.join(self.data_injection_directory,SPLIT_FILE_NAME,TEST_FILE_NAME)
        self.test_size = TEST_SIZE
 
