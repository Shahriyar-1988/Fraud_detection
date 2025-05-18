import os
import yaml
from box import ConfigBox
from typing import Any
from box.exceptions import BoxValueError
import joblib
from pathlib import Path
from ensure import ensure_annotations
from src import logger
import json


# This file contains the commonly used functionalities by the code
# Opening yaml file
@ensure_annotations
def read_yaml(yaml_path: Path)->ConfigBox:
    try:
        with open(yaml_path) as f:
            content = yaml.safe_load(f)
            logger.info(f" yaml file {yaml_path} loaded successfully!")
            return ConfigBox(content)
    except Exception as e:
        raise e
    except BoxValueError:
            raise ValueError(f"yaml file {os.path.split(yaml_path)[1]} is empty!")

# create directory
@ensure_annotations
def create_directories(path_of_directory:list,verbose=True):
     for path in path_of_directory:
          os.makedirs(path, exist_ok=True)
          if verbose:
               logger.info(f"created directory at: {path}")
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: object, path: Path):
    """save binary file

    Args:
        data (object): data to be saved as a python object
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

    
     

    



