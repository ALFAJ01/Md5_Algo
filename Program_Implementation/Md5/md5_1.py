# import math
# from Pre_P_1 import preprocess_binary_file, split_into_blocks, convert_block_to_words, write_to_debug_log

# class MD5:
#     def __init__(self):
#         self.reset()
#         self.T = [int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

#         write_to_debug_log("\nMD5 Constants (T Values):")
#         for i, value in enumerate(self.T):
#             write_to_debug_log(f"T[{i}] (Decimal): {value} (Binary: {bin(value)[2:].zfill(32)})")

#     def reset(self):
#         self.A = 0x67452301
#         self.B = 0xefcdab89
#         self.C = 0x98badcfe
#         self.D = 0x10325476

#     def _left_rotate(self, x, n):
#         return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

#     def _F(self, x, y, z):
#         return (x & y) | (~x & z)

#     def _G(self, x, y, z):
#         return (x & z) | (y & ~z)

#     def _H(self, x, y, z):
#         return x ^ y ^ z

#     def _I(self, x, y, z):
#         return y ^ (x | ~z)

#     def process_block(self, block):
#         """Process a single 512-bit block with detailed logging."""
#         write_to_debug_log("\nStarting process_block")
#         X = convert_block_to_words(block)

#         A, B, C, D = self.A, self.B, self.C, self.D

#         write_to_debug_log(f"\nInitial State:")
#         write_to_debug_log(f"A: {A:08x} (Binary: {bin(A)[2:].zfill(32)})")
#         write_to_debug_log(f"B: {B:08x} (Binary: {bin(B)[2:].zfill(32)})")
#         write_to_debug_log(f"C: {C:08x} (Binary: {bin(C)[2:].zfill(32)})")
#         write_to_debug_log(f"D: {D:08x} (Binary: {bin(D)[2:].zfill(32)})")

#         def round_function(func, S, start_t, round_num):
#             nonlocal A, B, C, D
#             write_to_debug_log(f"\nStarting Round {round_num}:")
#             for i in range(16):
#                 if func == self._G:
#                     k = (1 + 5 * i) % 16
#                 elif func == self._H:
#                     k = (5 + 3 * i) % 16
#                 elif func == self._I:
#                     k = (7 * i) % 16
#                 else:
#                     k = i
#                 s = S[i % 4]
#                 temp = (A + func(B, C, D) + X[k] + self.T[start_t + i]) & 0xFFFFFFFF
#                 write_to_debug_log(f"\n\tIteration {i+1}:")
#                 write_to_debug_log(f"\tA + f(B,C,D) + X[k] + T[i] = {temp:08x} (Binary: {bin(temp)[2:].zfill(32)})")
#                 A = (B + self._left_rotate(temp, s)) & 0xFFFFFFFF
#                 write_to_debug_log(f"\tLeft Rotate (temp, s) = {A:08x} (Binary: {bin(A)[2:].zfill(32)})")
#                 A, B, C, D = D, A, B, C
#                 write_to_debug_log(f"\tState after iteration {i+1}:")
#                 write_to_debug_log(f"\tA: {A:08x} (Binary: {bin(A)[2:].zfill(32)})")
#                 write_to_debug_log(f"\tB: {B:08x} (Binary: {bin(B)[2:].zfill(32)})")
#                 write_to_debug_log(f"\tC: {C:08x} (Binary: {bin(C)[2:].zfill(32)})")
#                 write_to_debug_log(f"\tD: {D:08x} (Binary: {bin(D)[2:].zfill(32)})")

#         round_function(self._F, [7, 12, 17, 22], 0, 1)
#         round_function(self._G, [5, 9, 14, 20], 16, 2)
#         round_function(self._H, [4, 11, 16, 23], 32, 3)
#         round_function(self._I, [6, 10, 15, 21], 48, 4)

#         self.A = (self.A + A) & 0xFFFFFFFF
#         self.B = (self.B + B) & 0xFFFFFFFF
#         self.C = (self.C + C) & 0xFFFFFFFF
#         self.D = (self.D + D) & 0xFFFFFFFF

#         write_to_debug_log(f"\nState after processing block:")
#         write_to_debug_log(f"A: {self.A:08x} (Binary: {bin(self.A)[2:].zfill(32)})")
#         write_to_debug_log(f"B: {self.B:08x} (Binary: {bin(self.B)[2:].zfill(32)})")
#         write_to_debug_log(f"C: {self.C:08x} (Binary: {bin(self.C)[2:].zfill(32)})")
#         write_to_debug_log(f"D: {self.D:08x} (Binary: {bin(self.D)[2:].zfill(32)})")



import math
from Pre_P_1 import preprocess_binary_file, split_into_blocks, convert_block_to_words, write_to_debug_log

