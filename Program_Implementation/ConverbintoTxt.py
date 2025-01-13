def binary_to_text(binary_filename, text_filename):
    try:
        with open(binary_filename, "rb") as bin_file:
            # Open the text file to write the content
            with open(text_filename, "w") as txt_file:
                byte = bin_file.read(1)
                while byte:
                    # Write each byte as its ASCII representation (text)
                    txt_file.write(chr(ord(byte)))  # Convert byte to its character representation
                    byte = bin_file.read(1)
                
                print(f"Binary file {binary_filename} has been converted to text file {text_filename}.")
    
    except FileNotFoundError:
        print(f"Error: File {binary_filename} not found.")
    except Exception as e:
        print(f"Error: {e}")
import pickle

import pickle

def read_binary_and_convert_to_text(filename, output_filename):
    try:
        with open(filename, 'rb') as f:
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                while True:
                    try:
                        line = pickle.load(f)
                        output_file.write(line)  # Write each line to the new text file
                    except EOFError:
                        break
        print(f"\nFile read successfully and written to {output_filename}!")
    except FileNotFoundError:
        print('File not found. Please try again.')

# Example usage
# ('example.bin', 'output.txt')


# Example usage



def main():
    # Ask the user for the binary file and text file names
    binary_filename = input("Enter the name of the binary file: ")
    text_filename = input("Enter the name for the output text file: ")

    # Convert binary file to text file
    read_binary_and_convert_to_text(binary_filename, text_filename)
    # read_binary_and_convert_to_text('22')

if __name__ == "__main__":
    main()
