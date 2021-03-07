import streamlit as st 
import pandas as pd
import numpy as np
import requests
import tweepy
import config
import plotly.graphobjects as go

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

st.sidebar.write("StreamLit Sidebar")

st.sidebar.text("Options")
option = st.sidebar.selectbox("Which Dashboard", ('Twitter', 'WallstreetBets', 'Chart', 'StockTwits'))

st.header(option)

if option == 'Twitter':
    for username in config.TWITTER_USERNAMES:
        user = api.get_user(username)
        tweets = api.user_timeline(username)
        st.header(username)
        st.image(user.profile_image_url)

        for tweet in tweets:
            if '$' in tweet.text:
                words = tweet.text.split(' ')
                for word in words:
                    if word.startswith('$') and word[1:].isalpha():
                        symbol = word[1:]
                        st.write(symbol)
                        st.write(tweet.text)
                        st.image(f"https://finviz.com/chart.ashx?t={symbol}")



if option == 'Chart':
    st.subheader("StreamLit Chart Logic")

if option == 'WallstreetBets':
    st.subheader("Wallstreetbets Logic")

if option == 'StockTwits':
    
    symbol = st.sidebar.text_input("Symbol", value='AAPL', max_chars=5)
    r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
    
    data = r.json()

    for message in data['messages']:
        st.write(message['user']['username'])
        st.image(message['user']['avatar_url'])
        st.write(message['body'])
        st.write(message['created_at'])