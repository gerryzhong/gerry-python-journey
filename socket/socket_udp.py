#--encoding=utf8--
import socket

target_host = "10.95.20.23"
target_port = 80

#建立一个socket对象
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#发送一些数据
client.sendto('aaabbccc',(target_host,target_port))

#接收一些数据
data,addr = client.recvfrom(1024)

print data
