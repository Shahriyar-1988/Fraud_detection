from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation

class EvaluationPipeline:
    def __init__(self):
        pass
    def initiate_evaluation(self):
        config=ConfigurationManager()
        evaluation_config=config.get_evaluation_config()
        model_evaluation=ModelEvaluation(config=evaluation_config)
        model_evaluation.model_evaluator()



