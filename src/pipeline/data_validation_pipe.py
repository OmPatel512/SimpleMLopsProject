from src.config.configuration import ConfigurationManager
from src import logger
from src.components.data_validation import DataValidation

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_validation(self):
        config_manager = ConfigurationManager()
        data_validation_config = config_manager.get_data_validation_config()
        
        data_validation = DataValidation(config=data_validation_config)
        validation_status = data_validation.validate_all_columns()
        
        if validation_status:
            logger.info(f"{STAGE_NAME} completed successfully.")
        else:
            logger.error(f"{STAGE_NAME} failed. Check the status file for details.")

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>> Starting {STAGE_NAME} <<<<<<<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>>>>>>>>>>>>{STAGE_NAME} completed successfully. <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(f"Exception occurred in {STAGE_NAME}: {e}")
        raise e