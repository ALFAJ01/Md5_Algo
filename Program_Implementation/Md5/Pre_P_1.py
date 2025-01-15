import os
DEBUG_LOG_FILE = "md5_debug.log" 

def write_to_debug_log(message):
    try:
        with open(DEBUG_LOG_FILE, 'a', encoding='utf-8') as log_file:
            log_file.write(message)
    except Exception as e:
        print(f"\nError writing to debug log: {e}")

def count_bits_in_binary_file(filename):
    """Counts bits in a binary file """
    write_to_debug_log(f"\nStarting count_bits_in_binary_file for: {filename}\n")
    try:
        with open(filename, 'rb') as f:
            file_content = f.read()
        num_bits = len(file_content) * 8
        binary_string = ""
        write_to_debug_log(f"\nByte to it equivalent binary is of {filename}\n")
        for byte in file_content:
            _byte = format(byte, '08b')
            write_to_debug_log(f"Byte: {_byte} ")
        write_to_debug_log(f"\n {filename} bits ie 1's and 0's Represntation is :\n")
        for byte in file_content:
            _byte = format(byte, '08b')
            write_to_debug_log(f"{_byte} ")

        write_to_debug_log( f"\nTotal bits in original data is : {num_bits}")
        return file_content, num_bits

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        write_to_debug_log(f"\nError: File '{filename}' not found.")
        return None, 0


####      1

# def append_length(binary_message_after_padding, message_length):
#     try:
#         if message_length < 0:
#             raise ValueError("\nMessage length cannot be negative.")
#         write_to_debug_log(f"\nChecking is the Message leanght is Grether than 2^64")
#         write_to_debug_log("""
#                      \nif the leangth is grether than 2^64 than only the low order bit is padded.
#                                                 otherwise """)
#         if message_length > (pow(2,64)):
#             write_to_debug_log(f"\nMessage lenght is Grether thah 2^64 ie the message lenght is {message_length} and We represent with 64 bits only which size is 18446744073709551616")
#             length_64bit = message_length % (2**64)
#         if message_length <(pow(2,64)):
#             length_64bit=message_length
#         # Convert to 64-bit binary string
#         write_to_debug_log(f"\nConverting the message length into eqivalent 64 bit binary representation ")
#         length_bytes = length_64bit.to_bytes(8, byteorder='little')
#         write_to_debug_log(f"\nLength bytes (little-endian): {length_bytes}")
#         length_binary_string = "".join(format(byte, '08b') for byte in length_bytes)
#         write_to_debug_log(f"\nLength bytes (binary): {length_binary_string}")  # Log in binary
 
#         write_to_debug_log( f"\n64-bit length representation of length {length_64bit} is  {length_bytes}")
#         write_to_debug_log(f"\nLength bytes (bytes object): {length_bytes}") #Log in bytes object

#         write_to_debug_log( f"\nNow Spliting the 64 bit into two 32 bit word ")
#         # Split into two 32-bit words (4 bytes each)
#         low_word_bytes = length_bytes[:4]
#         high_word_bytes = length_bytes[4:]

#         write_to_debug_log(f"\nLow word bytes: {low_word_bytes}")
#         write_to_debug_log(f"\nHigh word byreturn message_with_lengthtes: {high_word_bytes}")

#         message_with_length = binary_message_after_padding + high_word_bytes + low_word_bytes
#         write_to_debug_log(f"\nMessage with length appended:\n {message_with_length}")
            
#         write_to_debug_log( f"\nMessage after appended message original length  (binary)is\n")
#         for _byte in message_with_length:
#             write_to_debug_log(f"{_byte} ")
#         return message_with_length

#     except ValueError as e:
#         print(f"Error: {e}")
#         write_to_debug_log( f"\nError: {e}")
#         return None
#     except TypeError:
#         print("Error: Message length must be an integer.")
#         write_to_debug_log("\nError: Message length must be an integer.")
#         return None


#####   2

# def append_length(binary_message_after_padding, message_length):
#     try:
#         if message_length < 0:
#             raise ValueError("\nMessage length cannot be negative.")

