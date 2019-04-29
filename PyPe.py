import socket
import wx
import threading
import time




class GUI(wx.Frame):

	mainPanel 	= None
	vbox		= None
	hbox1		= None
	hbox2		= None
	msgHistory	= None
	msgWindow	= None

	def __init__(self, threadname, *args, **kwargs):
		super(GUI, self).__init__(*args, **kwargs)

		self.t = threading.Thread(target = self.ui_test, name = threadname)
		self.t.start()

		self.ui_test()

		self.SetSize(1280, 640)
		self.Center()

	def ui_test(self):

		self.mainPanel = wx.Panel(self, wx.NewIdRef())

		self.vbox = wx.BoxSizer(wx.VERTICAL)
		# Horizontal Boxes, set name later
		self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		# Text Ctrls
		self.msgHistory = wx.TextCtrl(self.mainPanel, style=wx.TE_READONLY | wx.TE_MULTILINE |
									wx.TE_AUTO_URL)
		self.msgWindow = wx.TextCtrl(self.mainPanel, style=wx.TE_MULTILINE | wx.TE_AUTO_URL )
		# Buttons etc,
		#sendButton = wx.Button(self.mainPanel, label="Send", size(50, 39))




		self.hbox1.Add(self.msgHistory, proportions=1, flag=wx.EXPAND)
		self.msgHistory.AppendText('ahahaha')
		self.vbox.Add(self.hbox1, flag=wx.LEFT | wx.RIGHT | 
						wx.EXPAND, border=10)

		self.vbox.Add((-1, 10))

		self.SetSizer(self.vbox)



if __name__ == '__main__':
	
	
    APP = wx.App()
    GUI1 = GUI('gui_test', None, title='testing')
    GUI1.Show()

    #time.sleep(2)
    #GUI1.msgWindow.AppendText('hello')

    APP.MainLoop()
    