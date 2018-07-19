import socket
import sys

def client(msg,log_buffer=sys.stderr):
    server_address=('localhost',10000)
    sock = socket.socket()
    sock.connect(server_address)

    recieve_message=''

    try:
        print('sending "{0}"'.format(msg),file=log_buffer)
        sock.sendall(msg.encode())
        chunk=sock.recv(16)
        recieve_message += chunk

    except:
        pass

if __name__=='__main__':
    client(sys.argv[1])


