import json
from bitarray import bitarray


def load_codes(path):

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def reverse_codes(codes):

    reverse = {}

    for char, code in codes.items():
        reverse[code] = char

    return reverse


def decompress_file(
        compressed_path,
        codebook_path,
        output_path
):

    codes = load_codes(
        codebook_path
    )

    reverse = reverse_codes(
        codes
    )

    bits = bitarray()

    with open(
            compressed_path,
            "rb"
    ) as file:

        bits.fromfile(file)

    encoded_text = bits.to01()

    current_code = ""

    decoded_text = ""

    for bit in encoded_text:

        current_code += bit

        if current_code in reverse:

            decoded_text += reverse[current_code]
            current_code = ""

    with open(
            output_path,
            "w",
            encoding="utf-8"
    ) as file:

        file.write(decoded_text)

    return decoded_text