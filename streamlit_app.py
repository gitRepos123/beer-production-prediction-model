import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

st.header('Beer Production Prediction - ARIMA Model')
def make_response(months: int = 1) -> None:
    months_array = [ month+1 for month in range(months) ]
    model = joblib.load('beer-production-prediction-model.pk1')
    predictions = model.forecast(steps = months)
    df = pd.DataFrame({
        'Month': months_array,
        'Production': predictions
    })
    st.subheader('Beer Production Trend')
    fig = plt.figure()
    plt.xlabel('Month')
    plt.ylabel('Production')
    plt.plot(df['Month'], df['Production'], color = 'green') 
    st.pyplot(fig)
    st.subheader('Predictions')
    st.table(df)

def init_app():
    days = st.slider('Number of Months', min_value = 1, max_value = 6, step = 1)
    make_response(days)

init_app()
