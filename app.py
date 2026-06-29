import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler

st.title("Stock Price Forecasting")

ticker = st.text_input("Ticker", "AAPL")

if st.button("Predict"):

    df = yf.download(
        ticker,
        start="2015-01-01"
    )

    st.write(df.tail())

    st.success(
        "Model loaded successfully."
    )

    st.info(
        "Prediction pipeline can be connected to the trained GRU model."
    )
