import zmq
import sys
import time
import base64
import json
import random



def client(data, chart):
    """"""
    port = "3000"
    if len(sys.argv) > 1:
        port =  sys.argv[1]
        int(port)

    if len(sys.argv) > 2:
        port1 =  sys.argv[2]
        int(port1)

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect ("tcp://localhost:%s" % port)
    if len(sys.argv) > 2:
        socket.connect ("tcp://localhost:%s" % port1)

    msg = (data, chart)
    send = bytes(json.dumps(msg), 'utf-8')
    socket.send(send)

    
    # generate random string
    name = ""
    while len(name) < 5:
        chr = str(random.randint(0,9))
        name = name + chr

    m = socket.recv()
    f = open('saved/%s.png' %name, 'wb')
    ba = bytearray(base64.b64decode(m))
    f.write(ba)
    f.close()

if __name__ == '__main__':
    data = {1:2, 2:3, 3:100}
    graph = "b"
    chart = "p"
    client(data, graph)
    time.sleep(5)
    client(data, chart)