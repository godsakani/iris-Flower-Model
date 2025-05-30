import streamlit as st
import pandas as pd
import numpy as np
import pickle

# loading the saved model
try:
    with open("log_model.sav", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Please check the file path.")
    model = None


flower_image = st.image("iris2.png", width=50)
st.title("Iris Flower Prediction App") 
def user_input_features():
    sepal_length = st.number_input("Sepal Length", min_value=4.3, max_value=7.9, value=5.4)
    sepal_width = st.number_input("Sepal Width", min_value=2.0, max_value=4.4, value=3.4)
    petal_length = st.number_input("Petal Length", min_value=1.0, max_value=6.9, value=1.3)
    petal_width = st.number_input("Petal Width", min_value=0.1, max_value=2.5, value=0.2)
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()
st.write(df)


if st.button("Predict"):
    prediction = model.predict(df)
    if prediction[0] == 0:
        species = "Setosa"
    elif prediction[0] == 1:
        species = "Versicolor"
    elif prediction[0] == 2:
        species = "Virginica"
    else:
        species = "Unknown"
    st.success(f"The predicted flower species is: {species}")




