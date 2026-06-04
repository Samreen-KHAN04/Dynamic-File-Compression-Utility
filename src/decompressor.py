from src.huffman import decode_text


def decompress_file(
        encoded_text,
        root,
        output_path
):

    decoded_text = decode_text(
        encoded_text,
        root
    )

    with open(
            output_path,
            "w",
            encoding="utf-8"
    ) as file:

        file.write(decoded_text)

    return decoded_text