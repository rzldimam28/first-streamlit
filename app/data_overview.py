import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def app():
    st.title('Data')
    st.write('''
    This app using 'auto-mpg' dataset on kaggle, you can access it [here] (https://www.kaggle.com/uciml/autompg-dataset).
    ''')
    st.write('''
    # Data Overview
    ''')
    st.write('Below listed the first 10 rows of the cleaned data.')
    data_cleaned = pd.read_csv('data_cleaned.csv')
    st.write(data_cleaned.head(10))
    st.write('''
    # Data Description
    ''')
    st.write('The variable names and its definition.')
    data_desc = pd.read_excel('data_desc.xls', index_col=0)
    pd.set_option('display.width', None)
    st.write(data_desc)
    st.write('''
    # Exploratory Data Analysis
    ''')
    st.write('''
    ### Descriptive Statictics
    ''')
    st.write(data_cleaned.describe())
    st.write('''
    ### Data Visualization
    ''')
    # numerical col
    fig, axes = plt.subplots(4, 2)
    fig.suptitle('Distribution of')
    axes[0, 0].hist(data_cleaned['mpg'])
    axes[0, 1].hist(data_cleaned['cylinders'])
    axes[1, 0].hist(data_cleaned['displacement'])
    axes[1, 1].hist(data_cleaned['horsepower'])
    axes[2, 0].hist(data_cleaned['weight'])
    axes[2, 1].hist(data_cleaned['acceleration'])
    axes[3, 0].hist(data_cleaned['model year'])
    axes[3, 1].hist(data_cleaned['origin'])
        
    axes[0, 0].set_title('MPG')
    axes[0, 1].set_title('Cylinders')
    axes[1, 0].set_title('Displacement')
    axes[1, 1].set_title('Horsepower')
    axes[2, 0].set_title('Weight')
    axes[2, 1].set_title('Acceleration')
    axes[3, 0].set_title('Model Year') 
    axes[3, 1].set_title('Origin') 
     
    fig.tight_layout()
    st.pyplot(fig)