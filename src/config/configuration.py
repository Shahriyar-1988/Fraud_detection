import os
from src.utils.common import read_yaml,create_directories
from src.constants import *
from src.entity.config_entity import DataIngestionConfig, DataTransformationConfig

class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH,
                 params_file_path =PARAMS_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH):
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)
        self.schema=read_yaml(schema_file_path)
        create_directories([self.config.artifacts_directory])
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_directory])
        data_ingestion_config= DataIngestionConfig(
            root_directory=config.root_directory,
            data_url=config.data_url,
            local_data_path=config.local_data_path

        ) 
        return data_ingestion_config  
    def get_data_transformation_config(self)-> DataTransformationConfig:
        config=self.config.data_transformation
        schema=self.schema.TARGET_COLUMN
        create_directories([config.root_directory])
        data_transformation_config=DataTransformationConfig(
            root_directory=config.root_directory,
            data_directory=config.data_directory,
            drop_columns=config.drop_columns,
            target_col=schema
        )
        return data_transformation_config
    




    


        


