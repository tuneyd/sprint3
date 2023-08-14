import zmq
import time
import sys
from matplotlib import pyplot as plt
import numpy as np
import base64

def server():
    port = "3000"
    if len(sys.argv) > 1:
        port =  sys.argv[1]
        int(port)

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:%s" % port)

    while True:
        msg = socket.recv()
        time.sleep (1)
        getGraph(msg)
        
        socket.send(msg)
        img = open('save.png', 'rb')
        byte_img = bytearray(img.read())
        send_img = base64.b64encode(bytes)
        socket.send(send_img)
        img.close()


def getGraph(data):
    """"""
    keys = list(data[0].keys())
    values = list(data[0].values())
    fig = plt.figure(clear = True)

    if data[1] == "b":
        plt.bar(keys, values)
        plt.savefig('save.png')

    else:
        plt.pie(values)
        plt.savefig("save.png")

if __name__ == '__main__':
    server()
