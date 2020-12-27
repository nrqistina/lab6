import socket
import sys
import time
import errno
import math
import colorama
from colorama import Fore, Style
from multiprocessing import Process


def process_start(clientSocket,addr):
	clientSocket.send(str.encode('Welcome to the Server\n'))
	while True:
		print('\nConnected to ', addr)

		data = clientSocket.recv(1024)
		num = clientSocket.recv(1024)

		if data == b'1':
			print(data.decode('utf-8') + '. Logarithm Process')
			answer = math.log(float(num))
		elif data == b'2':
			print(data.decode('utf-8') + '. Square Root Process')
			answer = math.sqrt(float(num))
		elif data == b'3':
			print(data.decode('utf-8') + '. Exponential Process')
			answer = math.frexp(float(num))
		elif data == b'4':
			num2 = clientSocket.recv(1024)
			print(data.decode('utf-8') + '. Multiplication Process')
			answer = (float(num) * float(num2))
		elif data == b'5':
			num2 = clientSocket.recv(1024)
			print(data.decode('utf-8') + '. Division Process')
			answer = (float(num) / float(num2))
		else:
			print('Connection Ended For ' + str(addr) + '\n')
			False
			break

		convert = str(answer)
		clientSocket.send(convert.encode('utf-8'))
	clientSocket.close()

if __name__ == '__main__':
	host = ''
	port = 8888
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	colorama.init()
	print(Fore.CYAN + Style.BRIGHT)
	serverSocket.bind((host,port))
	print("listening...")
	serverSocket.listen(3)
	try:
		while True:
			try:
				client, addr = serverSocket.accept()
				p = Process(target=process_start, args=(client,addr))
				p.start()
			except socket.error:
				print('got a socket error')
	except Exception as e:
		print('an exception occurred!')
		print(e)
		sys.exit(1)
	finally:
		serverSocket.close()
