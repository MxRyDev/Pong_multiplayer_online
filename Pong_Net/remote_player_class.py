from threading import Thread
import socket, pickle

HOST = 'mxrydev.com'
PORT = 12354

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))



class Remote_player():
    def __init__(self):
        self.x=0
        self.y=0
        self.recv_data = []
        self.send_data = []
        
        listen_thread = Thread(target = self.listen)
        listen_thread.start()
        
    def listen(self):
        while True:
            data = s.recv(1024)
            XandY = pickle.loads(data)
            self.x, self.y = XandY[0], XandY[1]
        # grab 2 item list and update self.x and self.y constantly
    
    def speak(self, posX, posY):
        local_pos = [posX, posY]
        data = pickle.dumps(local_pos)
        s.sendall(data)
        
    # send 2 item list of local player pos
    # needs x and y each time
    