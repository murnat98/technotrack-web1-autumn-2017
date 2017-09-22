# -*- coding: utf-8 -*-
import socket
import os

def http_parser(request):
    m = request.split("\n")#Разбиваем запрос по сторкам и помещаем каждую строку в массив
    res = []
    for str in m:
        res.append(str.split(" "))
    method = res[0][0]
    url = res[0][1]
    protocol = res[0][2]
    res = res[1:]
    #print res
    header = dict()
    for str in res:
        header[str[0].rstrip(":")] = " ".join(str[1:])	
    return method, url, protocol, header


def get_response(request):
	method, url, protocol, header = http_parser(request)
	if url == "/":
		return "Hello mister!\nYou are: " + header["User-Agent"] 
	elif url == "/test/":
		return request
	elif url.split("/")[1] == "media":
		if url == "/media/":
			return str(os.listdir("files"))
		else:
			try:
				m = url.split("/")
				m[1] = "files"
				res = "/".join(m)
				file = open("."+res, 'r')
			except IOError:
				return "File not found"
			return file.read()
	else:
		return "Page not found"
		


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #Связываем сокет с хостом и портом
server_socket.listen(10)  #Указываем максимальную очередь при подключении

print 'Started'

while True:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #Выводим подключенного пользователя
        request_string = client_socket.recv(2048)  #Считываем данные с сокета до 2048 байт
        client_socket.send(get_response(request_string))  #Отправляем ответ из функции
        client_socket.close()
    except KeyboardInterrupt:  #Обработка прерывания процесса сервера
        print 'Stopped'
        server_socket.close()  #Закрытие сокета
        exit()
