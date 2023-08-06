import streamlit as st

import numpy as np
import pandas as pd

from src.pipe.predict_pipeline import CustomData,PredictPipeline
from src.logger import logging
from src.exception import CustomException

import sys

# Define the Streamlit app
def main():
    # Custom theme
    st.markdown("""
    <style>
        .reportview-container {
            background-color: #111111;
        }
        .big-font {
            font-size:50px !important;
        }
        .text-font {
            font-size:20px !important;
        }
        .main {
            color: #8A2BE2;
        }
        .stButton>button {
            color: #8A2BE2;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # App header
    st.markdown("<p class='big-font main'>Number Classifier</p>", unsafe_allow_html=True)
    
    # User input
    number = st.text_input("Enter an integer (≤ 1024):")
    
    # Display message for constraints
    st.markdown("<p class='text-font'>Please ensure the input is an integer and less than or equal to 1024.</p>", unsafe_allow_html=True)
    
    # Predict button
    if st.button("Predict"):
        try:
            if number.isdigit() and int(number) <= 1024:

                data=CustomData(
                    Number=number
                )

                logging.info("Data Ingested")

                pred_df=data.get_data_as_data_frame()

                logging.info("Data as dataframe ready")

                predict_pipeline=PredictPipeline()

                logging.info("Predict_pipeline created")
                
                prediction=predict_pipeline.predict(pred_df)
                
                logging.info("Prediction ready")

                # Display the prediction
                st.markdown(f"<p class='big-font main'>{prediction[0]}</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p class='text-font'>Invalid input. Please enter a valid integer less than or equal to 1024.</p>", unsafe_allow_html=True)
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    main()
