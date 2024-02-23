import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta
import streamlit as st
import plotly.graph_objs as go
import pandas as pd

def getStockData(ticker, timePeroid):
    if timePeroid == '1d':
        neededTime = date.today() -  timedelta(days = 1)
    elif timePeroid == '5d':
        neededTime = date.today() - timedelta(days= 5)
    elif timePeroid == '1m':
        neededTime = date.today() - timedelta(days=30)
    elif timePeroid == '6m':
        neededTime = date.today() - timedelta(days=183)
    elif timePeroid == '1y':
        neededTime = date.today() - timedelta(days=365)
    elif timePeroid == '5y':
        neededTime = date.today() - timedelta(days = 1825)
    return yf.download(ticker, neededTime, date.today())
def plotStockData(ticker,stock):
    fig, ax = plt.subplots()
    ax.plot(stock['Close'])
    ax.set_title(f'{ticker} Stock Price')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    st.pyplot(fig)
def displayStats(current_price, high_price, low_price):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Close Price", f"${current_price:.2f}")
    with col2:
        st.metric("52-Week High", f"${high_price:.2f}")
    with col3:
        st.metric("52-Week Low", f"${low_price:.2f}")
st.title('Stock Dashboard')
ticker = st.text_input('Enter a ticker')
whatTimePeriod = st.radio('Select time period', ['1d','5d','1m','6m','1y','5y'])
submit = st.button('Submit')
stock_data = getStockData(ticker, whatTimePeriod)
latest_close_price = stock_data.iloc[-1]["Close"]
max_52_week_high = stock_data["High"].tail(252).max()
min_52_week_low = stock_data["Low"].tail(252).min()
if submit:
    displayStats(latest_close_price,max_52_week_high,min_52_week_low)
    plotStockData(ticker,stock_data)
