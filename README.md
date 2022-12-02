# socket-server-asn
Simple TCP socket server-client communication with ASN.1 message exchange

A simple ASN.1 message exchange with a TCP socket server. The client sends an encoded request message based on a sample ASN.1 sequence definition, which is then decoded on the server side. The server resends a new, encoded response message based on the same ASN.1 definition, which is then decoded again on the client side.

<img src = screenshot_1.png width=600>

Run server:

```
python server.py
```

Run client:

```
python client.py
```

The host.properties config file contains a host address and a port on which the server will be running. In the example the server side is running on a Debian subsystem and the client side is running on Windows.

<img src = screenshot_2.png width=600>
