import os
from src import logger
from src.entity.config_entity import DataIngestionConfig
from dotenv import load_dotenv
import shutil
from pathlib import Path
import kagglehub
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        load_dotenv()
    def extract_dataset_name(self, url: str) -> str:
        """
        Extracts the KaggleHub-friendly dataset name from the full URL.
        e.g., "https://www.kaggle.com/datasets/vagifa/ethereum-frauddetection-dataset"
        → "vagifa/ethereum-frauddetection-dataset"
        """
        return "/".join(url.rstrip("/").split("/")[-2:])
    def download_data(self):
        
        # Set Kaggle credentials from environment variables
        os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME")
        os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY")
        dataset_name= self.extract_dataset_name(self.config.data_url)
        logger.info(f"Downloading dataset: {dataset_name}")
        path=Path(kagglehub.dataset_download(dataset_name))
        os.makedirs(self.config.local_data_path, exist_ok=True)
         # Copy all files from cache to your desired location
        for item in path.iterdir():
            dest = Path(self.config.local_data_path) / item.name
            if item.is_file():
                shutil.copy(item, dest)
            elif item.is_dir():
                shutil.copytree(item, dest, dirs_exist_ok=True)

        logger.info(f"Dataset copied to {self.config.local_data_path}")
      
    





        

