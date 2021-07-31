import telebot
import os
import random





frases=["Se a vida te der limões, faça um suco de laranja. 🍊",
'O senso comum é o menos comum de todos os sensos.',
'De todos os círculos que fiz, você é o meu maior ângulo.',
'Aqueles que riem por último sempre pensam mais devagar. 🤔',
'Atualmente, os psiquiatras têm cobrado preços de doido. 🤪',
'Entre as palavras mais profundas do mundo, existe o subsolo.',
'Um pessimista é um otimista com experiência.',
'O mais importante não é ganhar. É evitar perder ou empatar. 💯',
'Não leve a vida tão a sério, você não sairá vivo dela. 😉',
'Eu não poderia discordar menos de você.',
'Saco vazio não pára em pé, por isso, continuo deitado.',
'Ser ignorante é fácil, ser burro leva bastante tempo. 💤',
'Se a montanha for até você, corra, porque ela está desmoronando.',
'Existem batalhas que só se ganham perdendo.',
'Que Deus me dê paciência, porque se Ele me der força, eu mato.',
'Na vida, existem muitas máscaras para poucos rostos. 🎭',
'Se o trabalho duro dá frutos, que deixem as árvores trabalharem. 🎋🍎',
'Não existe forma mais segura de se atrasar, do que ter muito tempo para se preparar.',
'Amadurecer é estar triste e não anunciar no Twitter. 😜',
'O casamento é a principal razão de qualquer divórcio.',
'Morro de raiva quando falam no momento que estou interrompendo.',
'Se você não quer respostas sarcásticas, não faça perguntas inteligentes. 😉',
'Eternize este belo momento por algumas horas.',
'O álcool não soluciona nenhum problema, nem a água.',
'Por favor, não me interrompa enquanto estou te ignorando. 😜',
'Prometo te pedir em noivado no próximo dia 30 de fevereiro.',
'Por um lado eu gosto, por outro, também. 🤔',
'Graças a Deus que sou ateu. 🙏🏻',
'Preciso ir ao oftalmologista, mas não consigo enxergar o momento ideal.',
'A sabedoria é uma vila de dois gumes.',
'Vejo que a inteligência te persegue, mas você segue correndo dela. 🏃‍♂️',
'O trem da alegria só me traz tristezas. 😭',
'Se você pretende cometer erros, que sejam novos.',
'Você tem a orelha de Van Gogh para música.',
'Defenda a ecologia, renove as suas emoções.',
'Se um dia eu for preso por baixar músicas de graça, por favor, separem as celas por gêneros musicais. 🙏🏻',
'Existem ocasiões que eu necessito muito de você e da sua ausência.',
'Não desista dos seus sonhos, continue dormindo.',
'Quem com ferro fere, sem ferro será ferreado.',
'Me encontro em um aeroporto, aguardando o barco da felicidade. 🚣‍♂️',
'O silêncio é o suspiro de um grito calado. 😱',
'Um dia sem sol é como uma noite sem tarde.',
'Existem passados tão belos que merecem um futuro do presente.',
'Dizem que é ofensivo falar com a boca cheia. É por isso que prefiro as pessoas com a cabeça vazia. 🤯',
'Se um pato perde a pata ele fica manco ou viúvo? 🦆',
'Se as pessoas vieram dos macacos, por que ainda existem macacos? 🐒',
'A maior ironia nas livrarias são os livros de “autoajuda”.',
'A inteligência sempre vem das mentes mais ignorantes.',
'Chocolate pode não curar os seus problemas, mas uma maçã também não. 🍫 😛',
'Se o leite vem em caixa, porque as vacas não voam?',
'Pedro: Eu gosto das pessoas originais e criativas.',
'Joãozinho: Eu digo o mesmo.',
'Já pensou que absolutamente todas as pessoas sempre falam da boca pra fora? 🤔',
'Toda regra tem exceção.',
'Subi no pé de manga pra apanhar jabuticaba, como eu não sabia nadar roubaram minha bicicleta.',
'O importante é o que importa.',
'A Terra é um dos planetas mais conhecidos no mundo.',
'Qual é o diminutivo de golfinho?',

]
BOT_KEY = ''
BOT_CHAVE = ''

#os.environ["BOT_CHAVE"] = "16"

if os.environ.get('BOT_KEY', '') != '':
	BOT_KEY = os.environ['BOT_KEY']
if os.environ.get('BOT_CHAVE', '') != '':
	BOT_CHAVE = os.environ['BOT_CHAVE']

chaves=BOT_KEY.split(";")

bot = telebot.TeleBot(chaves[0])



if(BOT_CHAVE=='0'):
	print("ok")
	for i in chaves[1:]:
		bot.send_message(i, text="Frase Aleatória.\n\n")
	os.environ["BOT_CHAVE"] = "1"
elif(BOT_CHAVE=='1'):
	os.environ["BOT_CHAVE"] = "0"
	for i in chaves[1:]:
		bot.send_message(i, text="funfo\n\n")

	print(BOT_CHAVE)

enviar=frases[random.randint(0,len(frases)-1)]
bot = telebot.TeleBot(chaves[0])
for i in chaves[1:]:
	bot.send_message(i, text="Frase Aleatória.\n\n"+enviar)