# Royce Pope
# Feb 28 2014
# Socket Client

import socket, pickle, sys

HOST = 'localhost'
PORT = 12354
#USR = input("Username?: \n>>")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#data = str(input("MESSAGE:\n>>"))

if __name__ == "__main__":
   # while True:
    #data = s.recv(1024)
    #data = pickle.loads(data)
    #print (data)
    data = 'awesome string happenings'
    print('sending ', data, 'to server')
    data = pickle.dumps(data)
    s.sendall(data)
    #x, y = "50", "100"
    #print (data)
    #data = str.encode(message)
    #print ("data: %r" % data)

    #result = s.recv(1024)
    #print (result)
    while True:
        data = s.recv(1024)
    s.close()
    
#while True:
    
#    x, y = "50", 100
#    message = input("MESSAGE:\n>>")
    #message = USR + ': ' + message
#    message = str.encode(message)   
#    s.sendall(message)
#    sendX = str.encode(x)
#    s.sendall(sendX)
#    data = s.recv(1024)
#    if data:
 #       data = data.decode(encoding = 'UTF-8')
 #       print('>>' + data)
 #   else:
 #       print("no new messages")
        
        
#s.close()
