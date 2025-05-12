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




