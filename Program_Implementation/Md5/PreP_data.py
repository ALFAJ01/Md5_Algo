import os

# def count_bits_in_binary_file(filename):
#     try:
#         with open(filename, 'rb') as f:
#             file_content = f.read()
#             print(file_content)
#         num_bits = len(file_content) * 8  # Each byte has 8 bits
#         return file_content, num_bits
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")
#         return None, 0
# count_bits_in_binary_file("test.txt")


# def count_bits_in_binary_file(filename):
#     try:
#         with open(filename, 'rb') as f:
#             file_content = f.read()
#             binary_string = bin(file_content)[2:]
#             print(binary_string)
#         num_bits = len(binary_string)
#         return file_content, num_bits
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")
#         return None, 0

# # Example usage (change "test.txt" to your desired file)
# count_bits_in_binary_file("test.txt")


# def read_text_file_as_text(filename):
#     try:
#         with open(filename, 'r') as f:
#             text_content = f.read()
#             # Optionally, convert to a specific encoding if needed
#             ascii_text = text_content.encode('ascii')
#             print(ascii_text)
#             return text_content
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")
#         return None

# # Example usage (change "test.txt" to your desired text file)
# text_data = read_text_file_as_text("test.txt")
# if text_data:
#     print(text_data)




# def count_bits_in_binary_file(filename):
#     try:
#         with open(filename, 'rb') as f:
#             file_content = f.read()
#             # Convert bytes to integer (might lose data for non-ASCII)
#             int_data = int.from_bytes(file_content, byteorder='big')
#             binary_string = bin(int_data)[2:]
#             print(binary_string)
#         num_bits = len(binary_string)
#         print(f"the message length {num_bits}")
#         return file_content, num_bits
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")
#         return None, 0

# # Example usage
# count_bits_in_binary_file("test.txt")

def count_bits_in_binary_file(filename):
    try:
        with open(filename, 'rb') as f:
            file_content = f.read()
            binary_string = ""
            for byte in file_content:
                _byte=format(byte, '08b')
                print(_byte,end=" ")
                # Convert each byte to binary string (8 bits)
                binary_string += format(byte, '08b')
            # print(binary_string)
            num_bits = len(binary_string)
        print(f"the message length {num_bits}")
        return file_content, num_bits
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, 0

# Example usage
count_bits_in_binary_file("/home/mr./Downloads/20241115_163705.jpg")




  def append_length(binary_message_after_padding, message_length):
    """
    Appends the 64-bit representation of the original message length to the
    padded message, handling lengths greater than 2^64 and appending as
    two 32-bit words (low-order word first).

    Args:
        binary_message_after_padding (str): The binary message after padding.
        message_length (int): The original message length in bits.

    Returns:
        str: The binary message with the length appended, or None if there's an error.
    """
    try:
        if message_length < 0:
            raise ValueError("Message length cannot be negative.")

        length_64bit = message_length % (2**64)

        # Convert to 64-bit binary string
        length_binary = bin(length_64bit)[2:].zfill(64)

        # Split into two 32-bit words
        low_word = length_binary[32:]
        high_word = length_binary[:32]

        # Append low-order word first
        message_with_length = binary_message_after_padding + low_word + high_word

        return message_with_length

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except TypeError:
        print("Error: Message length must be an integer.")
        return None

# # Example usage:
# message_length = 0xFFFFFFFFFFFFFFFF # Example message length in bits greater than 2**64
# binary_message_after_padding = "1010101010101010101010101010101010101010101010101010101010101010" # Example padded message (64 bits for demonstration)

# message_with_length = append_length(binary_message_after_padding, message_length)

# if message_with_length:
#     print("Message with length appended:", message_with_length)
#     print("Total length (bits):", len(message_with_length))
#     print("low word",message_with_length[64:96])
#     print("high word",message_with_length[96:])

# message_length = 255  # Example message length in bits
# binary_message_after_padding = "1010101010101010101010101010101010101010101010101010101010101010" # Example padded message (64 bits for demonstration)

# message_with_length = append_length(binary_message_after_padding, message_length)

# if message_with_length:
#     print("Message with length appended:", message_with_length)
#     print("Total length (bits):", len(message_with_length))
#     print("low word",message_with_length[64:96])
#     print("high word",message_with_length[96:])




def preprocess_binary_file(filename):
    binary_data, original_length = count_bits_in_binary_file(filename)

    # Step 1: Append '1' bit (10000000 in binary) and '0' bits
    binary_data += b'\x80'
    while (len(binary_data) * 8) % 512 != 448:
        binary_data += b'\x00'

    # Step 2: Append 64-bit length of the original message in bits (little-endian)
    binary_data_after_add_leangh= append_length(binary_data,original_length)

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



# import os

# def preprocess_data(data, is_file=True):
#     """
#     Preprocess input data for MD5 hashing.

#     Args:
#         data: The input data (string or file path).
#         is_file: Boolean indicating whether the input is a file path or instance data.

#     Returns:
#         Binary data ready for MD5 hashing.
#     """
#     if is_file:
#         try:
#             with open(data, 'rb') as f:
#                 binary_data = f.read()
#         except FileNotFoundError:
#             print(f"Error: File '{data}' not found.")
#             return None
#     else:
#         # Convert string to bytes
#         binary_data = data.encode('utf-8')

#     original_length = len(binary_data) * 8  # Length in bits

#     # Step 1: Append '1' bit (10000000 in binary) and '0' bits
#     binary_data += b'\x80'
#     while (len(binary_data) * 8) % 512 != 448:
#         binary_data += b'\x00'

#     # Step 2: Append 64-bit length of the original message in bits (little-endian)
#     binary_data += original_length.to_bytes(8, byteorder='little')

#     print(f"Total binary data size: {len(binary_data) * 8} bits")
#     return binary_data

# def split_into_blocks(binary_data, block_size=64):
#     return [binary_data[i:i + block_size] for i in range(0, len(binary_data), block_size)]

# def convert_block_to_words(block):
#     words = []
#     for i in range(0, len(block), 4):  # Process 4 bytes (32 bits) at a time
#         word = int.from_bytes(block[i:i + 4], byteorder='little')  # LSB first
#         words.append(word)
#     return words