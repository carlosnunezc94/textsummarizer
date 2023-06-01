from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textsummarizer.logging import logger


STAGE_NAME = "data_ingestion"
try:
    logger.info(f"Stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "data_validation"
try:
    logger.info(f"Stage {STAGE_NAME} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "data_transformation"
try:
    logger.info(f"Stage {STAGE_NAME} started")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

