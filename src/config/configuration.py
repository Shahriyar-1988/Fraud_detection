import os
from dotenv import load_dotenv
from src.utils.common import read_yaml,create_directories
from src.constants import *
from src.entity.config_entity import (DataIngestionConfig,
                                       DataTransformationConfig,
                                       TrainingConfig,
                                       ModelEvaluationConfig)

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
    def get_training_config(self)->TrainingConfig:
        config=self.config.training
        params=self.params.ExtraTree
        schema=self.schema.TARGET_COLUMN
        create_directories([config.root_directory,
                            config.model_directory,
                            config.metrics_directory])
        training_config=TrainingConfig(
            root_directory =config.root_directory,
            train_data_path=config.train_data_path,
            model_directory=config.model_directory,
            metrics_directory=config.metrics_directory,
            model_name=config.model_name,
            target_col=schema,
            param_grid=params.param_grid
          

        )
        return training_config
    
    def get_evaluation_config(self)->ModelEvaluationConfig:
        config=self.config.evaluation
        schema=self.schema.TARGET_COLUMN
        load_dotenv()
        MLFLOW_URI=os.getenv("MLFLOW_TRACKING_URI")

        test_config = ModelEvaluationConfig(
            test_data_path=config.test_data_path,
            tree_model_path=config.tree_model_path,
            knn_model_path=config.knn_model_path,
            metric_file_path=config.metric_file_path,
            target_col=schema,
            mlflow_uri=MLFLOW_URI  
        )
        return test_config
    




    


        


