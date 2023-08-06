import sys
import os

import pandas as pd

from src.exception import CustomException
from src.utils import load_object
from src.logger import logging
from src.components.data_transformation import DataTransformation


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model_mlp.pkl")
            
            model=load_object(file_path=model_path)
            
            logging.info("Model loaded")

            preprocessor = DataTransformation()

            logging.info("Preprocessor created")
            
            data_scaled=preprocessor.initiate_data_transformation(features)
           
            logging.info("Data transformed")

            preds=model.predict(data_scaled)

            logging.info("Prediction ready.")
           
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(  self,
        Number: int
        ):

        self.Number = Number

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Number": [self.Number],
            }
            
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)