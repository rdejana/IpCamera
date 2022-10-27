import cv2
import socket
import numpy
import pickle
import struct


s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
server_address = ('0.0.0.0', 8000)
s.bind(server_address)

while True:
    x=s.recvfrom(1000000)
    clientip = x[1][0]
    data=x[0]

    data=pickle.loads(data)
    #print(type(data))
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)
    #gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
    cv2.imshow('listener', data) #to open image
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()