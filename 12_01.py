import socket

while True:
    try:
        url= input("Enter a website: \t")
        url_comp = url.split("/")
        host = url_comp[ len(url_comp) - 1 ] 
        print(host)
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))
    except Exception as e:
        print("Invalid URL, please re-enter.")
        continue
    break

cmd = 'GET /1.1 \r\n\r\n'
mysock.send(cmd.encode())

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()