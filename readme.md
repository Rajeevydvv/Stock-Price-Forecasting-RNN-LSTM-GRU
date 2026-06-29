# Stock Forecasting with RNN, LSTM and GRU

## Overview

This project implements a deep learning pipeline for stock price forecasting using Recurrent Neural Networks (RNN), Long Short-Term Memory (LSTM), and Gated Recurrent Units (GRU).

The model is trained on historical Apple (AAPL) stock market data downloaded from Yahoo Finance and incorporates several technical indicators for feature engineering.

---

## Features

* Historical stock data collection using Yahoo Finance
* Exploratory Data Analysis (EDA)
* Stationarity testing using Augmented Dickey-Fuller (ADF) Test
* Technical Indicator Engineering

  * Moving Averages (MA20, MA50, MA200)
  * Exponential Moving Averages (EMA20, EMA50)
  * Relative Strength Index (RSI)
  * MACD
  * Bollinger Bands
  * Rolling Volatility
  * Volume-based Indicators
* Sequence generation for time-series forecasting
* Comparative study of:

  * Simple RNN
  * LSTM
  * GRU
* Early Stopping and Learning Rate Scheduling
* Performance Evaluation using:

  * MAE
  * MSE
  * RMSE
  * R² Score
  * MAPE

---

## Dataset

Source: Yahoo Finance

Ticker:

AAPL (Apple Inc.)

Period:

2015-01-01 to 2025-01-01

---

## Project Workflow

Data Collection

↓

Exploratory Data Analysis

↓

Feature Engineering

↓

Stationarity Analysis

↓

Time-Series Train/Test Split

↓

Feature Scaling

↓

Sequence Creation

↓

RNN / LSTM / GRU Training

↓

Performance Evaluation

---

## Results

The GRU model achieved the best performance among the evaluated architectures.

| Model | MAE    | RMSE   | R²     |
| ----- | ------ | ------ | ------ |
| RNN   | 0.1456 | 0.1814 | 0.015  |
| LSTM  | 0.3614 | 0.3802 | -3.327 |
| GRU   | 0.1019 | 0.1182 | 0.582  |

---

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Pandas
* Scikit-Learn
* Matplotlib
* Seaborn
* Yahoo Finance

---

## Future Improvements

* Multi-step forecasting
* Attention-based architectures
* Transformer-based forecasting
* Hyperparameter optimization
* Streamlit deployment
* Real-time prediction pipeline

---

## Author

Rajeev Yadav
