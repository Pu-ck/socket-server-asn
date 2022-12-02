import socketserver
import configparser
from codec import encode, decode


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        decoded = decode("ExampleASN.asn1", "Message", self.data)
        response_message = message_compose(
            "response", bytearray([0, 0, 0, 0, 0, 0, 0, 0])
        )
        encoded_response = encode("ExampleASN.asn1", "Message", response_message)
        self.request.sendall(encoded_response)


def start_server(HOST, PORT):
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()


def message_compose(response_string, response_octetstring):
    message = {"string": response_string, "octetstring": response_octetstring}
    return message


def get_host_data():
    config = configparser.RawConfigParser()
    config.read("config.properties")
    return config.get("Host", "host.address"), config.get("Host", "host.port")


if __name__ == "__main__":
    HOST, PORT = get_host_data()
    start_server(HOST, int(PORT))
