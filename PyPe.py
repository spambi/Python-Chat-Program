import socket
import wx
import threading
import time

username = 'spambi'
termDbase = []
msgDbase = []
BF_SIZE = 2048

def sendSvr(socket, msg):
	socket.sendall(msg)

class Client():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	BF_SIZE = 2048

	def __init__(self, IP, PORT, GUI):
		self.IP = IP
		self.PORT = PORT
		self.GUI = GUI


	def connServ(self):
		try:
			self.s.connect((self.IP, self.PORT))
			self.GUI.msgHistory.AppendText('Successfully connected to: {} : {}'.format(self.IP, self.PORT))
			termDbase.append('Successfully connected to: {} : {}'.format(self.IP, self.PORT))
			termDbase.append(len(termDbase) + 1)
			print termDbase

		except:
			self.GUI.msgHistory.AppendText('Could not connect to: {} : {}'.format(self.IP, self.PORT))
			termDbase.append('Could not connect to: {} : {}'.format(self.IP, self.PORT))

		self.s.sendall('lololol')
		welcome_msg = self.s.recv(self.BF_SIZE)
		self.GUI.msgHistory.AppendText(welcome_msg)

		print 'Starting recieve loop'
		termDbase.append('Starting recieve loop')
		recvLoop = threading.Thread(target = self.recvMsg)
		recvLoop.start()
		recvLoop.join()

	def recvMsg(self):
		print 'Started siht lol'
		while True:
			msg = self.s.recv(BF_SIZE)
			print 'Recieved {} from {}'.format(msg, self.IP)
			if msg == "{quit}":
				self.s.close()

		else:
			print 'Recieved {}'.format(msg)
			termDbase.append('Recieved {} from {}'.format(msg, self.IP))
			self.GUI.msgHistory.AppendText('{}\n'.format(msg))

	def msgServ(self, msg):
		self.s.sendall(msg)
		print 'sent {} to {}:{}'.format(msg, self.IP, self.PORT)
		termDbase.append('sent {} to {}:{}'.format(msg, self.IP, self.PORT))


class GUI(wx.Frame):

	mainPanel 	= None
	vbox		= None
	hbox1		= None
	hbox2 		= None	
	msgHistory	= None
	msgWindow	= None
	sendButton	= None
	socket 		= None

	def __init__(self, threadname, *args, **kwargs):
		super(GUI, self).__init__(*args, **kwargs)

		self.clientThread = threading.Thread(target = self.initUI, name = threadname)
		self.clientThread.start()

		self.SetSize(640, 320)
		self.Center()


	def initUI(self):

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

		self.msgWindow.AppendText('im a weeb lol, www.magicalgirls.moe/dance\n')

		self.Bind(wx.EVT_BUTTON, lambda evt: self.msgGUI(), self.sendButton)

		self.vbox.Add((-1, 10))

		self.mainPanel.SetSizer(self.vbox)

	def msgGUI(self):
		msg = self.msgWindow.GetValue()
		if msg == "":
			print 'put somthing in actually diiot'
		else:
			msgDbase.append(len(msgDbase) + 1)
			msgDbase.append(msg)
			termDbase.append('Sent {} to GUI'.format(msg))
			self.msgHistory.AppendText('{}: {}'.format(username, msg))
			self.msgHistory.AppendText('\n')
			self.msgWindow.Clear()
			self.socket.msgServ(msg)
			print msg


if __name__ == '__main__':
	
    APP = wx.App()
    GUI1 = GUI('lol', None, title='testing')
    GUI1.Show()

    clienttest = Client('localhost', 1234, GUI1)

    GUI1.socket = clienttest
    clienttest.connServ()

    clienttest.msgServ('test')

    APP.MainLoop()