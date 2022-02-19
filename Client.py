import threading
import socket
pseudo = input('Choisir un psuedonyme \n')
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',5566))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'NICK':
                client.send(pseudo.encode())
                pass
            else:
                print(message)
        except:
            print('Un erreur a servenu !')
            client.close()
            break

def write():
    while True:
        message = f'{pseudo}: {input("")}'
        client.send(message.encode())
receive_thread = threading.Thread(target=receive)

receive_thread.start()


write_thread = threading.Thread(target=write)
write_thread.start()




   