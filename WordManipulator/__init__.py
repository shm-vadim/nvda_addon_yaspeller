import api, textInfos
from logHandler import log


class WordManipulator:
	@staticmethod
	def getCurrentWord():
		object = api.getCaretObject()
		textInfo = object.makeTextInfo(textInfos.POSITION_CARET)
		textInfo.expand(textInfos.UNIT_WORD)
		text = textInfo.text
		log.info(text)
		return text

	@staticmethod
	def replaceWord(before, after):
		log.info(
			'Before: {before}, after: {after}'
				.format(before=before.encode('utf8'), after=after.encode('utf8'))
		)
