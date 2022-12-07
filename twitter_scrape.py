import snscrape.modules.twitter as sntwitter
import pandas as pd

''' This can scrape thousands of tweets within minutes can be used for ML models training and much more
Just change account name, Until, Since in line 9 and limit in line 15'''


# your query goes here, account to scrape and since when to scrape
query = "(from:elonmusk) until:2022-12-01 since:2022-01-01"

# creating list to append tweet data to
tweets = []

# maximum number of tweets to scrape
limit = 10000

# using TwitterSearchScraper to scrape
for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])


# creating a dataframe from the tweets list above
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])


# to save to csv
df.to_csv('tweets.csv')

