# Number Classifier

## Description

The Number Classifier project is an application designed to classify integers into different categories based on certain rules, for multiples of three print “Fizz” instead of “None” and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”. The application leverages machine learning to carry out the classification and presents it through a web interface using Streamlit.

## Models Used

### 1. Logistic Regression

Logistic Regression is a classification algorithm that estimates the probability that an instance belongs to a particular class.

### 2. Support Vector Machines (SVM)

SVM is a supervised learning algorithm capable of classifying cases by finding the hyperplane that best divides a dataset into classes.

### 3. Decision Tree

Decision Trees divide the dataset into increasingly smaller subsets while simultaneously developing an associated decision tree.

### 4. Random Forest

Random Forest is an ensemble method that relies on multiple decision trees.

### 5. K-Nearest Neighbors (K-NN)

K-NN is an algorithm that classifies an instance based on how its nearest neighbors are classified.

### 6. Multi-Layer Perceptron (MLP)

MLP is a neural network consisting of at least three layers of nodes and can distinguish data that is not linearly separable.

After the experimentation phase, the only model with an acceptable response without performing hyperparameter optimization was the MLP. As it presented a high degree of precision, it was decided to continue with the other phases of the project without further optimization and validation.

## Project Structure

In the notebook folder you can find the notebooks that contain the research process. The artifacts folder contains the saved pikle files needed by the application, such as models and preprocessors. In datasets the different versions of the generated and transformed data set. The logs generated in the application are stored in the logs folder. The src folder contains the files responsible for exception handling, logging, the necessary components for the pipelines, and the training and prediction pipelines. This project structure is generic and due to the simplicity of the problem, its complete implementation was not necessary, leaving aside data ingestion and the training pipeline.

## Installation and Execution

### Execution via Command Line

Clone the repository

Navigate to the project directory

Install dependencies using pip install -r requirements.txt

Run the application with streamlit run app.py

Open a browser and navigate to http://localhost:8501

### Execution with Docker

Clone the repository

Navigate to the project directory

Build the Docker image with docker build -t my-streamlit-app .

Run the container with docker run -p 8501:8501 my-streamlit-app

Open a browser and navigate to http://localhost:8501