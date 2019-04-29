import socket
import wx
import threading
import time


class GUI(wx.Frame):

	mainPanel 	= None
	vbox		= None
	hbox1		= None
	hbox2 		= None	
	msgHistory	= None
	msgWindow	= None
	sendButton	= None

	def __init__(self, *args, **kwargs):
		super(GUI, self).__init__(*args, **kwargs)

		#self.t = threading.Thread(target = self.ui_test, name = threadname)
		#self.t.start()

		self.ui_test()

		self.SetSize(1280, 640)
		self.Center()


	def ui_test(self):

		self.mainPanel = wx.Panel(self)

		self.vbox = wx.BoxSizer(wx.VERTICAL)
		# Horizontal Boxes, set name later
		self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		# Text Ctrls
		self.msgHistory = wx.TextCtrl(self.mainPanel, style=wx.TE_READONLY | wx.TE_MULTILINE |
									wx.TE_AUTO_URL)
		self.msgWindow = wx.TextCtrl(self.mainPanel, style=wx.TE_MULTILINE | wx.TE_AUTO_URL )
		# Buttons etc,
		self.sendButton = wx.Button(self.mainPanel, label="Send", size=(50, 39))
		

		self.hbox1.Add(self.msgHistory, proportion=1, flag=wx.EXPAND)
		self.hbox2.Add(self.msgWindow, proportion=1, flag=wx.EXPAND)
		self.hbox2.Add(self.sendButton, flag= wx.EXPAND | wx.RIGHT, border=10)
		self.vbox.Add(self.hbox1, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, border=10)
						
		self.vbox.Add(self.hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP,
                 border=10)

		self.msgWindow.AppendText('im a weeb lol, www.magicalgirls.moe/dance')

		#self.Bind(wx.EVT_BUTTON, self.msgGUI, self.sendButton)
		self.Bind(wx.EVT_BUTTON, lambda evt: self.msgGUI(), self.sendButton)

		self.vbox.Add((-1, 10))

		self.mainPanel.SetSizer(self.vbox)

	def msgGUI(self):
		msg = self.msgWindow.GetValue()
		self.msgHistory.AppendText('{}{}\n'.format(usernamemsg))
		self.msgWindow.Clear()
		print msg


if __name__ == '__main__':
	
    APP = wx.App()
    GUI1 = GUI(None, title='testing')
    GUI1.Show()

    APP.MainLoop()
    