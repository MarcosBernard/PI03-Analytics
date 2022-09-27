import streamlit as st
import datetime
import requests
import pandas as pd
from client import FtxClient
import mplfinance as mpf
import plotly.express as px
import plotly.graph_objects as go

st.write("""
# My first app
Hello *world!*
""")
api_url = 'https://ftx.us/api'
api = '/markets'
url = api_url+api
markets = requests.get(url).json()

# Historical data Etherium
market_name = 'ETH/USD' # Select cryto currency
resolution = 60*60*24*30 # Save time seconds
start = datetime.datetime(2022,1,1).timestamp()
path = f'/markets/{market_name}/candles?resolution={resolution}&start={start}'
url = api_url + path
res = requests.get(url).json()
df = pd.DataFrame(res['result'])
df['date'] = pd.to_datetime(df['startTime'])
df = df.set_index('date')
df = df.drop(columns=['startTime', 'time'])
#df
#mpf.plot(df.iloc[:,:],type='candle',style='charles',title='Etherium',ylabel='Price')

fig = px.Figure()

fig = go.Figure(data=[go.Candlestick(x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])
fig.show()