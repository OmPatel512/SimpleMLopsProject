from src.config.configuration import ConfigurationManager  
from src.components.data_transformation import DataTransformation
from src import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.initiate_data_transformation()
        logger.info("Data transformation completed successfully.")
        
if __name__ == "__main__":
    try:
        logger.info(">>>>>>>>>>>>>>>> Starting Data Transformation Stage <<<<<<<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(">>>>>>>>>>>>>> Data Transformation Stage completed successfully. <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(f"Exception occurred in Data Transformation Stage: {e}")
        raise e
    