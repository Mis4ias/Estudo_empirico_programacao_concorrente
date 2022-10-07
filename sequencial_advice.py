import csv
import requests
import time
import statistics
import numpy as np
url = "https://api.adviceslip.com/advice"

qtd_requisi=[10,50,100,150,200,250,300]


for i in qtd_requisi:
	f = open('requisicoes_sequencial'+str(i)+'.csv', 'w', newline='', encoding='utf-8')
	w = csv.writer(f)
	time_vec=[]
	for j in range(0,20):
		for k in range(0,i):
			print(str(j)+' de 20 de '+str(i)+"requisicoes")
			inicio = time.time()
			response = requests.request("GET", url)
			fim = time.time()	
			time_vec.append((fim-inicio)/100)
			json=response.json()
			print(json['slip']['advice'])	
			print(time_vec)
		w.writerow(time_vec)
		time_vec=[]
	f.close()
