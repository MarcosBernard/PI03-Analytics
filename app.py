from asyncio.base_futures import _FINISHED
import streamlit as st
import datetime
import requests
import pandas as pd
from client import FtxClient
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

T = [
    'BTC-PERP','ETH-PERP','BTC/USD','ETH/USD','SOL-PERP',
    'XRP-PERP','ATOM-PERP','LUNC-PERP','ETH-1230','XRP/USD'
]

#Making a Buttons
en1 = st.button(T[0])
en2 = st.button(T[1])
en3 = st.button(T[2])
en4 = st.button(T[3])
en5 = st.button(T[4])
en6 = st.button(T[5])
en7 = st.button(T[6])
en8 = st.button(T[7])
en9 = st.button(T[8])
en10 = st.button(T[9])

if en1:
    st.write(f'## {T[0]} Historical price')
    historical_data(T[0])
    en1 = False
if en2:
    st.write(f'## {T[1]} Historical price')
    historical_data(T[1])
    en2 = False
if en3:
    st.write(f'## {T[2]} Historical price')
    historical_data(T[2])
    en3 = False
if en4:
    st.write(f'## {T[3]} Historical price')
    historical_data(T[3])
    en4 = False
if en5:
    st.write(f'## {T[4]} Historical price')
    historical_data(T[4])
    en5 = False
if en6:
    st.write(f'## {T[5]} Historical price')
    historical_data(T[5])
    en6 = False
if en7:
    st.write(f'## {T[6]} Historical price')
    historical_data(T[6])
    en7 = False
if en8:
    st.write(f'## {T[7]} Historical price')
    historical_data(T[7])
    en8 = False
if en9:
    st.write(f'## {T[8]} Historical price')
    historical_data(T[8])
    en9 = False
if en10:
    st.write(f'## {T[9]} Historical price')
    historical_data(T[9])
    en10 = False