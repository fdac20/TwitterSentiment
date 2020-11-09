# import SentimentIntensityAnalyzer class 
# from vaderSentiment.vaderSentiment module. 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import dateutil.parser
import numpy as np

# function to print sentiments 
# of the sentence. 
def sentiment_scores(sentence): 
  
    # Create a SentimentIntensityAnalyzer object. 
    sid_obj = SentimentIntensityAnalyzer() 
  
    # polarity_scores method of SentimentIntensityAnalyzer 
    # oject gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
      
    print("Overall sentiment dictionary is : ", sentiment_dict) 
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
  
    print("Sentence Overall Rated As", end = " ") 
  
    # decide sentiment as positive, negative and neutral 
    if sentiment_dict['compound'] >= 0.05 : 
        print("Positive") 
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        print("Negative") 
  
    else : 
        print("Neutral") 
  
  
    
# Driver code 
if __name__ == '__main__' : 

    # Extract content and date fields from csv
    fields=['date', 'content']
    d = pd.read_csv('combined_csv.csv', usecols=fields)

    # Create dataframe
    tweets_df = pd.DataFrame(data=d)

    # Calculate polarity scores and store compound result into vals
    sid_obj = SentimentIntensityAnalyzer() 

    vals = []

    tweets = tweets_df['content'].tolist()
    for tweet in tweets:
        sentiment_dict = sid_obj.polarity_scores(tweet)
        vals.append(sentiment_dict['compound'])

    # Add vals to dataframe
    tweets_df['compound'] = vals 

    # Concert ISO 8601 time format to be readable by pandas
    tweets_df['date'] = tweets_df['date'].apply(lambda x: dateutil.parser.parse(x))

    # Set index as the data
    tweets_df.index = tweets_df['date']

    # Drop content column and resample on a weekly basis, calculating the mean of each month
    data = tweets_df.drop(columns=['content']).resample('W').mean()

    # print(data)

    # xticks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # labels = ['August \'19', 'September \'19', 'October \'19', 'November \'19', 'December \'19', 'January \'20', 'February \'20', 'March \'20', 'April \'20', 'May \'20', 'June \'20', 'July \'20', 'August \'20']

    plt.figure()
    # plt.plot(range(0, len(data)), data)
    plt.ylim(-1, 1)
    # plt.xticks(xticks, labels)
    plt.plot(np.arange(1, 56), data)
    plt.show()