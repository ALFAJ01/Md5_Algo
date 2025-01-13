def count_bits_in_binary_file(filename):
    try:
        # Open the binary file in read mode
        with open(filename, 'rb') as f:
            # Read the entire file
            file_content = f.read()
            
            # Calculate the number of bits (each byte has 8 bits)
            num_bits = len(file_content) * 8
            
            print(f"The binary file '{filename}' contains {num_bits} bits.")
            return num_bits
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
count_bits_in_binary_file("Bin.bin")
count_bits_in_binary_file("Example.txt")