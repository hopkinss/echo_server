import socket

# [(<AddressFamily.AF_INET: 2>,
#   <SocketKind.SOCK_STREAM: 1>,
#   0,
#   '',
#   ('188.184.64.53', 80))]
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
client.connect(('188.184.64.53', 80))
msg="GET /HTTP/1.1.\r\n"
msg+="Host: info.cern.ch\r\n\r\n"
msg=msg.encode('utf8')
client.sendall(msg)
response=client.recv(1024)
print(response)
client.close()