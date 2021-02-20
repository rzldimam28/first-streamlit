import streamlit as st
from multiapp import MultiApp
from app import home, predict, data_overview

app = MultiApp()

# Add all your application here

app.add_app("Home", home.app)
app.add_app("Prediction", predict.app)
app.add_app("Data Overview", data_overview.app)

app.run()