import os
from src import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config  = config
        
        
    def initiate_data_transformation(self):
        data = pd.read_csv(self.config.data_path)
        
        train, test = train_test_split(data, test_size=0.2, random_state=42)
        
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)
        
        logger.info("Splitted data into train ans test sets.")
        logger.info(train.shape)
        logger.info(test.shape)
        