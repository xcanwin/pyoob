import socket, threading, argparse

def listen(server_host, server_port, server_xcanwin, log_file):
    sock = socket.socket(socket.AF_INET, server_xcanwin)
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
        result_from = '\n\nPYOOB: %s: Connection from %s:%s\n' % (client_type, client_host, client_port)
        result = result_from.encode()
        result += get_data1 + b'\n'
        print(result.decode('utf-8', 'ignore'))
        open(log_file, 'ab').write(result)
        if sock.type == socket.SOCK_STREAM:
            connection.close()
    sock.close()

def create_thread(server_host, server_port, server_xcanwin, log_file):
    t = threading.Thread(target=listen, args=(server_host, server_port, server_xcanwin, log_file))
    t.daemon = True
    t.start()

def set_thread_tail():
    try:
        while True:
            input('')
    except:
        exit('PYOOB: Exit')

if __name__ == '__main__':
    description_tips = '''基于Python的轻量级NetCat服务器，用于接收HTTP、OOB、SSRF等多种请求，
同时监听TCP与UDP两种协议，并且可以持续获取结果，有日志记录功能。'''
    usage_tips = '''Example:
  python %(prog)s
  python %(prog)s -P 4444
  python %(prog)s -H 0.0.0.0 -P 4444
  python %(prog)s -H 0.0.0.0 -P 4444 -L pyoob.log'''
    parser = argparse.ArgumentParser(description = description_tips, epilog = usage_tips, formatter_class = argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-H', '--server-host', default = '0.0.0.0', help = 'Listen host')
    parser.add_argument('-P', '--server-port', type=int, default = 4444, help = 'Listen port')
    parser.add_argument('-L', '--log-file', default = './pyoob.log', help = 'Log file')
    options = parser.parse_args()
    print('PYOOB: Listening on %s:%s' % (options.server_host, options.server_port))
    for server_xcanwin in (socket.SOCK_STREAM, socket.SOCK_DGRAM):
        create_thread(options.server_host, options.server_port, server_xcanwin, options.log_file)
    set_thread_tail()
