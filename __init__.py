# Version announcement plugin for NVDA
# Developer guide example 2

import json
import globalPluginHandler
from scriptHandler import script
from Client import Client
import wx, gui, ui
from Dialog.ChangeWordDialog import ChangeWordDialog
from WordManipulator import Editor


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@script(gesture="kb:alt+w")
	def script_checkWord(self, obj):
		editor=Editor()
		word = editor.getCurrentWord()
		if word is None:
			ui.message('There is no text here.')
			return

		errors = Client.checkWord(word)
		if errors is None:
			ui.message('There is an error in making request.')
			return

		if 0 == len(errors):
			ui.message('All right.')
			return

		for words in errors:
			self.showDialog(word, words['s'], editor)

	def showDialog(self, word, variants, editor):
		def onChoose(after):
			editor.replaceWord(word, after)
		gui.mainFrame._popupSettingsDialog(ChangeWordDialog, words=variants, onChoose=onChoose)
