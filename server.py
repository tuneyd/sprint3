import time
import sys
import zmq
from matplotlib import pyplot as plt
import base64
import json


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
        decode_msg = json.loads(msg)
        print(decode_msg)
        
        time.sleep (1)
        if decode_msg[1] == 'b':
            getGraph(decode_msg[0])
            img = open('figures/graph.png', 'rb')
            byte_img = bytearray(img.read())
            send_img = base64.b64encode(byte_img)
            socket.send(send_img)
            img.close()
        elif decode_msg[1] == 'p':
            getChart(decode_msg[0])
            img = open('figures/chart.png', 'rb')
            byte_img = bytearray(img.read())
            send_img = base64.b64encode(byte_img)
            socket.send(send_img)
            img.close()
        else:
            return


def getGraph(data):
    """"""
    keys = list(data.keys())
    values = list(data.values())
    plt.bar(keys, values)
    plt.savefig('figures/graph.png')

def getChart(data):
    """"""
    keys = list(data.keys())
    values = list(data.values())
    fig = plt.figure(clear = True)
    plt.pie(values, labels=keys, autopct='%1.1f%%')
    plt.savefig('figures/chart.png')

if __name__ == '__main__':
    server()
