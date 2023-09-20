'''
import requests
url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)
print(response.json())
###################################################
import requests
url = "https://text-translator2.p.rapidapi.com/translate"
payload = {
	"source_language": "pt",
	"target_language": "en",
	"text": texto
}

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "9e8d643f68msh46e59adc17f295bp1129c9jsn9d14c1674404",
	"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)
response = response.json()
texto_traduzido = response['data']['translatedText']
'''
import requests

def cria_dic():
	for i in range(len(dic['data']['languages'])):
		idioma = dic['data']['languages'][i]['name']
		codigo = dic['data']['languages'][i]['code']
		linguas[idioma] = codigo
	return

linguas = {}

dic = {
	'data': {
		'languages': [
			{
				'code': 'af',
				'name': 'Afrikaans'
			 },
			{'code': 'sq', 'name': 'Albanian'},
			{'code': 'am', 'name': 'Amharic'},
			{'code': 'ar', 'name': 'Arabic'},
			{'code': 'hy', 'name': 'Armenian'},
			{'code': 'az', 'name': 'Azerbaijani'},
			{'code': 'eu', 'name': 'Basque'},
			{'code': 'be', 'name': 'Belarusian'},
			{'code': 'bn', 'name': 'Bengali'},
			{'code': 'bs', 'name': 'Bosnian'},
			{'code': 'bg', 'name': 'Bulgarian'},
			{'code': 'ca', 'name': 'Catalan'},
			{'code': 'ceb', 'name': 'Cebuano'},
			{'code': 'ny', 'name': 'Chichewa'},
			{'code': 'zh-CN', 'name': 'Chinese (Simplified)'},
			{'code': 'zh-TW', 'name': 'Chinese (Traditional)'},
			{'code': 'co', 'name': 'Corsican'},
			{'code': 'hr', 'name': 'Croatian'},
			{'code': 'cs', 'name': 'Czech'},
			{'code': 'da', 'name': 'Danish'},
			{'code': 'nl', 'name': 'Dutch'},
			{'code': 'en', 'name': 'English'},
			{'code': 'eo', 'name': 'Esperanto'},
			{'code': 'et', 'name': 'Estonian'},
			{'code': 'tl', 'name': 'Filipino'},
			{'code': 'fi', 'name': 'Finnish'},
			{'code': 'fr', 'name': 'French'},
			{'code': 'fy', 'name': 'Frisian'},
			{'code': 'gl', 'name': 'Galician'},
			{'code': 'ka', 'name': 'Georgian'},
			{'code': 'de', 'name': 'German'},
			{'code': 'el', 'name': 'Greek'},
			{'code': 'gu', 'name': 'Gujarati'},
			{'code': 'ht', 'name': 'Haitian Creole'},
			{'code': 'ha', 'name': 'Hausa'},
			{'code': 'haw', 'name': 'Hawaiian'},
			{'code': 'iw', 'name': 'Hebrew'},
			{'code': 'hi', 'name': 'Hindi'},
			{'code': 'hmn', 'name': 'Hmong'},
			{'code': 'hu', 'name': 'Hungarian'},
			{'code': 'is', 'name': 'Icelandic'},
			{'code': 'ig', 'name': 'Igbo'},
			{'code': 'id', 'name': 'Indonesian'},
			{'code': 'ga', 'name': 'Irish'},
			{'code': 'it', 'name': 'Italian'},
			{'code': 'ja', 'name': 'Japanese'},
			{'code': 'jw', 'name': 'Javanese'},
			{'code': 'kn', 'name': 'Kannada'},
			{'code': 'kk', 'name': 'Kazakh'},
			{'code': 'km', 'name': 'Khmer'},
			{'code': 'rw', 'name': 'Kinyarwanda'},
			{'code': 'ko', 'name': 'Korean'},
			{'code': 'ku', 'name': 'Kurdish (Kurmanji)'},
			{'code': 'ky', 'name': 'Kyrgyz'},
			{'code': 'lo', 'name': 'Lao'},
			{'code': 'la', 'name': 'Latin'},
			{'code': 'lv', 'name': 'Latvian'},
			{'code': 'lt', 'name': 'Lithuanian'},
			{'code': 'lb', 'name': 'Luxembourgish'},
			{'code': 'mk', 'name': 'Macedonian'},
			{'code': 'mg', 'name': 'Malagasy'},
			{'code': 'ms', 'name': 'Malay'},
			{'code': 'ml', 'name': 'Malayalam'},
			{'code': 'mt', 'name': 'Maltese'},
			{'code': 'mi', 'name': 'Maori'},
			{'code': 'mr', 'name': 'Marathi'},
			{'code': 'mn', 'name': 'Mongolian'},
			{'code': 'my', 'name': 'Myanmar (Burmese)'},
			{'code': 'ne', 'name': 'Nepali'},
			{'code': 'no', 'name': 'Norwegian'},
			{'code': 'or', 'name': 'Odia (Oriya)'},
			{'code': 'ps', 'name': 'Pashto'},
			{'code': 'fa', 'name': 'Persian'},
			{'code': 'pl', 'name': 'Polish'},
			{'code': 'pt', 'name': 'Portuguese'},
			{'code': 'pa', 'name': 'Punjabi'},
			{'code': 'ro', 'name': 'Romanian'},
			{'code': 'ru', 'name': 'Russian'},
			{'code': 'sm', 'name': 'Samoan'},
			{'code': 'gd', 'name': 'Scots Gaelic'},
			{'code': 'sr', 'name': 'Serbian'},
			{'code': 'st', 'name': 'Sesotho'},
			{'code': 'sn', 'name': 'Shona'},
			{'code': 'sd', 'name': 'Sindhi'},
			{'code': 'si', 'name': 'Sinhala'},
			{'code': 'sk', 'name': 'Slovak'},
			{'code': 'sl', 'name': 'Slovenian'},
			{'code': 'so', 'name': 'Somali'},
			{'code': 'es', 'name': 'Spanish'},
			{'code': 'su', 'name': 'Sundanese'},
			{'code': 'sw', 'name': 'Swahili'},
			{'code': 'sv', 'name': 'Swedish'},
			{'code': 'tg', 'name': 'Tajik'},
			{'code': 'ta', 'name': 'Tamil'},
			{'code': 'tt', 'name': 'Tatar'},
			{'code': 'te', 'name': 'Telugu'},
			{'code': 'th', 'name': 'Thai'},
			{'code': 'tr', 'name': 'Turkish'},
			{'code': 'tk', 'name': 'Turkmen'},
			{'code': 'uk', 'name': 'Ukrainian'},
			{'code': 'ur', 'name': 'Urdu'},
			{'code': 'ug', 'name': 'Uyghur'},
			{'code': 'uz', 'name': 'Uzbek'},
			{'code': 'vi', 'name': 'Vietnamese'},
			{'code': 'cy', 'name': 'Welsh'},
			{'code': 'xh', 'name': 'Xhosa'},
			{'code': 'yi', 'name': 'Yiddish'},
			{'code': 'yo', 'name': 'Yoruba'},
			{'code': 'zu', 'name': 'Zulu'},
			{'code': 'he', 'name': 'Hebrew'},
			{'code': 'zh', 'name': 'Chinese (Simplified)'}]}}

cria_dic()
print("Bem vindo ao programa de tradução!")
while True:
	idioma_origem = input("De qual idioma você quer traduzir?")
	idioma_destino = input("Para qual idioma você quer traduzir?")
	frase = input("Digite a frase que quer traduzir\nR:")

	url = "https://text-translator2.p.rapidapi.com/translate"
	payload = {
		"source_language": linguas[idioma_origem],
		"target_language": linguas[idioma_destino],
		"text": frase
	}
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"X-RapidAPI-Key": "9e8d643f68msh46e59adc17f295bp1129c9jsn9d14c1674404",
		"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
	}
	response = requests.post(url, data=payload, headers=headers)
	response = response.json()
	texto_traduzido = response['data']['translatedText']

	print(texto_traduzido)
	pergunta = input("Quer continuar traduzindo?(s/n)")
	if pergunta == "n":
		break
