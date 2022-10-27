import cv2
import socket
import numpy
import pickle
import struct


s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

multicast_group = '224.3.29.71'
server_address = ('', 8000)


s.bind(server_address)
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
while True:
    x=s.recvfrom(1000000)
    clientip = x[1][0]
    data=x[0]

    data=pickle.loads(data)
    #print(type(data))
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
    cv2.imshow('client', gray) #to open image
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()