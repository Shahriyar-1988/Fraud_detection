from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_directory: Path
    data_url: str
    local_data_path: Path


