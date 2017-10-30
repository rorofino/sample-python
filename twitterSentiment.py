import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

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