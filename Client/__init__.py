import json
from urllib import urlencode, urlopen


class Client:
	@staticmethod
	def checkWord(word):
		url = 'https://speller.yandex.net/services/spellservice.json/checkText?{word}'.format(
			word=urlencode({'text': word.encode('utf8')})
		)
		response = urlopen(url)
		if 200 != response.code:
			return None
		errors = response.read()
		return json.loads(errors)
