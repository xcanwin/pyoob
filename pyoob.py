import socket, threading, argparse

def listen(source_addr, source_port, source_xcanwin, output):
    sock = socket.socket(socket.AF_INET, source_xcanwin)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((source_addr, source_port))
    if sock.type == socket.SOCK_STREAM:
        sock.listen(1)
    while True:
        if sock.type == socket.SOCK_STREAM:
            client_type = 'TCP'
            connection, (client_host, client_port) = sock.accept()
            get_data1 = connection.recv(1024*1024)
        elif sock.type == socket.SOCK_DGRAM:
            client_type = 'UDP'
            get_data1, (client_host, client_port) = sock.recvfrom(1024*1024)
        else:
            client_type = 'OTHER'
        result_from = '\n\nPYOOB: %s: Connection from %s:%s\n' % (client_type, client_host, client_port)
        result = result_from.encode()
        if not get_data1:
            get_data1 = b''
        result += get_data1 + b'\n'
        print(result.decode('utf-8', 'ignore'))
        open(output, 'ab').write(result)
    if sock.type == socket.SOCK_STREAM:
        connection.close()
    sock.close()

def create_thread(source_addr, source_port, source_xcanwin, output):
    t = threading.Thread(target=listen, args=(source_addr, source_port, source_xcanwin, output))
    t.daemon = True
    t.start()

def set_thread_tail():
    try:
        while True:
            input('')
    except:
        exit('PYOOB: Closing connection')

if __name__ == '__main__':
    description_tips = '''基于Python的轻量级NetCat服务器，用于接收HTTP、OOB、SSRF等多种请求，
同时监听TCP与UDP两种协议，并且可以持续获取结果，有日志记录功能。'''
    usage_tips = '''Example:
  python %(prog)s
  python %(prog)s -p 6006
  python %(prog)s -s 0.0.0.0 -p 6006
  python %(prog)s -s 0.0.0.0 -p 6006 -o pyoob.log'''
    parser = argparse.ArgumentParser(description = description_tips, epilog = usage_tips, formatter_class = argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-s', '--source-addr', default = '0.0.0.0', help = 'Listen addr')
    parser.add_argument('-p', '--source-port', type=int, default = 6006, help = 'Listen port')
    parser.add_argument('-o', '--output', default = './pyoob.log', help = 'Log file')
    options = parser.parse_args()
    print('PYOOB: Listening on %s:%s' % (options.source_addr, options.source_port))
    for source_xcanwin in (socket.SOCK_STREAM, socket.SOCK_DGRAM):
        create_thread(options.source_addr, options.source_port, source_xcanwin, options.output)
    set_thread_tail()
