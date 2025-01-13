import os

def count_bits_in_binary_file(filename):
    try:
        with open(filename, 'rb') as f:
            file_content = f.read()
        num_bits = len(file_content) * 8  # Each byte has 8 bits
        return file_content, num_bits
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, 0

def preprocess_binary_file(filename):
    binary_data, original_length = count_bits_in_binary_file(filename)

    # Step 1: Append '1' bit (10000000 in binary) and '0' bits
    binary_data += b'\x80'
    while (len(binary_data) * 8) % 512 != 448:
        binary_data += b'\x00'

    # Step 2: Append 64-bit length of the original message in bits (little-endian)
    binary_data += original_length.to_bytes(8, byteorder='little')

    print(f"Total binary data size: {len(binary_data) * 8} bits")
    return binary_data

def split_into_blocks(binary_data, block_size=64):
    return [binary_data[i:i + block_size] for i in range(0, len(binary_data), block_size)]

def convert_block_to_words(block):
    words = []
    for i in range(0, len(block), 4):  # Process 4 bytes (32 bits) at a time
        word = int.from_bytes(block[i:i + 4], byteorder='little')  # LSB first
        words.append(word)
    return words

def finalprocess(binary_file):
    # Preprocess binary file
    binary_message = preprocess_binary_file(binary_file)

    # Split into 512-bit blocks
    message_blocks = split_into_blocks(binary_message)

    # Convert each block into words and collect results
    all_blocks_words = []
    for block in message_blocks:
        block_words = convert_block_to_words(block)
        all_blocks_words.append(block_words)

    return message_blocks, all_blocks_words

# Example usage
# message_blocks, all_blocks_words = finalprocess("66.bin")

# Print binary blocks
# if message_blocks:
#     print("Binary Blocks:")
#     for block in message_blocks:
#         print(block, "\n")

#     print("_________________________")

#     # Print 32-bit words for each block
#     print("Block Words:")
#     for i, words in enumerate(all_blocks_words, 1):
#         print(f"Block {i}:")
#         for word in words:
#             print(f"{word:08x}")  # Print each word in hex format
#         print()
