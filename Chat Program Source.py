""" ATM creates a way to put in text to a screen
Will change it to a client for the server and hvae the server console based, so it should be ez to implement on this
"""

import socket
import time
import threading
import wx


msgs =  ''
username = 'spambi'
welcome_msg = "Welcome to Pype %s, this is a python based chat program that uses wx and sockets, this very much a WIP\n" % username
msg_dbase = []
serv_socks = []


class Client:
    """ This is what connects to the server, made as a class so multiple clients can run
    """
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT
        self.s = None      
        
    # Each class run thing creates a now socketsket lol
    def connect_to_server(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.IP, self.PORT)) 
        serv_socks.append(self.s)
        print 'Connected to %s' % self.IP

        #new_client = SimpleGUI('newclient', None, title='New Client')
        #APP = wx.App()
        #new_client.Show()
        #APP.MainLoop()

   # def connect_serv_new_client(self):
   #     self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   #     self.s.connect((self.IP, self.PORT)) 
   #     serv_socks.append(self.s)
   #     print 'Connected to %s' % self.IP
#
   #     new_client = SimpleGUI('newclient', None, title='{}:{}'.format(self.IP, self.PORT))
   #     new_client.IP = self.IP
   #     new_client.PORT = self.PORT
   #     APP = wx.App()
   #     new_client.Show()
   #     APP.MainLoop()


    def send_msg(self, msg):
        self.s.sendall(msg)


class SimpleGUI(wx.Frame):
    """ This is the main GUI for PyPe
    """

    def __init__(self, threadname, *args, **kwargs):
        super(SimpleGUI, self).__init__(*args, **kwargs)

        # Create a seperate thread here so multiple clients can be run +-+
        self.t = threading.Thread(target = self.init_ui, name = threadname)
        self.t.start()

        self.init_ui()
        self.SetSize(1280, 640)
        self.Center()

        self.IP = None
        self.PORT = None
        self.serv1 = None


    def init_ui(self):
        """ This is the actual UI
        """

        # Menubar
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        
        fileConnServ = fileMenu.Append(wx.ID_ANY, 'Connect', 'Connect to a new server')
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.closewindow, fileItem)
        
        # This is going to be ugle but it will have to work
        #self.Bind(wx.EVT_MENU, self.serv1.connect_to_server, fileConnServ)

        
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        #  Make a Hojrizontal Sizer
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        #  Make a box that send the text in the textbox to the uneditable text

        #  Make a TextCtrl that had AUTO_URL, MULTILINE and is READONLY
        t_ctrl1 = wx.TextCtrl(panel, style=wx.TE_AUTO_URL | wx.TE_MULTILINE |
                              wx.TE_READONLY)

        t_ctrl1.AppendText(welcome_msg)

        #  Add t_ctrl1 to hbxo1

        hbox1.Add(t_ctrl1, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox1, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND,
                 border=10)

        vbox.Add((-1, 10))

        #  Create a new box
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        #  Create a new TextCtrl and put in some default text in it
        t_ctrl2 = wx.TextCtrl(panel, style=wx.TE_AUTO_URL | wx.TE_MULTILINE)
        t_ctrl2.AppendText('im a weeb lol, www.magicalgirls.moe/dance ')
        hbox2.Add(t_ctrl2, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP,
                 border=10)

        button1 = wx.Button(panel, label='Send', size=(50, 39))
        # Will send text to t_ctrl1 through the send_message_gui func that uses str_con_lst to convert msgs array 
        # into a string
        # Fuck that took too long xD
        #msgs.append(t_ctrl2.GetLineText(1))
        # i dont get lambda
        panel.Bind(wx.EVT_BUTTON, lambda evt: self.send_message_gui(t_ctrl1, t_ctrl2), button1)
        #panel.Bind(wx.EVT_BUTTON, msgs.append(t_ctrl2), button1)
        panel.Bind(wx.EVT_CLOSE, self.closewindow)
        hbox2.Add(button1, flag=wx.EXPAND | wx.RIGHT | wx.DOWN, border=10)

        vbox.Add((-1, 10))

        panel.SetSizer(vbox)


    def send_msg_server(self, msg):
        if self.serv1 == None:
            self.getIpPort(None)
            self.serv1 = Client(self.IP, self.PORT)
            self.serv1.connect_to_server()
            print 'Connected to {} and {}'.format(self.IP, self.PORT)
        else:
            print 'already connected'
            self.serv1.send_msg(msg)

    def send_message_gui(self, txtbox, new_msg):
        """
            This does some shit lmao
        """
        
        msgs = new_msg.GetValue()
        msg_dbase.append(msgs)
        # Pretty ugly, but have to put the % after %s cause it won't work otherwise
        txtbox.AppendText("%s: " % username + msgs + '\n') 
        new_msg.Clear()
        print msgs
        self.send_msg_server(msg_dbase[-1])
        
        
    def getIpPort(self, event):
        IPBox = wx.TextEntryDialog(None, 'What is the IP', 'IP of Server', '127.0.0.1')
        PORTBox = wx.TextEntryDialog(None, 'What is the PORT', 'PORT of Server', '4132')
        if IPBox.ShowModal()==wx.ID_OK:
            self.IP = IPBox.GetValue()
        if PORTBox.ShowModal()==wx.ID_OK:
            self.PORT = int(PORTBox.GetValue())
        

    def closewindow(self, e):
        """
            This destroys the window
        """
        self.Destroy()
    
if __name__ == '__main__':
    APP = wx.App()
    GUI1 = SimpleGUI('mainclient1', None, title='testing')
    GUI1.Show()

    # Connect to a server
    
    APP.MainLoop()
    