from threading import Thread
import socket, pickle,

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 12354))

client_list = []
max_clients = 2

class Client():
    def __init__(self, conn = ''):
        
        self.conn = conn
        # add to global clients list
        client_list.append(self)
        # create thread
        self.client_thread = Thread(target = self.process_messages)
        
        
        
    def process_messages(self):
        while True:
            data = self.conn.recv(1024)
            # send to all in client_list except self
            data = pickle.loads(data)
            print ("Sending Data: ", data)
            data = pickle.dumps(data)
            for client in client_list:
                #if client != self:
                client.conn.sendall(data)
            data = ""
  
def connection_manager():
    
    while len(client_list) < max_clients:
        print('waiting for connections...')
        s.listen(1)
        conn, addr = s.accept()
        # create client class w/ conn
        print ("Connected by: ", addr, "\n\n")
        x = Client(conn)
        print (client_list)
    print ("Max clients reached")
    print ("No longer listening..")
    data = (['go', 'go'])
    data = pickle.dumps(data)
    s.sendall(data)
    print('beginning game')
    for client in client_list:
        self.client_thread.start()
    print('started client threads and sent "go" message')
    

accept_connections_thread = Thread(target = connection_manager)
accept_connections_thread.start()

