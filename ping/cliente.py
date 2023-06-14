import time
from socket import *

serverName = '192.168.0.187'  
serverPort = 50000  
timeout = 1  


clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(timeout)

rtt_times = []  

for sequence_number in range(1, 11):

    send_time = time.time()

    message = f'Ping {sequence_number} {send_time}'

    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        receive_time = time.time()
        rtt = receive_time - send_time
        rtt_times.append(rtt)
        
        print(f'Resposta de {serverAddress[0]}: {modifiedMessage.decode()}')
        print(f'RTT: {rtt} segundos')

    except Exception as e:
        if type(e) == timeout:
            print(f'Request time out')
        else:
            print(f'Error: {e}')


min_rtt = min(rtt_times)
max_rtt = max(rtt_times)
avg_rtt = sum(rtt_times) / len(rtt_times)
packet_loss = (10 - len(rtt_times)) / 10 * 100

print(f'Minimo RTT: {min_rtt} segundos')
print(f'Maximo RTT: {max_rtt} segundos')
print(f'Media RTT: {avg_rtt} segundos')
print(f'Perda pacote: {packet_loss}%')

clientSocket.close()

