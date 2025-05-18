import os
from pathlib import Path
import pandas as pd
from src.config.configuration import ModelEvaluationConfig
import joblib
import mlflow
from src import logger
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from sklearn.metrics import( classification_report,ConfusionMatrixDisplay,
                            roc_auc_score,
                            confusion_matrix,f1_score,recall_score)

class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config=config
    @staticmethod
    def evaluation_metrics(actual,predict):
        cls_rep = classification_report(actual,predict, output_dict=True)
        f1=f1_score(actual,predict,average='macro')
        recall=recall_score(actual,predict,average='macro')
        try:
            roc_score = roc_auc_score(actual,predict)
        except ValueError as e:
            logger.warning(f"ROC score is not defined! {e}")
            roc_score=0.0
    
        return cls_rep, roc_score,f1,recall
    

    def model_logger(self,model,test_data,model_name):

        X_test=test_data.drop(self.config.target_col,axis=1)
        y_test=test_data[self.config.target_col]
        y_pred=model.predict(X_test)
        cls_rep,roc_score,f1,recall=self.evaluation_metrics(y_test,y_pred)
        load_dotenv()
        MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        mlflow.set_experiment(f"{model_name} fraud detection experiment")
        with mlflow.start_run():

            mlflow.log_dict(cls_rep,"classification_report.json")
            mlflow.log_metric("ROC",round(roc_score,3))
            mlflow.log_metrics({"f1":round(f1,3),"recall":round(recall,3)})
            cm=confusion_matrix(y_test,y_pred)
            disp=ConfusionMatrixDisplay(confusion_matrix=cm)
            disp.plot(cmap="viridis",values_format='d')
            plt.title(f"Confusion Matrix for {model_name}")
            plt.tight_layout()
            cm_path = f"{model_name}_confusion_matrix.jpg"
            plt.savefig(cm_path)
            plt.close()
            mlflow.log_artifact(cm_path)

    def model_evaluator(self):
        test_data=pd.read_csv(self.config.test_data_path)
        tree_model=joblib.load(self.config.tree_model_path)
        knn_model=joblib.load(self.config.knn_model_path)
        self.model_logger(tree_model,test_data,"ExtraTree")
        self.model_logger(knn_model,test_data,"KNN")

        







