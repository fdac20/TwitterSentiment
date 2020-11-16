import snscrape.modules.twitter as sntwitter
import csv
maxTweets = 3000

csvFile = open('tn.csv', 'a', newline='', encoding='utf8')

csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id','date','tweet', 'username'])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper("twitter-search:'knoxville tennessee' + since:2019-08-01 until:2020-08-01").get_items()):
    if i > maxTweets :
        break
    csvWriter.writerow([tweet.id, tweet.date, tweet.content, tweet.username])
csvFile.close()