import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key = 'CONSUMER_KEY_HERE'
consumer_secret = 'Your consumer secret here'
access_token = 'Your access token here'
access_token_secret = 'Your access token secret here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 2 - Retrieve Tweets
public_tweets = api.search('Your Keyword or Hashtag', count=100)

# Step 3: Perform Sentiment Analysis on Tweets
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0:
        print(f'[Positive]: {tweet.text}')
    elif sentiment < 0:
        print(f'[Negative]: {tweet.text}')
    else:
        print(f'[Neutral]: {tweet.text}')