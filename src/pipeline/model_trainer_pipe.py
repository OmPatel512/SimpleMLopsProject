from src.config.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src import logger

STAGE_NAME = "Model Trainer"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        try:
            config = ConfigurationManager()
            model_train_config = config.get_model_train_config()
            model_trainer = ModelTrainer(config=model_train_config)
            model_trainer.train()
        except Exception as e:
            logger.exception(f"Error occurred during {STAGE_NAME} stage: {e}")
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>> Starting {STAGE_NAME} Stage <<<<<<<<<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.initiate_model_training()
        logger.info(f">>>>>>>>>>>>>>> {STAGE_NAME} Stage completed successfully. <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(f"Exception occurred in {STAGE_NAME} Stage: {e}")
        raise e 