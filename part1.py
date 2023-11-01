import socket
import time
import pickle
from enum import Enum

class User(Enum):
    user1 = '127.0.0.1'
    user2 = '127.0.0.2'
    user3 = '127.0.0.3'
    user4 = '127.0.0.4'
    user5 = '127.0.0.5'

def localIP():
    local_host = socket.gethostbyname(socket.gethostname())
    print(f'Local IP: {local_host}')

def awaitConnections():
    server_host = '0.0.0.0'
    server_port = 5555
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_host, server_port))
    server.listen(5)

    while True:
        client_socket, client_address = server.accept()
        print(f'Connection accepted from {client_address}')  

        message_received = client_socket.recv(1024)
        blob = pickle.loads(message_received)

        message_text = blob[0]
        message_command = blob[1]

        print(f'Message Received: {message_text}, command associated {message_command}')

        if message_text == 'vai se fude':
            return


def messageHandling():
    target_name = input('Insert target: ').lower()
    
    try:
        target_user = User[target_name]
        target_host = target_user.value
        print(target_host)
    except:
        print('User not found in database!')
        return
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_host, 5555))

    message = input(f'Input the message to {target_host}: ')
    command = 1
    blob = (message, command)

    data_to_send = pickle.dumps(blob)

    sock.send(data_to_send)

    sock.close()


localIP()
awaitConnections()

