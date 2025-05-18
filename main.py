from src import logger
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.pipeline.training_pipeline import TrainingPipeline
from src.pipeline.evaluation_pipeline import EvaluationPipeline

# logger.info("Welcome to etherium transactions fraud detection project")
# STAGE_NAME = "Data Ingestion Stage"
# try:
#     logger.info(f">>>>{STAGE_NAME} started <<<<")
#     obj=DataIngestionPipeline()
#     obj.initiate_data_ingestion()
#     logger.info(f">>>> {STAGE_NAME} completed <<<<\n\n")
# except Exception as e:
#     raise e

# STAGE_NAME = "Data Transformation Stage"
# try:
#     logger.info(f">>>>{STAGE_NAME} started <<<<")
#     obj=DataTransformationPipeline()
#     obj.initiate_data_transformation()
#     logger.info(f">>>> {STAGE_NAME} completed <<<<\n\n")
# except Exception as e:
#     raise e

# STAGE_NAME = "Model training Stage"
# try:
#     logger.info(f">>>>{STAGE_NAME} started <<<<")
#     obj=TrainingPipeline()
#     obj.initiate_model_training()
#     logger.info(f">>>> {STAGE_NAME} completed <<<<\n\n")
# except Exception as e:
#     raise e

STAGE_NAME = "Model evaluation Stage"
try:
    logger.info(f">>>>{STAGE_NAME} started <<<<")
    obj=EvaluationPipeline()
    obj.initiate_evaluation()
    logger.info(f">>>> {STAGE_NAME} completed <<<<\n\n")
except Exception as e:
    raise e

