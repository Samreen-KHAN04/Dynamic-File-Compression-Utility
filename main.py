
import sys

from src.utils import read_text_file
from src.huffman import (
    build_frequency_table,
    build_heap,
    build_huffman_tree,
    generate_codes
)

from src.compressor import (
    compress_file,
    compression_ratio
)

from src.decompressor import (
    decompress_file
)

INPUT_FILE = "input_files/sample.txt"

COMPRESSED_FILE = "compressed_files/compressed.huff"

CODEBOOK_FILE = "compressed_files/codes.json"

DECOMPRESSED_FILE = "decompressed_files/decompressed.txt"


def compress_command():

    print("\nCompressing File...\n")

    text = read_text_file(INPUT_FILE)

    frequency_table = build_frequency_table(text)

    heap = build_heap(frequency_table)

    root = build_huffman_tree(heap)

    codes = generate_codes(root)

    compress_file(
        text,
        codes,
        COMPRESSED_FILE,
        CODEBOOK_FILE
    )

    print("Compression Successful")
    print(f"Output : {COMPRESSED_FILE}")
    print(f"Codebook : {CODEBOOK_FILE}")


def decompress_command():

    print("\nDecompressing File...\n")

    original_text = read_text_file(
        INPUT_FILE
    )

    decoded_text = decompress_file(
        COMPRESSED_FILE,
        CODEBOOK_FILE,
        DECOMPRESSED_FILE
    )

    print("Decompression Successful")
    print(f"Output : {DECOMPRESSED_FILE}")

    if original_text == decoded_text:
        print("Integrity Check : PASSED")
    else:
        print("Integrity Check : FAILED")
        
def stats_command():

    print("\nCompression Statistics\n")

    original_size, compressed_size, ratio = compression_ratio(
        INPUT_FILE,
        COMPRESSED_FILE
    )

    saved = original_size - compressed_size

    print("-" * 50)

    print(f"Original Size   : {original_size} bytes")
    print(f"Compressed Size : {compressed_size} bytes")
    print(f"Space Saved     : {saved} bytes")
    print(f"Compression Ratio : {ratio:.2f}%")

    print("-" * 50)


def show_help():

    print("""
Usage:

python main.py compress
python main.py decompress
python main.py stats
""")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        show_help()

    else:

        command = sys.argv[1].lower()

        if command == "compress":
            compress_command()

        elif command == "decompress":
            decompress_command()

        elif command == "stats":
            stats_command()

        else:
            show_help()

