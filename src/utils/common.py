import os
import yaml
from src import logger
import joblib
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} read successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """Create list of directories

    Args:
        path_to_directories (list): list of path of directories to be created
        ignore_log (bool, optional): ignore if multiple directories are created. Defaults to True.
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")
            
@ensure_annotations
def save_json(path: Path, data: Any):
    """Save data to a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (Any): Data to be saved.
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"Data saved to {path}")
        
@ensure_annotations
def load_json(path: Path) -> Any:
    """Load data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        Any: Data loaded from the JSON file.
    """
    with open(path, 'r') as json_file:
        data = json.load(json_file)
        logger.info(f"Data loaded from {path}")
        return ConfigBox(data)
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save data to a binary file using joblib.

    Args:
        data (Any): Data to be saved.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Data saved to {path} in binary format.")
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load data from a binary file using joblib.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(filename=path)
    logger.info(f"Data loaded from {path} in binary format.")
    return data 