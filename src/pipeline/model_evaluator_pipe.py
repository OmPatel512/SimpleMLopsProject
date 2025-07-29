from src.components.model_evaluator import ModelEvaluation
from src.config.configuration import ConfigurationManager
from src import logger

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        try:
            config = ConfigurationManager()
            model_eval_config = config.get_model_evaluation_config()
            model_evaluator = ModelEvaluation(config=model_eval_config)
            model_evaluator.log_into_mlflow()
        except Exception as e:
            logger.exception(f"Error occurred during {STAGE_NAME} stage: {e}")
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>> Starting {STAGE_NAME} Stage <<<<<<<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>>>>>>>>>>> {STAGE_NAME} Stage completed successfully. <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(f"Exception occurred in {STAGE_NAME} Stage: {e}")
        raise e