import requests as req
from bs4 import BeautifulSoup as bs

import telebot
import os
import random
import requests as req
from bs4 import BeautifulSoup as bs

BOT_KEY = ''
BOT_CHAVE = ''

#os.environ["BOT_CHAVE"] = "16"

if os.environ.get('BOT_KEY', '') != '':
	BOT_KEY = os.environ['BOT_KEY']


chaves=BOT_KEY.split(";")







class GetFinace:
	def __init__(self, tag):
		self.tag = tag['tag']
		self.valor= tag['valor']
		self.qtd=tag['qtd']
		self.price=0
		self.lucro=0
		self.lucro_acao=0
		self.get()
	def get(self):
		try:
			url='https://www.google.com/finance/quote/'+self.tag+':BVMF'

			bss=req.get(url)
			html=bs(bss.text,'html.parser')
			self.price=html.find_all("div", {"class": "YMlKec fxKbKc"})
			self.price=self.price[0].text[2:]

			self.price=float(self.price)


			self.lucro_acao=self.price - self.valor
			self.lucro=self.lucro_acao*self.qtd


			print ('---- '+self.tag+' ----')
			print (' preço -- '+str(self.price))
			print()
		except:
			pass
tags=[

{'tag':"bmgb4",'qtd':1,'valor':4.49},
{'tag':"bbrk3",'qtd':1,'valor':1.85},
{'tag':"nasd11",'qtd':1,'valor':10.97},
{'tag':"oibr3",'qtd':27,'valor':1.10},
{'tag':"cmin3",'qtd':2,'valor':5.98},
]
gets=[]
texto='``` \n'
for i in tags:
	gets.append(GetFinace(i))

total=0
for i in gets:
	texto+='-------'+i.tag+'-------'+'\n'
	texto+=' Qtd -> '+str(i.qtd)+'\n'
	texto+=' V/C -> '+str("{:.2f}".format(i.valor))+'\n'
	texto+=' Prc -> '+str("{:.2f}".format(i.price))+'\n'
	texto+=' L/A -> '+str("{:.2f}".format(i.lucro_acao))+'\n'
	texto+=' Lcr -> '+str("{:.2f}".format(i.lucro))+'\n\n'

	total+=i.lucro

	#'   -   '+str("{:.2f}".format(i.price))+'   -   '+str("{:.2f}".format(i.lucro_acao))+'   -   '+str("{:.2f}".format(i.lucro))+"\n"

texto+='Lucro -> '+str("{:.2f}".format(total))+'\n'
texto+=' ``` '
bot = telebot.TeleBot(chaves[0])




for i in chaves[1:]:
	bot.send_message(i, text=texto, parse_mode= 'Markdown')
