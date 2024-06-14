import streamlit as st 
import yfinance as yf
import pandas as pd
import plotly as p
import plotly.express as px
import plotly.graph_objects as go

from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

st.sidebar.title("Stock Selector")
st.sidebar.divider()
st.header("Stock Predictor")
st.divider()

tickers = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]

stock = st.sidebar.selectbox(
    label="Choose a  stock:",
    options= tickers["Security"],
    format_func=lambda x: x,
)   

sto = tickers[tickers["Security"] == stock]["Symbol"].values[0]

years = st.sidebar.radio(
    "Range of the actual values:",
    ['5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'], horizontal = True
)

pred = st.sidebar.slider("How far you want to predict? (in days)", 0, 36525, 365)

st.write(stock +" stock price change in "+ years + " and predicted values for the " + str(pred) + " day period")

st.sidebar.write(f"You selected: {stock} ({sto}) with the base of {years} range")


data = yf.download(sto, period = years)

value_close = pd.DataFrame(data["Close"])
df = pd.DataFrame(value_close.reset_index())
df.columns = ['ds','y']

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods= int(pred))
forecast = m.predict(future)


figure1 = plot_plotly(m, forecast)
figure2 = plot_components_plotly(m, forecast)

figure1.update_layout(
    paper_bgcolor="#f8f8fa",
    plot_bgcolor="#e5e6eb",
    title_text="Main graph",
    margin_t=100,
    margin_b=100,
    margin_r=30,
    margin_l=30
)

figure2.update_layout(
    paper_bgcolor="#f8f8fa",
    plot_bgcolor="#e5e6eb",
    title_text="Component graphs",
    margin_t=100,
    margin_b=100,
    margin_r=30,
    margin_l=30
)

figure1.update_xaxes(
    showline=True, linewidth=2, linecolor='gray',
)

figure1.update_yaxes(
    
    showline=True, linewidth=2, linecolor='gray',
)

figure2.update_xaxes(
    showline=True, linewidth=2, linecolor='gray',
)

figure2.update_yaxes(
    
    showline=True, linewidth=2, linecolor='gray',
)


st.plotly_chart(figure1,use_container_width=True)
st.plotly_chart(figure2,use_container_width=True)
