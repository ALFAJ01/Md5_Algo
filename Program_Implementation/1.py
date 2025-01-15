
import os
import math
from datetime import datetime
import os
from PreP_data import preprocess_data, split_into_blocks, convert_block_to_words

def preprocess_data(data, is_file=True):
    """
    Preprocess input data for MD5 hashing.

    Args:
        data: The input data (string or file path).
        is_file: Boolean indicating whether the input is a file path or instance data.

    Returns:
        Binary data ready for MD5 hashing.
    """
    if is_file:
        try:
            with open(data, 'rb') as f:
                binary_data = f.read()
        except FileNotFoundError:
            print(f"Error: File '{data}' not found.")
            return None
    else:
        # Convert string to bytes
        binary_data = data.encode('utf-8')

    original_length = len(binary_data) * 8  # Length in bits

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

class MD5:
    def __init__(self):
        # Initialize MD5 state variables (A, B, C, D)
        self.reset()

        # Precompute T values (constants derived from the sine function)
        self.T = [int(pow(2, 32) * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]

    def reset(self):
        """Reset MD5 internal state variables."""
        self.A = 0x67452301
        self.B = 0xefcdab89
        self.C = 0x98badcfe
        self.D = 0x10325476

    def _left_rotate(self, x, n):
        """Left-rotate a 32-bit integer x by n positions."""
        return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

    def _F(self, x, y, z):
        return (x & y) | (~x & z)

    def _G(self, x, y, z):
        return (x & z) | (y & ~z)

    def _H(self, x, y, z):
        return x ^ y ^ z

    def _I(self, x, y, z):
        return y ^ (x | ~z)

    def process_block(self, block):
        """Process a single 512-bit block."""
        X = convert_block_to_words(block)  # Convert block to 16 32-bit words

        # Save current state
        A, B, C, D = self.A, self.B, self.C, self.D

        # Round 1
        S = [7, 12, 17, 22]
        for i in range(16):
            k = i
            s = S[i % 4]
            A = (B + self._left_rotate(A + self._F(B, C, D) + X[k] + self.T[i], s)) & 0xFFFFFFFF
            A, B, C, D = D, A, B, C

        # Round 2
        S = [5, 9, 14, 20]
        for i in range(16):
            k = (1 + 5 * i) % 16
            s = S[i % 4]
            A = (B + self._left_rotate(A + self._G(B, C, D) + X[k] + self.T[16 + i], s)) & 0xFFFFFFFF
            A, B, C, D = D, A, B, C

        # Round 3
        S = [4, 11, 16, 23]
        for i in range(16):
            k = (5 + 3 * i) % 16
            s = S[i % 4]
            A = (B + self._left_rotate(A + self._H(B, C, D) + X[k] + self.T[32 + i], s)) & 0xFFFFFFFF
            A, B, C, D = D, A, B, C

        # Round 4
        S = [6, 10, 15, 21]
        for i in range(16):
            k = (7 * i) % 16
            s = S[i % 4]
            A = (B + self._left_rotate(A + self._I(B, C, D) + X[k] + self.T[48 + i], s)) & 0xFFFFFFFF
            A, B, C, D = D, A, B, C

        # Update state variables
        self.A = (self.A + A) & 0xFFFFFFFF
        self.B = (self.B + B) & 0xFFFFFFFF
        self.C = (self.C + C) & 0xFFFFFFFF
        self.D = (self.D + D) & 0xFFFFFFFF

    def compute_md5(self, data, is_file=True):
        """
        Compute the MD5 hash for the given input.

        Args:
            data: The input data (string or file path).
            is_file: Boolean indicating whether the input is a file path or instance data.

        Returns:
            The MD5 hash as a hexadecimal string.
        """
        # Step 1: Preprocess the data
        binary_data = preprocess_data(data, is_file)
        if binary_data is None:
            return None

        # Step 2: Split into 512-bit blocks
        blocks = split_into_blocks(binary_data)

        # Step 3: Process each block
        for block in blocks:
            self.process_block(block)

        # Step 4: Produce the final digest (A, B, C, D in little-endian format)
        digest = (
            self.A.to_bytes(4, byteorder='little') +
            self.B.to_bytes(4, byteorder='little') +
            self.C.to_bytes(4, byteorder='little') +
            self.D.to_bytes(4, byteorder='little')
        )

        # Convert to hexadecimal string
        return ''.join(f'{byte:02x}' for byte in digest)

if __name__ == "__main__":
    md5 = MD5()

    while True:
        print("\nSelect input type:")
        print("1. File")
        print("2. Text Stream")
        print("3. Exit")
        md5.reset()

        choice = input("Enter your choice: ")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if choice == '1':
            file_path = input("Enter the file path: ")
            try:
                hash_result = md5.compute_md5(file_path)
                if hash_result:
                    print(f"MD5 Hash: {hash_result}")
                    
                    binary_output_path = f"{file_path}_binary_{timestamp}.bin"
                    txt_output_path = f"{file_path}_text_{timestamp}.txt"
                    hash_file = f"{file_path}_hash_{timestamp}.txt"

                    with open(binary_output_path, 'wb') as bin_file, open(file_path, 'rb') as original_file:
                        bin_file.write(original_file.read())

                    with open(txt_output_path, 'w') as txt_file:
                        with open(file_path, 'rb') as original_file:
                            txt_file.write(original_file.read().decode('utf-8', errors='replace'))

                    with open(hash_file, 'w') as hash_txt:
                        hash_txt.write(hash_result)

                    print(f"Binary file saved: {binary_output_path} ({os.path.getsize(binary_output_path)} bytes)")
                    print(f"Text file saved: {txt_output_path} ({os.path.getsize(txt_output_path)} bytes)")

            except FileNotFoundError:
                print("Error: File not found.")
            except PermissionError:
                print("Error: Permission denied.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif choice == '2':
            text_data = input("Enter the text data: ")
            hash_result = md5.compute_md5(text_data, is_file=False)
            if hash_result:
                print(f"MD5 Hash: {hash_result}")
                
                binary_output_path = f"text_binary_{timestamp}.bin"
                txt_output_path = f"text_output_{timestamp}.txt"
                hash_file = f"text_hash_{timestamp}.txt"

                with open(binary_output_path, 'wb') as bin_file:
                    bin_file.write(text_data.encode('utf-8'))

                with open(txt_output_path, 'w') as txt_file:
                    txt_file.write(text_data)

                with open(hash_file, 'w') as hash_txt:
                    hash_txt.write(hash_result)

                print(f"Binary file saved: {binary_output_path}")
                print(f"Text file saved: {txt_output_path}")

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
