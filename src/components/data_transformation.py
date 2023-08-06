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
        num_digits:int = 10 


    # Function to convert numbers to their binary representation
    def binary_encode(i, num_digits):
        return np.array([i >> d & 1 for d in range(num_digits)])


    # Function to transform initial dataframe V1 into dtaframe V2
    def initiate_data_transformation(self,df:pd.DataFrame):
        try:
            # Applying the binary encoding function to the 'Number' column
            binary_representation = df['Number'].apply(lambda x: self.binary_encode(x, self.num_digits))
            
            logging.info("Number converted to binary")

            # Creating a DataFrame from the binary matrix
            binary_df_v1 = pd.DataFrame(binary_representation.tolist(), columns=[f'Bit_{i}' for i in range(self.num_digits)])

            logging.info("Binary columns created")

            # Concatenating the binary DataFrame with the original
            data_v1_transformed = pd.concat([df, binary_df_v1], axis=1)

            logging.info("New dataframe concatenated")

            return data_v1_transformed
        
        except Exception as e:
            raise CustomException(e,sys)
