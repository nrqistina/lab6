import socket
import time
import colorama
from colorama import Fore,Style

clientSocket = socket.socket()

host = '192.168.43.30'
port = 8888

clientSocket.connect((host,port))

print('\nConnecting to ', host, '....')

time.sleep(1)

response = clientSocket.recv(1024)
print(response.decode('utf-8'))
colorama.init()
while True:
	print(Fore.CYAN + Style.BRIGHT)
	print('\nOnline Calculator')
	print('1. Logarithm')
	print('2. Square Root')
	print('3. Exponential')
	print('4. Multiplication')
	print('5. Division')
	print('6. Exit')
	choice = input('\nChoose the Number : ')

	clientSocket.send(choice.encode('utf-8'))

	if int(choice) == 1:
		num = input('\nEnter a number to Logarithm : ')
		clientSocket.send(num.encode('utf-8'))
		answer = clientSocket.recv(1024)
		print(Fore.GREEN + 'Answer for Logarithm ',num,':',answer.decode('utf-8'))
	elif int(choice) == 2:
		num = input('\nEnter a number to Square Root : ')
		clientSocket.send(num.encode('utf-8'))
		answer = clientSocket.recv(1024)
		print(Fore.GREEN + 'Answer for Square Root ',num,':',answer.decode('utf-8'))
	elif int(choice) == 3:
		num = input('\nEnter a number to Exponential : ')
		clientSocket.send(num.encode('utf-8'))
		answer = clientSocket.recv(1024)
		print(Fore.GREEN + 'Answer for Exponential ',num,':',answer.decode('utf-8'))
	elif int(choice) == 4:
		num = input('\nEnter first number : ')
		num2 = input('\nEnter second number : ')
		clientSocket.send(num.encode('utf-8'))
		clientSocket.send(num2.encode('utf-8'))
		answer = clientSocket.recv(1024)
		print(Fore.GREEN + 'Answer for Multiplication ', num, 'x', num2, ':', answer.decode('utf-8'))
	elif int(choice) == 5:
		num = input('\nEnter first number : ')
		num2 = input('\nEnter second number : ')
		if(int(num2) == 0):
			print(Fore.RED + Style.BRIGHT + 'Second number cannot be 0 for division.')
			print(Fore.CYAN)
			num2 = input('Enter another second number : ')
		clientSocket.send(num.encode('utf-8'))
		clientSocket.send(num2.encode('utf-8'))
		answer = clientSocket.recv(1024)
		print(Fore.GREEN + 'Answer for Division ', num, '/', num2, ':', answer.decode('utf-8'))
	else:
		clientSocket.send(choice.encode('utf-8'))
		print('\nThank You!\n')
		clientSocket.close()
		False
		break
clientSocket.close()
