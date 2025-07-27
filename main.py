from src import logger
from src.pipeline.data_ingestion_pipe import DataIngestionTrainingPipeline
from src.pipeline.data_validation_pipe import DataValidationTrainingPipeline
from src.pipeline.data_transformation_pipe import DataTransformationTrainingPipeline


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