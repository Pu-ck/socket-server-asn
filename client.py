import configparser
import socket
from codec import encode, decode


def send_message(HOST, PORT, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(message)
        received = sock.recv(1024)
        return received


def message_compose(response_string, response_octetstring):
    message = {"string": response_string, "octetstring": response_octetstring}
    return message


def get_host_data():
    config = configparser.RawConfigParser()
    config.read("host.properties")
    return config.get("Host", "host.address"), config.get("Host", "host.port")


if __name__ == "__main__":
    HOST, PORT = get_host_data()

    asn_sequence_name = "Message"
    request_message = message_compose("request", bytearray([1, 0, 1, 0, 1, 0, 1, 0]))

    print("Client request message: ")
    print(request_message)

    encoded = encode("ExampleASN.asn1", asn_sequence_name, request_message)
    received = send_message(HOST, int(PORT), encoded)
    decoded = decode("ExampleASN.asn1", "Message", received)

    print("Server response message: ")
    print(decoded)
