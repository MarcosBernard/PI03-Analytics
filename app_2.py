from asyncio.base_futures import _FINISHED
import streamlit as st
import datetime
import requests
import pandas as pd
from client import FtxClient
#import mplfinance as mpf
import plotly.express as px
import plotly.graph_objects as go

cryptoc = ' '

st.write("""
# FTX Market Trading app
""")

def historical_data(market_name_):
    
    api_url = 'https://ftx.com/api'
    api = '/markets'
    url = api_url+api
    markets = requests.get(url).json()
    #if market_name_ == 'BTC/USD'
    # Historical data Etherium
    #market_name = market_name_ # Select cryto currency
    resolution = 60*60*24*30 # Save time seconds
    start = datetime.datetime(2021,1,1).timestamp()
    #path = f'/markets/{market_name_}/candles?resolution={resolution}&start={start}'
    path = f'/markets/{market_name_}/candles?resolution={resolution}'
    url = api_url + path
    res = requests.get(url).json()
    df = pd.DataFrame(res['result'])
    df['date'] = pd.to_datetime(df['startTime'])
    df = df.drop(columns=['startTime', 'time'])
    fig = go.Figure(data=[go.Candlestick(x=df['date'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'])])
    return(st.plotly_chart(fig, use_container_width=True))

#Making a Buttons
ena1 = st.button("BTC-PERP")

if ena1:
    #st.write(":smile:")
    st.title("BTC-PERP Historical data")
    historical_data('BTC-PERP')
    ena1 = False