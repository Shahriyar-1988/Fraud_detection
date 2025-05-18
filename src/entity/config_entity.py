from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_directory: Path
    data_url: str
    local_data_path: Path

@dataclass
class DataTransformationConfig:
    root_directory: Path
    data_directory: Path
    drop_columns : list
    target_col: str

@dataclass
class TrainingConfig:
    root_directory: Path
    train_data_path: Path
    model_directory: Path
    metrics_directory: Path
    model_name: str
    target_col: str
    param_grid: dict

@dataclass
class ModelEvaluationConfig:
    test_data_path: Path
    tree_model_path: Path
    knn_model_path: Path
    metric_file_path: Path
    target_col: str
    mlflow_uri: str






    



