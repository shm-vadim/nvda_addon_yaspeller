import api
from logHandler import log


class WordManipulator:
	@staticmethod
	def getCurrentWord():
		text = WordManipulator.getCurrentText()
		if text is None:
			return None
		log.info(text)
		return text

	@staticmethod
	def replaceWord(before, after):
		log.info('Before: {before}, after: {after}'.format(before=before, after=after))

	@staticmethod
	def getCurrentText():
		log.info(api.getFocusObject().TextInfo())
		return api.getFocusObject().value
