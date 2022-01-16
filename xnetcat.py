import socket, threading

def listen(server_host, server_port, server_type):
    sock = socket.socket(socket.AF_INET, server_type)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((server_host, server_port))
    while True:
        if sock.type == socket.SOCK_STREAM:
            client_type = 'TCP'
            sock.listen(1)
            connection, (client_host, client_port) = sock.accept()
            get_data1 = connection.recv(1024*1024)
        elif sock.type == socket.SOCK_DGRAM:
            client_type = 'UDP'
            get_data1, (client_host, client_port) = sock.recvfrom(1024*1024)
        else:
            client_type = 'OTHER'
        result_from = '\n\nXNETCAT: %s: Connection from %s:%s\n' % (client_type, client_host, client_port)
        result = result_from.encode()
        result += get_data1 + b'\n'
        print(result.decode('utf-8', 'ignore'))
        open('xnetcat.log', 'ab').write(result)
        if sock.type == socket.SOCK_STREAM:
            connection.close()
    sock.close()

def create_thread(server_host, server_port, server_type):
    t = threading.Thread(target=listen, args=(server_host, server_port, server_type))
    t.daemon = True
    t.start()

def stop():
    try:
        while True:
            pass
    except:
        exit('XNETCAT: Exit')


server_host = '0.0.0.0'
server_port = 4444
print('XNETCAT: Listening on %s:%s' % (server_host, server_port))
create_thread(server_host, server_port, socket.SOCK_STREAM)
create_thread(server_host, server_port, socket.SOCK_DGRAM)
stop()