class MD5:
    def __init__(self):
        self.reset()
        self.T = [int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

        write_to_debug_log("\nMD5 Constants (T Values):")
        for i, value in enumerate(self.T):
            write_to_debug_log(f"T[{i:02}] (Hex): {value:08x} (Binary: {bin(value)[2:].zfill(32)})") # Hexadecimal Output

    def reset(self):
        self.A = 0x67452301
        self.B = 0xefcdab89
        self.C = 0x98badcfe
        self.D = 0x10325476

    def _left_rotate(self, x, n):
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
        """Process a single 512-bit block with detailed logging."""
        write_to_debug_log("\nStarting process_block")
        X = convert_block_to_words(block)

        A, B, C, D = self.A, self.B, self.C, self.D

        write_to_debug_log(f"\nInitial State:")
        write_to_debug_log(f"A: {A:08x} (Binary: {bin(A)[2:].zfill(32)})")
        write_to_debug_log(f"B: {B:08x} (Binary: {bin(B)[2:].zfill(32)})")
        write_to_debug_log(f"C: {C:08x} (Binary: {bin(C)[2:].zfill(32)})")
        write_to_debug_log(f"D: {D:08x} (Binary: {bin(D)[2:].zfill(32)})")

        def round_function(func, S, start_t, round_num):
            nonlocal A, B, C, D
            write_to_debug_log(f"\nStarting Round {round_num}:")
            for i in range(16):
                if func == self._G:
                    k = (1 + 5 * i) % 16
                elif func == self._H:
                    k = (5 + 3 * i) % 16
                elif func == self._I:
                    k = (7 * i) % 16
                else:
                    k = i
                s = S[i % 4]
                temp = (A + func(B, C, D) + X[k] + self.T[start_t + i]) & 0xFFFFFFFF
                write_to_debug_log(f"\n\tIteration {i+1}:")
                write_to_debug_log(f"\tA + f(B,C,D) + X[k] + T[i] = {temp:08x} (Binary: {bin(temp)[2:].zfill(32)})") # Hexadecimal Output
                A = (B + self._left_rotate(temp, s)) & 0xFFFFFFFF
                write_to_debug_log(f"\tLeft Rotate (temp, s) = {A:08x} (Binary: {bin(A)[2:].zfill(32)})") # Hexadecimal Output
                A, B, C, D = D, A, B, C
                write_to_debug_log(f"\tState after iteration {i+1}:")
                write_to_debug_log(f"\tA: {A:08x} (Binary: {bin(A)[2:].zfill(32)})") # Hexadecimal Output
                write_to_debug_log(f"\tB: {B:08x} (Binary: {bin(B)[2:].zfill(32)})") # Hexadecimal Output
                write_to_debug_log(f"\tC: {C:08x} (Binary: {bin(C)[2:].zfill(32)})") # Hexadecimal Output
                write_to_debug_log(f"\tD: {D:08x} (Binary: {bin(D)[2:].zfill(32)})") # Hexadecimal Output

        round_function(self._F, [7, 12, 17, 22], 0, 1)
        round_function(self._G, [5, 9, 14, 20], 16, 2)
        round_function(self._H, [4, 11, 16, 23], 32, 3)
        round_function(self._I, [6, 10, 15, 21], 48, 4)

        self.A = (self.A + A) & 0xFFFFFFFF
        self.B = (self.B + B) & 0xFFFFFFFF
        self.C = (self.C + C) & 0xFFFFFFFF
        self.D = (self.D + D) & 0xFFFFFFFF

        write_to_debug_log(f"\nState after processing block:")
        write_to_debug_log(f"A: {self.A:08x} (Binary: {bin(self.A)[2:].zfill(32)})") # Hexadecimal Output
        write_to_debug_log(f"B: {self.B:08x} (Binary: {bin(self.B)[2:].zfill(32)})") # Hexadecimal Output
        write_to_debug_log(f"C: {self.C:08x} (Binary: {bin(self.C)[2:].zfill(32)})") # Hexadecimal Output
        write_to_debug_log(f"D: {self.D:08x} (Binary: {bin(self.D)[2:].zfill(32)})") # Hexadecimal Output

    def digest(self, filename):
        write_to_debug_log(f"\nStarting digest for file {filename}")
        binary_message = preprocess_binary_file(filename)
        if binary_message is None:
            return None

        message_blocks = split_into_blocks(binary_message)

        self.reset()

        for i, block in enumerate(message_blocks):
            write_to_debug_log(f"\nProcessing Block {i + 1}:")
            self.process_block(block)

        digest = (self.A.to_bytes(4, 'little') +
                  self.B.to_bytes(4, 'little') +
                  self.C.to_bytes(4, 'little') +
                  self.D.to_bytes(4, 'little'))

        write_to_debug_log(f"\nMD5 Digest (Bytes): {digest}")
        hex_digest = digest.hex()
        write_to_debug_log(f"\nMD5 Digest (Hex): {hex_digest}")
        return hex_digest


def finalprocess(binary_file):
    md5 = MD5()
    digest = md5.digest(binary_file)
    if digest:
        print(f"MD5 Digest of {binary_file}: {digest}")

if __name__ == "__main__":
    while True:
        file_name = input("Enter the File Name (or 'exit' to quit): ")
        if file_name.lower() == 'exit':
            break
        finalprocess(file_name)