if __name__ == '__main__':
    from socket import *

    serverName = '127.0.0.1'
    serverPort = 1234

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    while True:

        name = input('Digite o nome do destinatário: ')

        clientSocket.send(name.encode())

        ip_address = clientSocket.recv(1024).decode()

        if ip_address:
            print(f'O endereço IP do destinatário {name} é {ip_address}.')
        else:
            print(f'O destinatário {name} não foi encontrado no servidor DNS.')
    clientSocket.close()

