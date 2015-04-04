import tweepy
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

consumer_key='M5WaMYqVPjODgKMbWhVwnBRGA'
consumer_secret='Z5xMhSrj4P1zerBuFKjAUkyBvhGeypmgRnZZ5ynTlhUlaAbx8H'
access_token='313642562-xhZu0SdkXFWjIzLf4poaTZe9J8TPDyDYsCjowEvI'
access_token_secret='kcW1DmYcp4EhIjX7v0v15U8l2hYDtPjfr24Mah5e7OTxo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

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

