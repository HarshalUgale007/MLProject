from scr.mlprojectds.logger import logging
from scr.mlprojectds.exception import CustomException
from scr.mlprojectds.components.data_ingestion import DataIngestion
from scr.mlprojectds.components.data_transformation import DataTransformation
from scr.mlprojectds.components.model_trainer import ModelTrainer
import sys

if __name__ == "__main__":
    logging.info("The execution has started")
    
    try:
        # Data Ingestion
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        
        # Data Transformation
        data_transformation = DataTransformation()
        transformation_result = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        
        if len(transformation_result) < 2:
            raise ValueError(f"initiate_data_transformation returned {len(transformation_result)} values instead of at least 2")
        
        train_arr, test_arr = transformation_result[:2]

        # Model Training
        model_trainer = ModelTrainer()
        model_trainer.initiate_model_trainer(train_arr, test_arr)
        
    except Exception as e:
        logging.error("An error occurred during execution: %s", str(e))
        raise CustomException(e, sys)
