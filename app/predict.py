import streamlit as st
from annotated_text import annotated_text, annotation
import numpy as np
import pandas as pd
import pickle

def app():
    st.title('Car Fuel Consumption')
    st.write('''
    In this submenu, you can predict how many liters of fuel did you spent on a mile of trips using below features.
    ''')
    st.subheader('User Input Features')
    st.write('''
    You can free to 'play' with these parameters below.
    ''')

    def user_input_features():
        cylinders = st.slider('Cylinders', 1, 10, 5)
        displacement = st.slider('Displacement', 50, 500, 200)
        horsepower = st.slider('Horse Power', 40, 250, 100)
        weight = st.slider('Weight', 1500, 2500, 5500)
        acceleration = st.slider('Acceleration', 5, 30, 10)
        model_year = st.slider('Model Year', 70, 90, 72)
        origin = st.slider('Origin', 1, 3, 2)
        data = {'Silinder Mesin' : cylinders,
                'Perpindahan Mesin' : displacement,
                'Tenaga Kuda' : horsepower,
                'Berat' : weight,
                'Akselerasi' : acceleration,
                'Model Tahun' : model_year,
                'Asal' : origin}
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    load_model = pickle.load(open('linear_regression_model.pkl', 'rb'))

    prediction = load_model.predict(input_df)
    prediction = np.round(prediction, 2)
    st.write('''
    Your car fuel efficiency with using above parameters is
    ''')
    annotated_text(
        (prediction, 'MPG', '#faa')
    )