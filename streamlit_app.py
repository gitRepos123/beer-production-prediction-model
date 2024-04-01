import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

st.header('Beer Production Prediction - ARIMA Model')
def make_response(days: int = 1) -> None:
    days_array = [ day+1 for day in range(days) ]
    model = joblib.load('beer-production-prediction-model.pk1')
    predictions = model.forecast(steps = days)
    st.subheader('Beer Production Trend')
    fig = plt.figure()
    plt.xlabel('Day')
    plt.ylabel('Production')
    plt.plot(df['Day'], df['Production'], color = 'green') 
    st.pyplot(fig)
    st.subheader('Predictions')
    df = pd.DataFrame({
        'Day': days_array,
        'Production': predictions
    })
    st.table(df)

def init_app():
    days = st.slider('Number of Days', min_value = 1, max_value = 500, step = 1)
    make_response(days)

init_app()
