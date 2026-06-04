# Dynamic File Compression Utility

A DSA-based lossless file compression utility built using **Huffman Coding**, **Min Heap**, **Binary Trees**, and **Greedy Algorithms**. The application compresses text files into a compact binary format and restores them back to their original form without any data loss.

---

## 📌 Project Overview

Data compression is an essential technique used to reduce storage requirements and improve transmission efficiency.

This project implements the **Huffman Coding Algorithm**, a lossless compression technique that assigns shorter binary codes to frequently occurring characters and longer codes to less frequent characters.

The utility performs:

* File Compression
* File Decompression
* Huffman Tree Construction
* Binary Encoding & Decoding
* Compression Statistics Generation
* Integrity Verification

---

## 🎯 Objectives

* Implement Huffman Coding from scratch.
* Demonstrate key Data Structures and Algorithms concepts.
* Reduce file size without losing information.
* Provide a command-line utility for compression and decompression.
* Analyze compression performance using statistics.

---

## 🚀 Features

### Compression

* Reads text files
* Builds character frequency table
* Constructs Huffman Tree
* Generates Huffman Codes
* Compresses data into binary format
* Stores metadata in JSON format

### Decompression

* Reads compressed binary file
* Loads Huffman codebook
* Decodes compressed bitstream
* Reconstructs original file
* Verifies data integrity

### Statistics

* Original file size
* Compressed file size
* Compression ratio
* Space saved

---

## 🏗️ Project Architecture

```text
Input File
     │
     ▼
Frequency Analysis
(Hash Map)
     │
     ▼
Min Heap Creation
(Priority Queue)
     │
     ▼
Huffman Tree
(Binary Tree)
     │
     ▼
Code Generation
     │
     ▼
Encoding
     │
     ▼
Binary Compression
     │
     ▼
Compressed File (.huff)
     │
     ▼
Decoding
     │
     ▼
Original File Restored
```

---

## 📂 Project Structure

```text
Dynamic-File-Compression-Utility/
│
├── compressed_files/
│   ├── compressed.huff
│   └── codes.json
│
├── decompressed_files/
│   └── decompressed.txt
│
├── input_files/
│   └── sample.txt
│
├── images/
│
├── docs/
│
├── src/
│   ├── huffman.py
│   ├── compressor.py
│   ├── decompressor.py
│   └── utils.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Technologies Used

* Python 3.x
* Huffman Coding
* Bitarray Library
* JSON
* File Handling
* Git & GitHub

---

## 📚 Data Structures Used

### Hash Map (Dictionary)

Used to store character frequencies.

Example:

```python
{
    'a': 10,
    'e': 11,
    ' ': 12
}
```

---

### Min Heap (Priority Queue)

Used to efficiently retrieve nodes with minimum frequency during Huffman Tree construction.

Operations:

* heappush()
* heappop()

Time Complexity:

```text
O(log n)
```

---

### Binary Tree

Used to represent the Huffman Tree.

Each leaf node represents a character and its frequency.

---

## 🧠 Algorithm Used

### Huffman Coding Algorithm

1. Calculate character frequencies.
2. Create a node for each character.
3. Insert all nodes into a Min Heap.
4. Repeatedly remove two minimum-frequency nodes.
5. Merge them into a new internal node.
6. Insert merged node back into heap.
7. Continue until only one node remains.
8. Generate binary codes through tree traversal.
9. Encode input data using generated codes.

---

## ⚙️ Time Complexity Analysis

| Operation                 | Complexity |
| ------------------------- | ---------- |
| Frequency Counting        | O(n)       |
| Heap Construction         | O(n log n) |
| Huffman Tree Construction | O(n log n) |
| Code Generation           | O(n)       |
| Encoding                  | O(n)       |
| Decoding                  | O(n)       |

Where:

* n = Number of characters

---

## 💻 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Dynamic-File-Compression-Utility.git

cd Dynamic-File-Compression-Utility
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Compress File

```bash
python main.py compress
```

Output:

```text
Compression Successful
Output : compressed_files/compressed.huff
Codebook : compressed_files/codes.json
```

---

### Decompress File

```bash
python main.py decompress
```

Output:

```text
Decompression Successful
Output : decompressed_files/decompressed.txt

Integrity Check : PASSED
```

---

### View Statistics

```bash
python main.py stats
```

Output:

```text
Original Size   : 145 bytes
Compressed Size : 77 bytes
Space Saved     : 68 bytes
Compression Ratio : 53.10%
```

---

## 📊 Sample Results

| Metric            | Value     |
| ----------------- | --------- |
| Original Size     | 145 Bytes |
| Compressed Size   | 77 Bytes  |
| Space Saved       | 68 Bytes  |
| Compression Ratio | 53.10%    |
| Integrity Check   | PASSED    |

---

## 📸 Screenshots

Add screenshots inside the images folder.

Recommended screenshots:

* Project Structure
* Huffman Tree Output
* Huffman Codes
* Compression Process
* Compression Statistics
* Decompression Success
* Codebook File

Example:

```markdown
![Compression Statistics](images/compression_ratio.png)
```

---

## 🔍 Key Learning Outcomes

Through this project, I gained hands-on experience with:

* Huffman Coding
* Greedy Algorithms
* Binary Trees
* Priority Queues
* File Compression Techniques
* Binary File Handling
* JSON Metadata Storage
* Command Line Interfaces
* Git & GitHub Workflow

---

## 🔮 Future Enhancements

* GUI using Tkinter
* Drag-and-Drop File Support
* Multiple File Compression
* Folder Compression
* Compression History
* Real-Time Progress Bar
* Support for Additional Compression Algorithms

---

## 👨‍💻 Author

**Samreen Begum**

B.Tech Information Technology


---

## 📄 License

This project is developed for educational and learning purposes.
Feel free to fork, improve, and contribute.
