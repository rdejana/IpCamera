import cv2
import socket
import pickle
import numpy as np
import struct

# pip3 install opencv-python

# this is a simple multicast example
multicast_group = ('224.3.29.71', 8000)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,1000000)

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# the index depends on your camera setup and which one is your USB camera.
# you may need to change to 1 depending on your local config
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)

    ret, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 30])
    x_as_bytes = pickle.dumps(buffer)
    s.sendto((x_as_bytes), multicast_group)
    # Display the resulting frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()