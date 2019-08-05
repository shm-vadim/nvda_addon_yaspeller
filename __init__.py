# Version announcement plugin for NVDA
# Developer guide example 2

import json
import globalPluginHandler
from scriptHandler import script
from Client import Client
import wx, gui, ui
from Dialog.ChangeWordDialog import ChangeWordDialog
from WordManipulator import WordManipulator


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@script(gesture="kb:alt+w")
	def script_checkWord(self, obj):
		word = WordManipulator.getCurrentWord()
		if word is None:
			ui.message('There is no text here.')
			return

		data = Client.checkWord(word)
		if 0 == len(data):
			ui.message('All right.')
			return

		for words in data:
			self.showDialog(word, words['s'])

	def showDialog(self, word, variants):
		def onChoose(after):
			WordManipulator.replaceWord(word, after)
		gui.mainFrame._popupSettingsDialog(ChangeWordDialog, words=variants, onChoose=onChoose)
