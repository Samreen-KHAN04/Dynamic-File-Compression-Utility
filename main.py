from src.utils import read_text_file

from src.huffman import (
    build_frequency_table,
    build_heap,
    build_huffman_tree,
    generate_codes,
    print_tree,
    encode_text
)

from src.compressor import (
    compress_file,
    compression_ratio
)

from src.decompressor import (
    decompress_file
)


INPUT_FILE = "input_files/sample.txt"

COMPRESSED_FILE = (
    "compressed_files/compressed.bin"
)

DECOMPRESSED_FILE = (
    "decompressed_files/decompressed.txt"
)


def main():

    print("\nReading Input File...")

    text = read_text_file(
        INPUT_FILE
    )

    frequency_table = (
        build_frequency_table(text)
    )

    heap = build_heap(
        frequency_table
    )

    root = build_huffman_tree(
        heap
    )

    codes = generate_codes(
        root
    )

    print("\nGenerated Huffman Codes")

    print("-" * 50)

    for char, code in sorted(
            codes.items()):

        if char == "\n":
            display = "\\n"

        elif char == " ":
            display = "SPACE"

        else:
            display = char

        print(
            f"{display:<10} -> {code}"
        )

    print("\nCompressing File...")

    encoded_text = compress_file(
        text,
        codes,
        COMPRESSED_FILE
    )

    print(
        f"Compressed file saved:"
        f" {COMPRESSED_FILE}"
    )

    print("\nDecompressing File...")

    decoded_text = decompress_file(
        encoded_text,
        root,
        DECOMPRESSED_FILE
    )

    print(
        f"Decompressed file saved:"
        f" {DECOMPRESSED_FILE}"
    )

    print("\nChecking Integrity")

    if text == decoded_text:
        print(
            "SUCCESS:"
            " Original and Decompressed"
            " files match."
        )
    else:
        print(
            "ERROR:"
            " Files do not match."
        )

    (
        original_size,
        compressed_size,
        ratio
    ) = compression_ratio(
        INPUT_FILE,
        COMPRESSED_FILE
    )

    print("\nCompression Report")

    print("-" * 50)

    print(
        f"Original Size   : "
        f"{original_size} bytes"
    )

    print(
        f"Compressed Size : "
        f"{compressed_size} bytes"
    )

    print(
        f"Compression Ratio:"
        f" {ratio:.2f}%"
    )


if __name__ == "__main__":
    main()