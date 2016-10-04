#--encoding=utf8--
import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(6)
print "[*] listening on %s:%d" % (bind_ip,bind_port)

def handle_client(client_socket):
	#打印客户端发送的内容
	request = client_socket.recv(1024)
	print "[*] Received: %s " % request
	#返还一个数据包
	client_socket.send("ACK!")
	client_socket.close()
	
while True:
	client,addr = server.accept()
	print "[*] Accepted connection from : %s %d" % (addr[0],addr[1])
	
	#挂起客户端thread,handle 数据
	client_handler = threading.Thread(target = handle_client,args = (client,))
	client_handler.start()


