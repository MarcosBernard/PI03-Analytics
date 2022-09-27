# Etherium historical price
from turtle import title
import streamlit as st
import datetime
import requests
import pandas as pd
import plotly.graph_objects as go

st.write("""
# FTX Market Trading app
""")
st.write("""
## 1. ETH/US
""")

api_url = 'https://ftx.us/api'
api = '/markets'
url = api_url+api
markets = requests.get(url).json()

# Historical data Etherium
market_name = 'ETH/USD' # Select cryto currency
resolution = 60*60*24*15 # Save time seconds
#start = datetime.datetime(2022,8,1).timestamp()

#path = f'/markets/{market_name}/candles?resolution={resolution}&start={start}'
path = f'/markets/{market_name}/candles?resolution={resolution}'
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
#fig.show()
# Plot!
st.plotly_chart(fig, use_container_width=True,title='Hola')