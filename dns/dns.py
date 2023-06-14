dns_table = [
    ['alice', '192.168.1.10'],
    ['bob', '192.168.1.20'],
    ['charlie', '192.168.1.30']
]

def search_ip_address(name):
    for entry in dns_table:
        if entry[0] == name:
            return entry[1]
    return None

if __name__ == '__main__':
    from socket import *

    serverPort = 1234

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('127.0.0.1', serverPort))
    serverSocket.listen(1)

    print('Servidor DNS pronto para receber consultas.')

    while True:
        connectionSocket, addr = serverSocket.accept()

        name = connectionSocket.recv(1024).decode()

        ip_address = search_ip_address(name)

        if(ip_address!= None):
            connectionSocket.send(ip_address.encode())

        connectionSocket.close()

