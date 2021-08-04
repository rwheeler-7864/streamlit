#! /usr/bin/env python3
import yfinance as yf
import streamlit as st
import pandas as pd


# now do the markup stuff
st.write("""

# Simple Stock Price app using streamlit.io 

Shown are stock **closing** price and ***volume*** of Google stock price

rwheeler

""")

# get ticker symbol
tickerSymbol = "GOOGL"
# get data on the ticker symbol
tickerData = yf.Ticker(tickerSymbol)
# get historical price on symbol
tickerDf = tickerData.history(period = 'id', start = '2020-5-31', end = '2021-5-31')
# Open  High  Low  Close  Volume  Dividends  Stock Splits
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

