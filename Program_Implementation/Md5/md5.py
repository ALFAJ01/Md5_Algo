import math
from PreP_data import preprocess_binary_file, split_into_blocks,convert_block_to_words

# MD5 algorithm implementation
class MD5:
    def __init__(self):
        # Initialize MD5 state variables (A, B, C, D)
        self.A = 0x67452301
        self.B = 0xefcdab89
        self.C = 0x98badcfe
        self.D = 0x10325476

        # Precompute T values (constants derived from the sine function)
        self.T = [int(pow(2,32) * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]

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

    def compute_md5(self, filename):
        # Step 1: Preprocess the file
        binary_message = preprocess_binary_file(filename)

        # Step 2: Split into 512-bit blocks
        blocks = split_into_blocks(binary_message)

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

# Example usage
if __name__ == "__main__":
    md5 = MD5()
    hash_result = md5.compute_md5("/home/mr./Pictures/Screenshots/Screenshot_20241114_164044.png")
    hash_resul = md5.compute_md5("/home/mr./Downloads/VideoDownloader/COA/L-1.2： Von Neumann's Architecture ｜ Stored Memory Concept in Computer Architecture.webm")
    print(f"MD5 Hash: {hash_result}")
    print(f"MD5 Hash: {hash_resul}")
