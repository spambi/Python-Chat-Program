import socket
import wx
import threading
import time

username = 'spambi'
termDbase = []
msgDbase = []

class Client():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def __init__(self, IP, PORT, GUI):
		self.IP = IP
		self.PORT = PORT
		self.GUI = GUI
		BF_SIZE = 2048


	def connServ(self):
		self.s.connect((self.IP, self.PORT))
		self.GUI.msgHistory.AppendText('Successfully connected to: {}:{}'.format(self.IP, self.PORT))
		termDbase.append('Successfully connected to: {}:{}'.format(self.IP, self.PORT))
		termDbase.append(len(termDbase) + 1)

	def msgServ(self, msg):
		self.s.sendall(msg)
		print 'sent {} to {}:{}'.format(msg, self.IP, self.PORT)



class GUI(wx.Frame):

	mainPanel 	= None
	vbox		= None
	hbox1		= None
	hbox2 		= None	
	msgHistory	= None
	msgWindow	= None
	sendButton	= None

	#IP 			= 'localhost'
	#PORT 		= 1234
	#socketConn 	= Client(self.IP, self.PORT, GUI)


	def __init__(self, *args, **kwargs):
		super(GUI, self).__init__(*args, **kwargs)

		#self.t = threading.Thread(target = self.ui_test, name = threadname)
		#self.t.start()

		# Create new instance of socket


		self.ui_test()

		self.SetSize(640, 320)
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
		msgDbase.append(len(msgDbase) + 1)
		msgDbase.append(msg)
		self.msgHistory.AppendText('{}: {}\n'.format(username, msg))
		self.msgWindow.Clear()
		print msg




if __name__ == '__main__':
	
    APP = wx.App()
    GUI1 = GUI(None, title='testing')
    GUI1.Show()

    clienttest = Client('localhost', 1234, GUI1)
    clienttest.connServ()

    APP.MainLoop()
    

# To fix stuation where I have to reference something that doesn't exist
# maybe like i have to use a variable not in scope to monitor eveything
# something annoying like that I don't reall knwo tbh
# its super late and im about to sleep
# remember to uWu on the haters lul