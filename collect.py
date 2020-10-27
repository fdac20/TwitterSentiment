import GetOldTweets3 as got

uni_unames = ['DondePlowman', 'randyboyd', 'tucarpenter', 'UTIA_SVP', 'KC4UTM', 
              'utknoxville', 'utk_tce', 'utkdos', 'ut_admissions', 'utk_asc', 'UTKCEHHS'
              'utk_cfs', 'UTKStudentLife', 'UTKCoAD', 'UTKSOM', 'tennalum', 'utknursing', 'HaslamUT']

for idx, uname in enumerate(uni_unames):
    if idx == 5:
        break;
    tweetCriteria = got.manager.TweetCriteria().setUsername(uname).setSince("2019-08-01").setUntil("2020-08-01")
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    print(tweet.txt)