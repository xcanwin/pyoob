import socket, threading

server_host = '0.0.0.0'
server_port = 61359

def listen(server_host, server_port):
    print('XNETCAT: Listening on %s:%s' % (server_host, server_port))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    sock.bind((server_host, server_port))
    sock.listen(5)
    while True:
        connection, (client_host, client_port) = sock.accept()
        print('\n\nXNETCAT: Connection from %s:%s' % (client_host, client_port))
        print(connection.recv(1024*100).decode('utf-8','ignore'))
        connection.close()

t = threading.Thread(target=listen, args=(server_host, server_port))
t.daemon = True
t.start()
try:
    while True:
        pass
except:
    exit('XNETCAT: Exit')
