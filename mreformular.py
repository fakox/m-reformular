# -*- encoding: utf-8 -*-
import tweepy
import sys
import urllib3.contrib.pyopenssl

urllib3.contrib.pyopenssl.inject_into_urllib3()
reload(sys)
sys.setdefaultencoding("utf-8")

consumer_key='M5WaMYqVPjODgKMbWhVwnBRGA'
consumer_secret='Z5xMhSrj4P1zerBuFKjAUkyBvhGeypmgRnZZ5ynTlhUlaAbx8H'
access_token='313642562-xhZu0SdkXFWjIzLf4poaTZe9J8TPDyDYsCjowEvI'
access_token_secret='kcW1DmYcp4EhIjX7v0v15U8l2hYDtPjfr24Mah5e7OTxo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


palabras=['hola','gato','nombre','tonto','abril','daniel','sol','javiera','dos','diez']

correcto=0;
seleccion=[]
for x in xrange(0,10):
	for tweet in tweepy.Cursor(api.search,q=palabras[x],count=1,result_type="recent",include_entities=True,lang="es").items(1):
		frase=str((tweet.text)).split()
		for palabra in frase:
			if len(palabra)>=4:
				for letra in palabra:
					if letra.lower()>='a'and letra.lower()<='z':
						seleccion=seleccion+[palabra]
						correcto=1
					else:
						correcto=0
						break
			else:
				correcto=0
			if correcto:
				print palabra
				correcto=0

			



