# -*- coding: utf-8 -*-
import socket
import os
import re


def http_code(code_):
    codes_ = {"code": code_, "status": ""}

    if code_ == 200:
        codes_["status"] = "OK"
    elif code_ == 400:
        codes_["status"] = "Bad request"
    elif code_ == 404:
        codes_["status"] = "Not found"

    return codes_


def define_headers(string):
    lines = string.split("\r\n")[1:]
    headers = dict()

    for line in lines:
        words = line.split(": ")
        if len(words) >= 2:
            headers[words[0]] = words[1]

    return headers


def parse(client_info):
    uri = "/"
    user_agent = ""
    method = ""
    protocol = "HTTP/1.1"

    words = client_info.split(" ")
    method = words[0]

    if len(words) >= 3:
        uri = words[1]
        protocol = words[2].split("\r\n")[0]

    headers = define_headers(client_info)
    if "User-Agent" in headers:
        user_agent = headers["User-Agent"]

    return {"uri": uri, "user_agent": user_agent, "method": method, "protocol": protocol}


def generate_404_page():
    body = "<p>Page not found</p>"
    return body


def generate_media_page():
    body = "<ul>"

    files = os.listdir("../files")
    for file_ in files:
        body += "<li>" + file_ + "</li>"

    body += "</ul>"

    return body


def generate_files_page(url):
    body = ""

    try:
        file_name = url.split("/")[2]
        file_ = open("../files/" + file_name, "r")
        body += file_.read()
        code = 200
    except IOError:
        body = generate_404_page()
        code = 404

    return body, code


def generate_test_page(request):
    body = """<style>
    p
    {
        white-space: pre-wrap;
    }
    </style>
    """
    body += "<p>" + request + "</p>"

    return body


def generate_page(info, request):
    respond = dict()

    code = 200
    uri = info["uri"]
    user_agent = info["user_agent"]
    method = info["method"]
    protocol = info["protocol"]
    body = ""
    html = """<!DOCTYPE html>
    <html>
    <head>
    <title>http сервер</title>
    </head>
    <body>"""

    if method != "GET":
        body = generate_404_page()
        code = 404
    elif uri == "/" or uri == "":
        body = "<p>Hello, mister</p><p>You are: " + user_agent + "</p>"
        code = 200
    elif uri == "/media/" or uri == "/media":
        body = generate_media_page()
        code = 200
    elif re.match("/media/*", uri):
        body, code = generate_files_page(uri)
    elif uri == "/test/" or uri == "/test":
        body = generate_test_page(request)
        code = 200
    else:
        body = generate_404_page()
        code = 404

    html += body
    html += "</body></html>"

    respond.update({"protocol": protocol, "html": html})
    respond.update(http_code(code))

    return respond


content_type = "Content-Type: text/html"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  # устанавливаем хост и номер порта
server_socket.listen(0)  # режим прослушивания

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  # вывод нового подключения
        request_string = client_socket.recv(2048)  # принимаем данные от клиента (макс. 2048)

        user_info = parse(request_string)
        server_info = generate_page(user_info, request_string)

        send = server_info["protocol"] + " " + str(server_info["code"]) + " " + server_info["status"] \
            + "\n" + content_type + "\n\n" + server_info["html"]

        client_socket.send(send)  # отправляем данные клиенту
        client_socket.close()

    except KeyboardInterrupt:  # ручное выключение сервера
        print 'Stopped'

        server_socket.close()  # разрыв соединения

        exit()
