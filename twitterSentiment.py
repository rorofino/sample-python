import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'Hmezj3u04S2lWwsBEQQ7MU9QF'
consumer_secret= 'ZFMpVcrx3wMa39nZWmPjwgSQVf7p2tb0mGdO12Ecvn8n13QPHZ'

access_token='98268224-KoeIoBqC8wLXnKYKBrzbw1EhcWtW7RjEfYiuGPha9'
access_token_secret='QK0MWGUN4jyzrXE76pRliPEtQjPMSyeBu4qVg6BuKjSk2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Super Mario Odyssey')

print("got {} tweets", +len(public_tweets))

dict = {'Good': 0, 'Bad': 0}

for tweet in public_tweets:
    print(tweet.text)
    print("")
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
    if analysis.sentiment.polarity < 0.5:
        dict['Good'] += 1
    else:
        dict['Bad'] += 1

print()
print(dict)