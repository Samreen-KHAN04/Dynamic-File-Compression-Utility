import heapq
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_frequency_table(text):
    return Counter(text)


def build_heap(freq_table):

    heap = []

    for char, freq in freq_table.items():
        heapq.heappush(heap, Node(char, freq))

    return heap


def build_huffman_tree(heap):

    while len(heap) > 1:

        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)

        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]
def generate_codes(root):

    codes = {}

    def traverse(node, current_code):

        if node is None:
            return

        if node.char is not None:
            codes[node.char] = current_code
            return

        traverse(node.left, current_code + "0")
        traverse(node.right, current_code + "1")

    traverse(root, "")

    return codes
def print_tree(node, level=0):

    if node is None:
        return

    print_tree(node.right, level + 1)

    if node.char is not None:
        print("    " * level + f"{node.char}:{node.freq}")
    else:
        print("    " * level + f"*:{node.freq}")

    print_tree(node.left, level + 1)
def encode_text(text, codes):

    encoded_text = ""

    for char in text:
        encoded_text += codes[char]

    return encoded_text


def decode_text(encoded_text, root):

    decoded_text = ""

    current = root

    for bit in encoded_text:

        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded_text += current.char
            current = root

    return decoded_text