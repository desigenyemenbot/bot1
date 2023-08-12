import requests ,telebot
from mtranslate import translate
from ZaidPP import Zaid
bot = telebot.TeleBot('6065811922:AAEuVw55yYr70vckP4fElw4UcePyR0UDm6A')
@bot.message_handler(commands=['start'])
def start(message):
	name=message.from_user.first_name
	id = str(message.from_user.id)
	user = message.from_user.username
	op = Zaid.store_open('sarch')
	if id in op :
		pass
	else:
		ad = Zaid.store_add(f'sarch:{name} > {id} > @{user}')
	bot.send_message(message.chat.id,text=f'''مرحبا بك انا هنا لمساعدتك ايها المصمم 🎨
	فقط قم بإرسال اسم الصور التي تريدني ان اجلبها لك
مبرمج البوت : THE NEXT BOSS 
INSTA : @V_6PX ''')
@bot.message_handler(func=lambda m:True)
def start(Ali):
	try:
		sarch=translate(Ali.text, 'en', 'ar')
		headers = {
	    'authority': 'sp.cdnpk.net',
	    'accept': '*/*',
	    'accept-language': 'ar-YE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'origin': 'https://www.freepik.com',
	    'referer': 'https://www.freepik.com/search?format=search&query=Cars',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Linux"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
	    'x-product': 'SearchAppFP/1.0',
	}
		response = requests.get(
	    f'https://sp.cdnpk.net/Rest/Media/1/ExpressSearch/Files?search_parameters[limit]=40&locale=en_US&page=0&product=freepik-js-1&search_parameters[filters][content_type:vector]=1&search_parameters[filters][content_type:photo]=1&search_parameters[words]={sarch}',
	    headers=headers,
	).json()
		s=0
		while s<10:
			s+=1
			image=((response['files'][s]['thumbnail_240_url']))
			bot.send_photo(Ali.chat.id,image,f'GETED BY : THE NEXT BOSS')
	except Exception as e:
		print(e)
		bot.send_message(Ali.chat.id,text=f'''عذرا حدث خطأ اعد ارسال ماتوده مع تغيير النص''')
bot.polling(True)