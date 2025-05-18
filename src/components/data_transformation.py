# Activate only when testing this code individually
# import sys
# import os

# # ✅ Fix path so that 'src' can be imported properly
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


import pandas as pd
import os
from sklearn.model_selection import train_test_split
from src import logger
from src.entity.config_entity import DataTransformationConfig
from src.config.configuration import ConfigurationManager
from src.utils.common import read_yaml
from sklearn.base import BaseEstimator, TransformerMixin
from src.constants import *

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config
        self.schema = read_yaml(SCHEMA_FILE_PATH)
    def data_transformer(self):
        data=pd.read_csv(self.config.data_directory)
        data.columns=[col.strip().lower().replace(" ","_") for col in data.columns]
        data=data.drop(self.config.drop_columns,axis=1)
        return data
    def train_test_splitter(self):
        data=self.data_transformer()
        train_data, test_data = train_test_split(data,test_size=0.2,stratify=data[self.schema.TARGET_COLUMN])
        encoder=TargetEncoder()
        train_data=encoder.fit_transform(train_data)
        test_data=encoder.transform(test_data)
        train_data=train_data.drop(self.schema.ENCODING_COLUMN,axis=1)
        test_data=test_data.drop(self.schema.ENCODING_COLUMN,axis=1)
        train_data.to_csv(os.path.join(self.config.root_directory,"train.csv"),index=False)
        test_data.to_csv(os.path.join(self.config.root_directory,"test.csv"),index=False)
        logger.info("Data splitted into training and test sets")
        logger.info(f" Training data size: {train_data.shape}")
        logger.info(f" Test data size: {test_data.shape}")

class TargetEncoder(BaseEstimator, TransformerMixin):
    def __init__(self,token_col:str,
                 output_col: str = "erc20_rec_token_risk"):
        self.schema=read_yaml(SCHEMA_FILE_PATH)
        self.token_col = self.schema.ENCODING_COLUMN
        self.target_col = self.schema.TARGET_COLUMN
        self.output_col = output_col
        self.token_risk_scores_ = None
    def fit(self, X: pd.DataFrame, y=None):
        fraud_count = X[X[self.target_col] == 1][self.token_col].value_counts()
        total_frauds = X[self.target_col].sum()
        self.token_risk_scores_ = (fraud_count / total_frauds).to_dict()
        return self
    def transform(self, X: pd.DataFrame):
        X = X.copy()
        X[self.output_col] = X[self.token_col].map(self.token_risk_scores_).fillna(0)
        return X





if __name__=="__main__":
    config=ConfigurationManager()
    data_transformation_config=config.get_data_transformation_config()
    data_transformation=DataTransformation(config=data_transformation_config)
    data_transformation.train_test_splitter()




