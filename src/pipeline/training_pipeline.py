from src.config.configuration import ConfigurationManager
from src.components.training import Training

class TrainingPipeline:
    def __init__ (self):
        pass
    def initiate_model_training(self):
        config = ConfigurationManager()
        training_config=config.get_training_config()
        model_trainer=Training(training_config)
        model_trainer.trainer()
