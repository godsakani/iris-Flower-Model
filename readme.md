# Iris Flower Prediction App

A Streamlit web application that predicts Iris flower species based on sepal and petal measurements using machine learning.

## Overview

This application uses a trained machine learning model to predict the species of Iris flowers based on four measurements:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The model can classify flowers into three species:
- Setosa
- Versicolor
- Virginica

## Features

- Interactive web interface built with Streamlit
- Real-time predictions
- Input validation with reasonable ranges for measurements
- Clear display of input data and prediction results

## Technical Details

- Built with Python 3.9
- Uses scikit-learn version 1.5.2 for the machine learning model
- Implements a Logistic Regression model with One-vs-One classification
- Model is saved using Python's pickle module

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install streamlit pandas numpy scikit-learn==1.5.2
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run iris.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Input the measurements for your Iris flower:
   - Sepal Length (4.3 - 7.9 cm)
   - Sepal Width (2.0 - 4.4 cm)
   - Petal Length (1.0 - 6.9 cm)
   - Petal Width (0.1 - 2.5 cm)

4. Click the "Predict" button to see the predicted species

## Model Information

The model was trained on the famous Iris dataset and uses a Logistic Regression classifier with One-vs-One classification strategy. The model is saved in `log_model.sav` and loaded at runtime.

## Requirements

- Python 3.9
- streamlit
- pandas
- numpy
- scikit-learn==1.5.2

## Note

Make sure to use scikit-learn version 1.5.2 as the model was trained and saved using this version. Using a different version might cause compatibility issues.
