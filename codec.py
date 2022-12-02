import asn1tools


def encode(filename, asn_sequence_name, asn_sequence_data):
    asn = asn1tools.compile_files(filename)
    encoded = asn.encode(asn_sequence_name, asn_sequence_data)
    return encoded


def decode(filename, asn_sequence_name, encoded):
    asn = asn1tools.compile_files(filename)
    decoded = asn.decode(asn_sequence_name, encoded)
    return decoded
