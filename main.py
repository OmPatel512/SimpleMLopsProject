from src import logger
from src.pipeline.data_ingestion_pipe import DataIngestionTrainingPipeline
from src.pipeline.data_validation_pipe import DataValidationTrainingPipeline
from src.pipeline.data_transformation_pipe import DataTransformationTrainingPipeline
from src.pipeline.model_trainer_pipe import ModelTrainerPipeline

DataIngestionTrainingPipeline = DataIngestionTrainingPipeline()
logger.info("Data ingestion pipeline module loaded successfully.")
DataIngestionTrainingPipeline.initiate_data_ingestion()
logger.info("Data ingestion pipeline executed successfully.")

DataValidationTrainingPipeline = DataValidationTrainingPipeline()
logger.info("Data validation pipeline module loaded successfully.")
DataValidationTrainingPipeline.initiate_data_validation()
logger.info("Data validation pipeline executed successfully.")

DataTransformationTrainingPipeline = DataTransformationTrainingPipeline()
logger.info("Data transformation pipeline module loaded successfully.")
DataTransformationTrainingPipeline.initiate_data_transformation()   
logger.info("Data transformation pipeline executed successfully.")

ModelTrainerPipeline = ModelTrainerPipeline()
logger.info("Model trainer pipeline module loaded successfully.")       
ModelTrainerPipeline.initiate_model_training()
logger.info("Model trainer pipeline executed successfully.")