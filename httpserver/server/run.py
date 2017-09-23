# -*- coding: utf-8 -*-
import socket
import os

def http_parser(request):
	#Получаем из строки двумерный массив
    res = []
    for str in request.split("\n"):
        res.append(str.split(" "))
    #Получаем строку запроса
    method = res[0][0]
    url = res[0][1]
    protocol = res[0][2]
    #Получаем заголовки в словаре
    res = res[1:]
    header = dict()
    for str in res:
        header[str[0].rstrip(":")] = " ".join(str[1:])
        	
    return method, url, protocol, header


def get_response(request):
	method, url, protocol, header = http_parser(request)
	body = """<!DOCTYPE html> 
<html>
<head>
	<title>HTTP сервер</title>
	<meta http-equiv="Content-Type" content="text/html" charset="utf-8">
</head>
<body>
	""" #Тело ответа в html
	code = 200 #HTTP код ответа
	status = "OK"
	if url == "/":
		body += "<h3>Hello mister!</h3>" \
				+ "<p>You are: " + header["User-Agent"] + "</p>"
		
	elif url == "/test/":
		body += request.replace("\n", "<br>") #Выводим запрос (Замена "\n" для html)
		
	elif url.split("/")[1] == "media": #Url начинается с /media/
		if url == "/media/": #Получить файлы в папке files
			#Формируем список файлов в директории
			m = os.listdir("files")
			body += "<h3>Files in the media: </h3>\n"
			body += "<ul>\n"
			for f in m:
				body += "<li><a href=" + url + f + ">" \
						+ f \
						+ "</a></li>\n" 
			body += "</ul>"
		else: #Вывести файл
			try:
				#Заменяем /media/ в url на /files/
				m = url.split("/")
				m[1] = "files"
				res = "/".join(m)
				#Пытаемся открыть и вывести файл
				file = open("."+res, 'r')
				body += file.read()
			except IOError: #Файла не существует
				body += "<font color=red size=4>File not found</font>"
				code = 404
				status = "Not Found"
				
	else: #Неверный url
		body += "<font color=red size=4>Page not found</font>"
		code = 404
		status = "Not Found"
	body += "\n</body>\n</html>"
	return protocol, code, status, body
	


def get_http_response(request):
	protocol, code, status, body = get_response(request)
	#Формируем HTTP ответ
	return protocol + " " + str(code) + " " + status + "\n" \
			+ "Content-Type: text/html" + "\n\n" \
			+ body
		
	


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #Связываем сокет с хостом и портом
server_socket.listen(0)  #Указываем максимальную очередь при подключении

print 'Started'

while True:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #Выводим подключенного пользователя
        request_string = client_socket.recv(2048)  #Считываем данные с сокета до 2048 байт
        client_socket.send(get_http_response(request_string))  #Отправляем ответ из функции
        client_socket.close()
    except KeyboardInterrupt:  #Обработка прерывания процесса сервера
        print 'Stopped'
        server_socket.close()  #Закрытие сокета
        exit()