#         write_to_debug_log(f"\nMessage Length: {message_length} bits")

#         length_64bit = message_length % (2**64)  # Handle lengths > 2^64

#         length_bytes = length_64bit.to_bytes(8, byteorder='little')

#         write_to_debug_log(f"\n64-bit length (little-endian bytes): {length_bytes}")

#         # Correct order: LOW word FIRST, then HIGH word
#         low_word_bytes = length_bytes[:4]
#         high_word_bytes = length_bytes[4:]

#         write_to_debug_log(f"\nLow word bytes: {low_word_bytes}")
#         write_to_debug_log(f"\nHigh word bytes: {high_word_bytes}")

#         # ***KEY CHANGE: Append low word THEN high word***
#         message_with_length = binary_message_after_padding + low_word_bytes + high_word_bytes

#         write_to_debug_log(f"\nMessage with length appended:")
#         write_to_debug_log(f"Length of message with length appended: {len(message_with_length)*8} bits")
#         write_to_debug_log(" ".join(format(byte, '08b') for byte in message_with_length))

#         return message_with_length

#     except ValueError as e:
#         print(f"Error: {e}")
#         write_to_debug_log(f"\nError: {e}")
#         return None
#     except TypeError:
#         print("Error: Message length must be an integer.")
#         write_to_debug_log("\nError: Message length must be an integer.")
#         return None

###  3



def append_length(binary_message_after_padding, message_length):
    try:
        if message_length < 0:
            raise ValueError("\nMessage length cannot be negative.")

        write_to_debug_log(f"\nMessage Length: {message_length} bits")

        length_64bit = message_length % (2**64)  # Handle lengths > 2^64

        length_bytes = length_64bit.to_bytes(8, byteorder='big')

        write_to_debug_log(f"\n64-bit length (little-endian bytes): {length_bytes}")

        # Correct order: LOW word FIRST, then HIGH word
        low_word_bytes = length_bytes[:4]
        high_word_bytes = length_bytes[4:]

        # ***KEY CHANGE: Reverse bytes WITHIN each word***
        low_word_bytes = low_word_bytes[::-1]  # Reverse bytes in low word
        high_word_bytes = high_word_bytes[::-1] # Reverse bytes in high word

        write_to_debug_log(f"\nLow word bytes (reversed): {low_word_bytes}")
        write_to_debug_log(f"\nHigh word bytes (reversed): {high_word_bytes}")

        message_with_length = binary_message_after_padding + low_word_bytes + high_word_bytes

        write_to_debug_log(f"\nMessage with length appended:")
        write_to_debug_log(" ".join(format(byte, '08b') for byte in message_with_length))
        write_to_debug_log(f"Length of message with length appended: {len(message_with_length)*8} bits")

        return message_with_length

    except ValueError as e:
        print(f"Error: {e}")
        write_to_debug_log(f"\nError: {e}")
        return None
    except TypeError:
        print("Error: Message length must be an integer.")
        write_to_debug_log("\nError: Message length must be an integer.")
        return None

def preprocess_binary_file(filename):
    """Preprocesses the binary file for MD5."""
    write_to_debug_log(f"\nStarting preprocess_binary_file for: {filename}\n")
    binary_data, original_length = count_bits_in_binary_file(filename)

    if binary_data is None:  # Handle file not found
        return None

    write_to_debug_log(f"\nOriginal length: {original_length} bits")

    binary_data += b'\x80'
    write_to_debug_log(f"\nAfter appending '1' bit: ")
    write_to_debug_log( f"\nMessage after appended padding 1st bits as 1 is:\n")
    for byte in binary_data:
        _byte = format(byte, '08b')
        write_to_debug_log(f"{_byte} ")
    write_to_debug_log(f"\nChecking wheather the file is Modulo 512 =448 is or not ")
    i=True
    while (len(binary_data) * 8) % 512 != 448:
        if i==True:
            write_to_debug_log(f"\nMessage length is not Modulo 512 =448 is  So padding the 0 to make the message modulo(512)=448 ")
        binary_data += b'\x00'
        i=False
    write_to_debug_log(f"\nAfter padding with zeros: {binary_data}\n")
    for byte in binary_data:
        _byte = format(byte, '08b')
        write_to_debug_log(f"{_byte} ")

    binary_data_after_add_length = append_length(binary_data, original_length)
    if binary_data_after_add_length is None:
        return None
    write_to_debug_log(f"\nAfter appending length: {binary_data_after_add_length}")

    write_to_debug_log(f"\nTotal binary data size: {len(binary_data_after_add_length)} bits")
    return binary_data_after_add_length

