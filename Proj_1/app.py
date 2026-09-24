import yfinance as yf 
import pandas as pd
import streamlit as st

st.write("""
# Stock Price App

Shown are the stock closing price and volume of GOOGLE!
""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(
    start='2015-5-31', end='2026-5-31')
# a span of 10 years of data from 2015 to 2026


st.line_chart(tickerDf.Close)


st.line_chart(tickerDf.Volume)