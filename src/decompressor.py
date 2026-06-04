import json
import os
from bitarray import bitarray


def load_codes(codebook_path: str) -> dict:
    """
    Load Huffman codes from JSON file.

    Args:
        codebook_path (str): Path to codebook file.

    Returns:
        dict: Huffman code dictionary.
    """

    if not os.path.exists(codebook_path):
        raise FileNotFoundError(
            f"Codebook not found: {codebook_path}"
        )

    with open(
        codebook_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def reverse_codes(codes: dict) -> dict:
    """
    Reverse Huffman codes for decoding.

    Example:
        {'a':'101'} -> {'101':'a'}
    """

    return {
        code: char
        for char, code in codes.items()
    }


def load_compressed_bits(
        compressed_path: str
) -> str:
    """
    Read compressed binary file and
    convert it to bit string.
    """

    if not os.path.exists(compressed_path):
        raise FileNotFoundError(
            f"Compressed file not found: "
            f"{compressed_path}"
        )

    bits = bitarray()

    with open(
        compressed_path,
        "rb"
    ) as file:

        bits.fromfile(file)

    return bits.to01()


def decode_bitstream(
        encoded_text: str,
        reverse_codebook: dict
) -> str:
    """
    Decode Huffman bit stream.
    """

    current_code = ""

    decoded_text = []

    for bit in encoded_text:

        current_code += bit

        if current_code in reverse_codebook:

            decoded_text.append(
                reverse_codebook[current_code]
            )

            current_code = ""

    return "".join(decoded_text)


def save_decompressed_file(
        output_path: str,
        text: str
) -> None:
    """
    Save decoded text to file.
    """

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)


def decompress_file(
        compressed_path: str,
        codebook_path: str,
        output_path: str
) -> str:
    """
    Complete decompression pipeline.

    Steps:
    1. Load Huffman codes
    2. Reverse codes
    3. Load compressed bits
    4. Decode bit stream
    5. Save decompressed file

    Returns:
        str: Decoded text
    """

    codes = load_codes(
        codebook_path
    )

    reverse_codebook = reverse_codes(
        codes
    )

    encoded_text = load_compressed_bits(
        compressed_path
    )

    decoded_text = decode_bitstream(
        encoded_text,
        reverse_codebook
    )

    save_decompressed_file(
        output_path,
        decoded_text
    )

    return decoded_text