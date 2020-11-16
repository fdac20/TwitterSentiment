import snscrape.modules.twitter as sntwitter
import csv
maxTweets = 3000

csvFile = open('place_result.csv', 'a', newline='', encoding='utf8')

csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id','date','tweet',])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:@billgates + since:2015-12-02 until:2020-11-05-filter:links -filter:replies').get_items()):
    if i > maxTweets :
        break
    csvWriter.writerow([tweet.id, tweet.date, tweet.content])
csvFile.close()