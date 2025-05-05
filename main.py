from src import logger
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline

logger.info("Welcome to etherium transactions fraud detection project")
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>{STAGE_NAME} started <<<<")
    obj=DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>> {STAGE_NAME} completed <<<<\n\n")
except Exception as e:
    raise e

