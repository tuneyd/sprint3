# sprint3

How to request data:

- The micro service takes two parameters: a dictionary of key:value pairs, and a single character — either ‘b’ or ‘p’. No other characters will be accepted and will case the micro service to return an empty file.
- Example call:
		
		import zmq
		import json
		
		# build package to send to microservice
		pkg = (dict, chr)
		req = bytes(json.dumps(pkg), ‘utf-8’)

		socket.send(req)

How to receive data:
- The microservice will return an base64 encoded.png file. Your program will decode and write the decoded data to a .png file.
- Example code:
		
	    import base64
		
	    # decode package
	    pkg_encode = socket.recv()		
        pkg_decode = bytearray(base64.b64decode(pkg_encode))

	    # write decoded data to file		
        f = open( ‘<file>’, ‘wb’)
	    f.write(pkg_decode)
	    f.close()

![Alt text](/git/uml_microservice.jpg?raw=true "UML")