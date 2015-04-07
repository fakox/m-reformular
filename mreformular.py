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
contador=0
cambiador=0
t_inicio2=int(time.time())
t_inicio=int(time.time())	
#codigo principal
while(True):	
	t_actual=int(time.time())
	while (t_actual-t_inicio<10):
	 	
	 	cantidad_lineas=0
	 	archivo=open('lol.txt')
	 	for linea in archivo:
	 		cantidad_lineas=cantidad_lineas+1
	 	#print cantidad_lineas
	 	x=randint(0,cantidad_lineas-1)
	 	archivo.close()

	 	contador_x=0
	 	archivo=open('lol.txt')
	 	for linea in archivo:
	 		if contador_x==x:
	 			linea_sel=linea.split(':')
	 			break
	 		else:
	 			contador_x=contador_x+1
	 	#print 'linea seleccionada:  ' ,linea_sel

		listo=0
		while(listo==0):
			y=randint(0,len(linea_sel)-1)
			palabra_sel=linea_sel[y]
			if palabra_sel.lower()>='a'and palabra_sel.lower()<='z':
				listo=1
			else:
				listo=0
		print 'modismo seleccionado:  ',palabra_sel

		for tweet in tweepy.Cursor(api.search,q=palabra_sel,count=1,result_type="recent",include_entities=True,lang="es").items(1):
	  	 	frase=str((tweet.text)).split()
	  	 	for palabra in frase:
	  	 		if len(palabra)>=2:
	  	 			for letra in palabra:
	  	 				if letra.lower()>='a'and letra.lower()<='z':
	  						seleccion=seleccion+[palabra]
	  					else:
	  						break
	  	t_actual=time.time()
	t_inicio=int(time.time())

	z1=randint(0,len(seleccion)-1)
	z2=randint(0,len(seleccion)-1)
	palabra_encontrada1=seleccion[z1]
	palabra_encontrada2=seleccion[z2]
	print 'palabra seleccionada1:  ',palabra_encontrada1
	print 'palabra seleccionada2:  ',palabra_encontrada2
	
	t_actual2=int(time.time())
	
	if t_actual2-t_inicio2<120:
		cambiador=cambiador
	else:
		cambiador=not(cambiador)
		t_inicio2=int(time.time())
	if cambiador:
		conectores='lol2.txt'
	else:
		conectores='lol3.txt'
	conector=open(conectores)
	cantidad_lineas=0
	for linea in conector:
	 		cantidad_lineas=cantidad_lineas+1
	x=randint(0,cantidad_lineas-1)
	conector.close()

	contador_x=0
	conector=open(conectores)
	for linea in conector:
		if contador_x==x:
			linea_sel=linea.split(':')
			break
		else:
			contador_x=contador_x+1
	listo=0
	while(listo==0):
		y=randint(0,len(linea_sel)-1)
		conector_obtenido=linea_sel[y]
		if conector_obtenido.lower()>='a'and conector_obtenido.lower()<='z':
			listo=1
		else:
			listo=0
	print palabra_encontrada1 ,conector_obtenido,palabra_encontrada2
	conector.close()