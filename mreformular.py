import tweepy
import sys
from tweepy import Curs|
api = tweepy.API(auth)

# public_tweets = api.home_timeline()
#for tweet in public_tweets:
 #   print tweet.text

#for status in tweepy.Cursor(api.user_timeline).items():
    
#   process_status(status)
palabras=['hola','gato','nombre','tonto','abril','daniel','sol','javiera','dos','diez']
for x in xrange(1,10):
	for tweet in tweepy.Cursor(api.search,q=palabras[x],count=1,result_type="recent",include_entities=True,lang="en").items(1):
		print tweet.created_at, unicode(tweet.text)

#for tweet in tweepy.Cursor(api.search(q='bachelet',rpp=1,count=1,show_user='True')).items():
 #   print tweet.created_at, tweet.text
#for tweet in c
#	print tweet.text



#hi=api.followers_ids('Fakoxx')
#print hi