# def split_into_blocks(binary_data, block_size=512): # changed to 512
#     write_to_debug_log(f"Starting split_into_blocks with block_size: {block_size}")
#     blocks = [binary_data[i:i + block_size] for i in range(0, len(binary_data), block_size)]
#     write_to_debug_log(f"Number of blocks: {len(blocks)}")
#     return blocks
def split_into_blocks(binary_data, block_size=512):
    """Splits binary data into blocks and logs the process with block details."""
    write_to_debug_log(f"\nStarting split_into_blocks with block_size: {block_size}")

    blocks = []
    for i in range(0, len(binary_data), block_size):
        block = binary_data[i:i + block_size]
        blocks.append(block)

        # Log block number and data (binary format)
        block_number = i // block_size  # Calculate block number
        block_binary_string = " ".join(format(byte, '08b') for byte in block) # Convert block to string of 0s and 1s
        write_to_debug_log(f"Block {block_number}: {block_binary_string}")

    write_to_debug_log(f"\nNumber of blocks: {len(blocks)}")
    return blocks
# def convert_block_to_words(block):
#     write_to_debug_log("Starting convert_block_to_words")
#     words = []
#     for i in range(0, len(block), 4):
#         word = int.from_bytes(block[i:i + 4], byteorder='little')
#         write_to_debug_log(f"Word: {word}")
#         words.append(word)
#     return words


def convert_block_to_words(block):
    write_to_debug_log("\nStarting convert_block_to_words")
    words = []
    for i in range(0, len(block), 4):
        word_bytes = block[i:i + 4]
        # Explicitly use little-endian
        word = int.from_bytes(word_bytes, byteorder='little')
        word_binary = bin(word)[2:].zfill(32)
        word_number = i // 4
        write_to_debug_log(f"Word {word_number}: {word_binary} (Decimal: {word})")
        words.append(word)
    return words
# def convert_block_to_words(block):
#     """Converts a block to words according to MD5's byte order."""
#     write_to_debug_log("\nStarting convert_block_to_words")
#     words = []
#     for i in range(0, len(block), 4):
#         word_bytes = block[i:i + 4]

#         # MD5 byte order: byte 0, byte 1, byte 2, byte 3
#         # forming word: (byte 3 << 24) | (byte 2 << 16) | (byte 1 << 8) | byte 0
#         word = (word_bytes[3] << 24) | (word_bytes[2] << 16) | (word_bytes[1] << 8) | word_bytes[0]

#         word_binary = bin(word)[2:].zfill(32)
#         word_number = i // 4
#         write_to_debug_log(f"Word {word_number}: {word_binary} (Decimal: {word})")
#         words.append(word)
#     return words

def finalprocess(binary_file):
    write_to_debug_log(f"\nStarting finalprocess for: {binary_file}\n")

    binary_message = preprocess_binary_file(binary_file)
    if binary_message is None:
        write_to_debug_log("\nPreprocessing failed. Exiting.")
        return None, None

    message_blocks = split_into_blocks(binary_message)

    all_blocks_words = []
    for i, block in enumerate(message_blocks):
        write_to_debug_log(f"\nProcessing block {i+1}: {block}")
        block_words = convert_block_to_words(block)
        all_blocks_words.append(block_words)

    write_to_debug_log("""                   <=======finalprocess complete.========>              """)
    print("""                                <=======finalprocess complete.========>                               """)
    return message_blocks, all_blocks_words

if __name__ == "__main__":
    while True:
        file_name=input("Enter the File Name :")
        finalprocess(file_name)