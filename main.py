from src import logger
from src.pipeline.data_ingestion_pipe import DataIngestionTrainingPipeline

DataIngestionTrainingPipeline = DataIngestionTrainingPipeline()
logger.info("Data ingestion pipeline module loaded successfully.")
DataIngestionTrainingPipeline.initiate_data_ingestion()
logger.info("Data ingestion pipeline executed successfully.")