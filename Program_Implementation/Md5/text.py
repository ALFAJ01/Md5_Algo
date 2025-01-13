import os

def convert_text_to_binary_raw(filename, newfilename=None, encoding='utf-8'):
    try:
        # Check if the file exists
        if not os.path.exists(filename):
            print(f"File '{filename}' not found.")
            return
        
        # Add .bin extension if not provided
        if not newfilename.endswith('.bin'):
            newfilename += '.bin'
        
        # Open the text file and read the content
        with open(filename, 'r', encoding=encoding) as f:
            content = f.read()
        
        # Write the raw content (encoded) to a binary file
        with open(newfilename, 'wb') as f:
            f.write(content.encode(encoding))  # Encoding the content to binary bytes
        
        print(f"Text file '{filename}' successfully converted to binary file '{newfilename}' using {encoding} encoding.")
    
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

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

# Example usage:
text_filename = "Example.txt"
binary_filename = "Bin.bin"

# Convert text file to binary using raw encoding
convert_text_to_binary_raw(text_filename, binary_filename, encoding='utf-8')

# Count bits in the new binary file
count_bits_in_binary_file(binary_filename)
