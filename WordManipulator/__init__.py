import api, textInfos, winUser, win32con
from logHandler import log


class Editor:
	def __init__(self):
		self.object = api.getCaretObject()
		self.textInfo = self.object.makeTextInfo(textInfos.POSITION_CARET)
		self.textInfo.expand(textInfos.UNIT_WORD)

	def getCurrentWord(self):
		return self.textInfo.text

	def replaceWord(self, before, after):
		self.textInfo.updateSelection()
		for char in after:
			winUser.sendMessage(self.object.windowHandle, win32con.WM_CHAR, ord(char), 0)
