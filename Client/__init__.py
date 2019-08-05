import json
from urllib import urlencode, urlopen


class Client:
	@staticmethod
	def checkWord(word):
		url = 'https://speller.yandex.net/services/spellservice.json/checkText?{word}'.format(
			word=urlencode({'text': word})
		)
		response = urlopen(url).read()
		return json.loads(response)

	@staticmethod
	def checkSome(some):
		return
