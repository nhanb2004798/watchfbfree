#Bai45
'''
import socket
print("Ten may tinh cuc o la:",socket.gethostname())
print("Dia chi IP cua www.google.com:",socket.gethostbyname('www.google.com'))
print("Ten may tinh co dia chi 172.18.63.194:",socket.gethostbyaddr("172.18.63.194"))
'''

#Bai46

#Client

'''import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect( ('127.0.0.1', 9999) )

str = "Hello Server Nice to meet you!!"
s.sendall(str.encode('ascii'))

data = s.recv(1024)
print('Nhan tu Server: ', data.decode('ascii'))

s.close

#Server

import socket
#tao socket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#tao dia chi
ss.bind( ("",9999) )

#cho noi ket
ss.listen()
print('=====Dang cho noi ket=====')

while True:
    s,(ip_host,port_host) = ss.accept()
    str = "da nhan host co dia chi: %s\n" %ip_host
    s.sendall(str.encode('ascii'))

    #nhan du lieu tu Client
    data = s.recv(1024)
    print(data.decode('ascii'))

    
#dong socket
s.close'''

#Bai47
#Server
'''import socket
#tao socket
ss = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#tao dia chi
ss.bind(("",9999))
print('===Dang cho noi ket===')


while True:
    data,(ip_host,port_host) = ss.recvfrom(1024)
   
    #gui du lieu den client
    mess = "Xin chao %s da ket noi server" %ip_host
    ss.sendto(mess.encode('ascii'), (ip_host,port_host) )


    #nhan du lieu tu client
    print(data.decode('ascii'))'''

#Client
'''
import socket


#tao socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#gui du lieu cho server
str ='Hello server i send to server'
s.sendto(str.encode('ascii'),('127.0.0.1',9999))


#nhan du lieu tu server
data,(ip,port) = s.recvfrom(1024)
print('Server phan hoi:',data.decode('ascii'))


#dong socket
s.close
'''

#Bai48
#Server
'''
import socket
#tao socket server
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#tao dia chi
ss.bind( ("", 7777) )


#lang nghe noi ket
ss.listen(1)
print('===cho noi ket===')


while True:
    s, (ip_host,port_host) = ss.accept()
    print('co 1 client noi ket ',ip_host)


    while True:
        #nhan du lieu tu client
        data = s.recv(1024).decode('ascii')
        print('du lieu tu client:',data)


        #gui lai du lieu cho client
        if data == '#quit':
            print('dong noi ket')
            break
       
        s.sendall(data.encode('ascii'))
   
    #dong noi ket
    s.close()
'''

#Client
'''
import socket
#tao socket client
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#noi ket server
s.connect(('127.0.0.1',7777))




while True:
    #gui du lieu den server
    str = input('nhap du lieu tu ban phim:')
    s.sendall(str.encode('ascii'))
    if (str == '#quit'):
        break


    #nhan du lieu tu server
    data = s.recv(1024)
    print('Server phan hoi:',data.decode('ascii'))


#dong socket
s.close()
'''

#Bai49
#Server
'''import socket
import threading
#tao socket
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#tao dia chi
ss.bind(("",7777))

#lang nghe noi ket
ss.listen(1)
print('===cho noi ket===')

def handle_client(s,a,p):
    print('co 1 client noi ket '+a+' cong '+str(p))
    while True:
        #nhan du lieu tu client
        data = s.recv(1024).decode('ascii')
        print('du lieu tu client:',data)

        #gui lai du lieu cho client
        s.sendall(data.encode('ascii'))
        if data == '#quit':
            print('dong noi ket')
            break
    #dong noi ket
    s.close()

while True:
    s,(a,p) = ss.accept()
    t = threading.Thread(target=handle_client,args=(s,a,p))
    t.start()


#Client

import socket
#tao socket client
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#noi ket server
s.connect(('127.0.0.1',7777))

while True:
    #gui du lieu den server
    str = input('nhap du lieu tu ban phim:')
    s.sendall(str.encode('ascii'))

    #nhan du lieu tu server
    data = s.recv(1024)
    print('Server phan hoi:',data.decode('ascii'))
    if(data.decode('ascii') == '#quit'):
        break

#dong socket
s.close()'''

#Bai50
'''Viết chương trình Chat server lắng nghe tại cổng 8888 và chấp nhận phục vụ nhiều client nối kết cùng thời điểm để chat. Khi nhận chuỗi #quit thì Chat server đóng kết nối với client. Dùng chương trình telnet để kiểm tra chat server.

#Server

import socket
import threading
#tao socket
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#tao dia chi
ss.bind(("",8888))

#lang nghe noi ket
ss.listen(1)
print('===cho noi ket===')

def handle_client(s,a,p):
    print('co 1 client noi ket '+a+' cong '+str(p))
    while True:
        #nhan du lieu tu client
        data = s.recv(1024).decode('ascii')
        print('du lieu tu client:',data)

        #gui lai du lieu cho client
        s.sendall(data.encode('ascii'))
        if data == '#quit':
            print('dong noi ket')
            break
    #dong noi ket
    s.close()

while True:
    s,(a,p) = ss.accept()
    t = threading.Thread(target=handle_client,args=(s,a,p))
    t.start()



#Client

import socket
#tao socket client
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#noi ket server

s.connect(('127.0.0.1', 8888))

while True:
    #gui du lieu den server
    str = input('nhap du lieu tu ban phim:')
    s.sendall(str.encode('ascii'))

    #nhan du lieu tu server
    data = s.recv(1024)
    print('Server phan hoi:',data.decode('ascii'))
    if(data.decode('ascii') == '#quit'):
        break

#dong socket
s.close()'''


 Viết chương trình Chat client

#server
import socket
import threading
#tao socket
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#tao dia chi
ss.bind(("",8888))

#lang nghe noi ket
ss.listen(1)
print('===cho noi ket===')

def handle_client(s,a,p):
 
    while True:
        #nhan du lieu tu client
        data = s.recv(1024).decode('ascii')
        print('du lieu tu client:',data)

        #gui lai du lieu cho client
        s.sendall(data.encode('ascii'))
        if data == '#quit':
            print('dong noi ket')
            break
    #dong noi ket
    s.close()

while True:
    s,(a,p) = ss.accept()
    t = threading.Thread(target=handle_client,args=(s,a,p))
    t.start()




#client
import socket
#tao socket client
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#noi ket server

s.connect(('127.0.0.1', 8888))

while True:

    #gui du lieu den server
    str = input('nhap du lieu tu ban phim:')
    s.sendall(str.encode('ascii'))

    #nhan du lieu tu server
    data = s.recv(1024)
    print('Server phan hoi:',data.decode('ascii'))
    if(data.decode('ascii') == '#quit'):
        break
        
#dong socket
s.close()

