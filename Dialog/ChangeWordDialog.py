import gui
import wx


class ChangeWordDialog(gui.SettingsDialog):
	title = 'Change the word.'

	def __init__(self, parent, words, onChoose):
		self.words = words
		self.onChoose = onChoose
		super(ChangeWordDialog, self).__init__(parent)

	def makeSettings(self, sizer):
		variantsSizer = wx.BoxSizer()
		self.variantList = wx.Choice(self, choices=self.words)
		variantsSizer.Add(self.variantList)
		sizer.Add(variantsSizer)

	def onOk(self, commandEvent):
		key = self.variantList.GetCurrentSelection()
		self.onChoose(self.variantList.GetString(key))
		return super(ChangeWordDialog, self).onOk(commandEvent)
