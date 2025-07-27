from src import logger
from src.components.data_ingestion import DataIngestion
from src.config.configuration import ConfigurationManager

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_ingestion(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()
        
        logger.info(f"{STAGE_NAME} completed successfully.")
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>> Starting {STAGE_NAME} <<<<<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>>>>>>>>>>>>{STAGE_NAME} completed successfully. <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(f"Exception occurred in {STAGE_NAME}: {e}")
        raise e
    
    