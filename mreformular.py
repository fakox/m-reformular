# -*- encoding: utf-8 -*-

import tweepy
import sys
import urllib3.contrib.pyopenssl
import time
from random import randint

urllib3.contrib.pyopenssl.inject_into_urllib3()
reload(sys)
sys.setdefaultencoding("utf-8")

pancho_consumer_key='M5WaMYqVPjODgKMbWhVwnBRGA'
pancho_consumer_secret='Z5xMhSrj4P1zerBuFKjAUkyBvhGeypmgRnZZ5ynTlhUlaAbx8H'
pancho_access_token='313642562-xhZu0SdkXFWjIzLf4poaTZe9J8TPDyDYsCjowEvI'
pancho_access_token_secret='kcW1DmYcp4EhIjX7v0v15U8l2hYDtPjfr24Mah5e7OTxo'

maquina_consumer_key='M5WaMYqVPjODgKMbWhVwnBRGA'
maquina_consumer_secret='Z5xMhSrj4P1zerBuFKjAUkyBvhGeypmgRnZZ5ynTlhUlaAbx8H'
maquina_access_token='313642562-xhZu0SdkXFWjIzLf4poaTZe9J8TPDyDYsCjowEvI'
maquina_access_token_secret='kcW1DmYcp4EhIjX7v0v15U8l2hYDtPjfr24Mah5e7OTxo'

auth = tweepy.OAuthHandler(pancho_consumer_key,pancho_consumer_secret)
auth.set_access_token(pancho_access_token, pancho_access_token_secret)

api = tweepy.API(auth)

correcto=0;
seleccion=[]

t_inicio=int(time.time())
t_actual=int(time.time())
contador=0

#codigo principal
while (t_actual-t_inicio<30):
 	cantidad_lineas=0
 	archivo=open('lol.txt')
 	for linea in archivo:
 		cantidad_lineas=cantidad_lineas+1
 		#print linea.split(':')
 	#print cantidad_lineas
 	
 	x=randint(0,cantidad_lineas-1)
 	#print x
 	archivo.close()
 	contador_x=0
 	
 	archivo=open('lol.txt')
 	for linea in archivo:
 		if contador_x==x:
 			linea_sel=linea.split(':')
 			break
 		else:
 			contador_x=contador_x+1
 	print linea_sel
	
	listo=0
	while(listo==0):
		y=randint(0,len(linea_sel)-1)
		palabra_sel=linea_sel[y]
		if palabra_sel.lower()>='a'and palabra_sel.lower()<='z':
			listo=1
		else:
			listo=0
	
	print 'palabra seleccionada:  ' ,palabra_sel, y 

	for tweet in tweepy.Cursor(api.search,q=palabra_sel,count=1,result_type="recent",include_entities=True,lang="es").items(1):
  	 	frase=str((tweet.text)).split()
  	 	#print frase
  	 	for palabra in frase:
  	 		#print len (palabra)
  	 		if len(palabra)>=2:
  	 			for letra in palabra:
  	 				if letra.lower()>='a'and letra.lower()<='z':
  						#seleccion=seleccion+[palabra]
  	 					correcto=1
  	 				else:
  	 					correcto=0
  	 					break
  	 		else:
  	 			correcto=0
  	 		if correcto:
  	 			print palabra
  	 			correcto=0
	 			#contador+=1
  	t_actual=time.time()
	#print contador