# Exercise 1: Change the socket program socket1.py to prompt the user for the
# URL so it can read any web page.
# You can use split('/') to break the URL into its component parts so you can
# extract the host name for the socket connect call. Add error checking using try
# and except to handle the condition where the user enters an improperly formatted
# or non-existent URL.

import socket

url = input("Enter url: ")

try:
    address = url.split('/')
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((address[2],80))
    get_connection = 'GET /' + url[3] + ' HTTP/1.1\r\nHost: ' + address[2] + '\r\n\r\n'
    cmd = get_connection.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

    mysock.close()

except: 
    print("The url is improperly formatted of non-existent!")