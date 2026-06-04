from bitarray import bitarray
from src.utils import get_file_size


def compress_file(text, codes, output_path):

    encoded_text = ""

    for char in text:
        encoded_text += codes[char]

    bits = bitarray(encoded_text)

    with open(output_path, "wb") as file:
        bits.tofile(file)

    return encoded_text


def compression_ratio(original_file, compressed_file):

    original_size = get_file_size(original_file)

    compressed_size = get_file_size(compressed_file)

    ratio = (compressed_size / original_size) * 100

    return (
        original_size,
        compressed_size,
        ratio
    )