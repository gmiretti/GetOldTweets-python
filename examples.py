import got3 as got

#    Get tweets by username

tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
print(tweet.text)

#    Get tweets by query search

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees').setSince("2015-05-01").setUntil("2015-09-30").setMaxTweets(1)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
print(tweet.text, tweet.date)

#    Get tweets by username and bound dates

tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
print(tweet.text, tweet.date)

#    Get the last 10 top tweets by username

tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama").setTopTweets(True).setMaxTweets(10)
# first one
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[9]
print(tweet.text)
