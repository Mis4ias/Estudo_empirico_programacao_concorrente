import csv
import requests
import time
import statistics
import threading
url = "https://api.adviceslip.com/advice"

qtd_requisi=[10,50,100,150,200,250,300]

def requisicoes():
		response = requests.request("GET", url)
		json=response.json()
		print(json['slip']['advice'])	

for i in qtd_requisi:
	f = open('requisicoes_concorrente'+str(i)+'.csv', 'w', newline='', encoding='utf-8')
	w = csv.writer(f)
	time_vec=[]
	for j in range(0,20):
		for k in range(0,i):
			inicio = time.time()
			threading.Thread(target=requisicoes).start()
			fim = time.time()	
			time_vec.append((fim-inicio)/100)
			
		print(time_vec)
		time.sleep(30)
		w.writerow(time_vec)
		time_vec=[]
	
	f.close()
	
