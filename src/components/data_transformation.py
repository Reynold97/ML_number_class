import os
import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd

from src.exception import CustomException
from src.logger import logging


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        self.num_digits:int = 10 


    # Function to convert numbers to their binary representation
    def binary_encode(self, i):
        return np.array([i >> d & 1 for d in range(self.num_digits)])


    # Function to transform initial dataframe V1 into dataframe V2
    def initiate_data_transformation(self,df:pd.DataFrame):
        try:
            # Convert the 'Number' column to integers
            df['Number'] = df['Number'].astype(int)
            
            # Applying the binary encoding function to the 'Number' column
            binary_representation = df['Number'].apply(lambda x: self.binary_encode(x))
            
            logging.info("Number converted to binary")

            # Creating a DataFrame from the binary matrix
            binary_df_v1 = pd.DataFrame(binary_representation.tolist(), columns=[f'Bit_{i}' for i in range(self.num_digits)])

            logging.info("Binary columns created")

            return binary_df_v1
        
        except Exception as e:
            raise CustomException(e,sys)
