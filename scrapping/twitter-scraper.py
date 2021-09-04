import pandas as pd
import numpy as np
import re
import snscrape.modules.twitter as sntwitter
from tqdm import tqdm

# PARAMETERS

PHRASE = ''
USERNAME = ''
SINCE = '' #2020-07-31
UNTIL = '' #2020-07-31
NO_OF_TWEETS = 150000
CSV_NAME = '' + '.csv'


def tweets_from_usernames(USERNAME):
	tweets_list = []

	# Using TwitterSearchScraper to scrape data and append tweets to list
	for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{USERNAME}').get_items()):
		if i > NO_OF_TWEETS:
			break
		tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.user.url, tweet.user.location, tweet.lang, tweet.source])
		
	# Creating a dataframe from the tweets list above 
	tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Url', 'Location', 'Lang', 'Source' ])
	return tweets_df


def tweets_from_phrase(PHRASE):
	tweets_list = []

	# Using TwitterSearchScraper to scrape data and append tweets to list
	for i,tweet in enumerate(tqdm(sntwitter.TwitterSearchScraper(f'{PHRASE}').get_items())):
		if i>NO_OF_TWEETS:
			break
		tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.user.url, tweet.user.location, tweet.lang, tweet.source])
		
	# Creating a dataframe from the tweets list above 
	tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Url', 'Location', 'Lang', 'Source' ])
	return tweets_df


# df = tweets_from_phrase('#Hashtag')
# df = tweets_from_usernames('username')