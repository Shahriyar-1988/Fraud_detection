#Activate only when testing this code individually
# import sys
# import os

# # Fix path so that 'src' can be imported properly
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


import os
from src import logger
from src.utils.common import save_bin,save_json
import pandas as pd
from pathlib import Path
from src.config.configuration import TrainingConfig
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.impute import KNNImputer
from sklearn.model_selection import RandomizedSearchCV
from imblearn.pipeline import Pipeline
from imblearn.under_sampling import RandomUnderSampler
from sklearn.metrics import f1_score
from src.config.configuration import ConfigurationManager

class Training:
    def __init__ (self,config:TrainingConfig):
        self.config=config
    def trainer(self):
        train_data=pd.read_csv(self.config.train_data_path)
        tree_pipeline=Pipeline(steps=[('imputer',KNNImputer()),
                                      ('sampler',RandomUnderSampler(sampling_strategy=0.4,random_state=0)),
                                      ('classifier', ExtraTreesClassifier(random_state=32))])
        knn_pipeline=Pipeline(steps=[('imputer',KNNImputer()),
                                      ('sampler',RandomUnderSampler(sampling_strategy=0.4,random_state=0)),
                                      ('classifier', KNeighborsClassifier())])

        X_train=train_data.drop(self.config.target_col,axis=1)
        y_train=train_data[self.config.target_col]
        # KNN model
        knn_=knn_pipeline.fit(X_train,y_train)
        cv_scores = cross_val_score(knn_pipeline,X_train,y_train,cv=5,scoring='f1_macro')
        logger.info(f" The KNN model has an f1_macro score of {cv_scores.mean():.2f} for training!")
        model_name="KNNClassifier_"+ self.config.model_name
        model_path=Path(os.path.join(self.config.model_directory,model_name))
        save_bin(knn_,model_path)

        # For extra-tree the model will be tuned
        param_grid=self.config.param_grid
        grid_search=RandomizedSearchCV(estimator=tree_pipeline,
                                       param_distributions=param_grid,
                                       cv=5,
                                       scoring='f1_macro',
                                       n_jobs=-1)
        xtra_tree=grid_search.fit(X_train,y_train)
        best_fit=xtra_tree.best_estimator_
        best_params = xtra_tree.best_params_
        model_name="ExtraTree_"+self.config.model_name
        model_path=Path(os.path.join(self.config.model_directory,model_name))
        save_bin(best_fit, model_path)
        params_json_path = os.path.join(self.config.model_directory, "model_params.json")
        save_json(Path(params_json_path),best_params)
        
        

if __name__=="__main__":
    config=ConfigurationManager()
    training_config=config.get_training_config()
    model_trainer=Training(config=training_config)
    model_trainer.trainer()




        





