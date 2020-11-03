import pandas as pd

d = pd.read_csv('utknoxville.csv')

tweets_df = pd.DataFrame(data=d)

tweets = tweets_df['content']

for tweet in tweets:
    print(tweet)