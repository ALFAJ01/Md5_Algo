import os

# def convert_to_binary(filename, newfilename=None, encoding='utf-8'):
#     try:
#         with open(filename, 'r', encoding=encoding) as f:
#             pass  # Check if encoding is valid
#     except (UnicodeEncodeError, UnicodeDecodeError):
#         print(f"Invalid encoding: {encoding}. Using 'utf-8' encoding by default.")
#         encoding = 'utf-8'

#     # Add .bin extension if not provided
#     if not newfilename.endswith('.bin'):
#         newfilename += '.bin'
    
#     # Check if file already exists
#     if os.path.exists(newfilename):
#         user_choice = input(f"The file '{newfilename}' already exists. Do you want to (O)verride or (C)hange the filename? (O/C): ").strip().lower()
#         if user_choice == 'c':
#             newfilename = input("Enter the new filename: ").strip()
#             if not newfilename.endswith('.bin'):
#                 newfilename += '.bin'
#         elif user_choice != 'o':
#             print("Invalid choice. Exiting program.")
#             return
    
#     try:
#         with open(filename, 'r', encoding=encoding) as f1:
#             lines = f1.readlines()
#             with open(newfilename, 'wb') as f2:
#                 for line in lines:
#                     pickle.dump(line, f2)
#         print(f'Text file "{filename}" converted to binary file "{newfilename}" successfully!')
#     except FileNotFoundError:
#         print('File not found. Please try again.')

# def read_binary_and_convert_to_text(filename):
#     converted_text = ""
#     try:
#         with open(filename, 'rb') as f:
#             while True:
#                 try:
#                     line = pickle.load(f)
#                     converted_text += line
#                 except EOFError:
#                     break
#         print("\nFile read successfully from binary to txt format!")
#         return converted_text
#     except FileNotFoundError:
#         print('File not found. Please try again.')
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
        return newfilename
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
def convert_binary_to_text_raw(bin_filename, txt_filename=None, encoding='utf-8'):
    try:
        # Check if txt_filename is provided; if not, generate one from the bin filename
        if not txt_filename:
            txt_filename = bin_filename.replace('.bin', '.txt')

        # Open the binary file for reading
        with open(bin_filename, 'rb') as bin_file:
            # Read the raw binary content
            binary_content = bin_file.read()

            # Decode the binary content into a text string using the specified encoding
            decoded_content = binary_content.decode(encoding)

        # Write the decoded text to a text file
        with open(txt_filename, 'w', encoding=encoding) as txt_file:
            txt_file.write(decoded_content)

        print(f"Binary file '{bin_filename}' converted to text file '{txt_filename}' successfully!")
        return txt_filename

    except FileNotFoundError:
        print(f"Binary file '{bin_filename}' not found. Please try again.")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode the binary file with {encoding} encoding.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
def verify_conversion(original_txt_file, binary_file):
    print("\n===== Verifying Conversion =====\n")

    try:
        with open(binary_file, 'r', encoding='utf-8') as f2:
             converted_text =convert_binary_to_text_raw(binary_file)
             print(f"Binary Converted Text File Content:\n{converted_text}")
        with open(original_txt_file, 'r', encoding='utf-8') as f1:
            original_text = f1.read()
            print(f"Original Text File Content:\n{original_text}")
    except FileNotFoundError:
        print(f'Original text file "{original_txt_file}" not found. Please try again.')
        return

    if original_text == converted_text:
        print("\nThe original text file and the converted binary file match!")
    else:
        print("\nThe original text file and the converted binary file do not match.")

filename = input('Enter the name of the text file you want to convert: ').strip()
newfilename = input('Enter the name for the converted binary file (or press Enter to keep the default): ').strip()
binary_file=convert_text_to_binary_raw(filename, newfilename)
verify_conversion(filename ,binary_file)
# count_bits_in_binary_file(binary_file)
# convert_binary_to_text_raw('Bin.bin', '11.txt')


# def read_binary_as_zeros_ones_hex(filename):
#     try:
#         with open(filename, 'rb') as f:
#             print(f"Reading binary file '{filename}' in binary format (1's and 0's):")
#             byte = f.read(1)
#             while byte:
#                 binary_rep = bin(ord(byte))[2:].zfill(8)
#                 print(binary_rep, end=' ')
#                 byte = f.read(1)
#             print("\nFile read successfully in binary 1's and 0's format!")

#             # Hexadecimal format
#         with open(filename, "rb") as file:
#             print(f"Reading binary file: {filename}")

#             # Read the file byte by byte
#             byte = file.read(1)
#             while byte:
#                 byte_value = ord(byte)
#                 # Print the byte in hexadecimal format
#                 print(f"{byte_value:02X}", end=' ')
#                 byte = file.read(1)

#             print("\nEnd of file read succesfully in hexdecimal format!.")
#     except FileNotFoundError:
#         print('File not found. Please try again.')

# def read_file(filename):
#     if not os.path.exists(filename):
#         print(f"File '{filename}' not found.")
#         return

#     file_extension = filename.split('.')[-1].lower()

#     if file_extension == 'txt':
#         try:
#             with open(filename, 'r', encoding='utf-8') as f:
#                 print(f"Reading text file: {filename}")
#                 print(f.read())
#         except FileNotFoundError:
#             print(f"File '{filename}' not found.")
#         except UnicodeDecodeError:
#             print(f"Error: Unable to read file '{filename}' due to encoding issues.")
    
#     elif file_extension == 'bin':
#         try:
#             read_binary_and_convert_to_text(filename)
#         except FileNotFoundError:
#             print(f"File '{filename}' not found.")
    
#     else:
#         print(f"Unsupported file format: {file_extension}. Please provide a .txt or .bin file.")

# def verify_conversion(original_txt_file, binary_file):
#     print("\n===== Verifying Conversion =====\n")

#     try:
#         with open(binary_file, 'r', encoding='utf-8') as f2:
#              converted_text = f2.read()
#         with open(original_txt_file, 'r', encoding='utf-8') as f1:
#             original_text = f1.read()
#             print(f"Original Text File Content:\n{original_text}")
#     except FileNotFoundError:
#         print(f'Original text file "{original_txt_file}" not found. Please try again.')
#         return

#     if original_text == converted_text:
#         print("\nThe original text file and the converted binary file match!")
#     else:
#         print("\nThe original text file and the converted binary file do not match.")

def main():
    while True:
        print('\n========== File Conversion and Verification Program ==========')
        print('1. Convert a Text file to Binary file')
        print('2. Verify if the text and binary files match')
        print('3. Read a file (Text/Binary)')
        print("4. Read Binary file into 1's and 0's format and hexadecimal Format.")
        print('5. Exit')
    
        
        choice = input('Enter your choice (1-4): ').strip()
        
        if choice == '1':
            filename = input('Enter the name of the text file you want to convert: ').strip()
            newfilename = input('Enter the name for the converted binary file (or press Enter to keep the default): ').strip()
            if not newfilename:
                newfilename = filename.split('.')[0] + '.bin'  # Default to .bin if not provided
            convert_to_binary(filename, newfilename)

        elif choice == '2':
            original_txt_file = input('Enter the name of the original text file: ').strip()
            binary_file = input('Enter the name of the converted binary file: ').strip()
            verify_conversion(original_txt_file, binary_file)

        elif choice == '3':
            filename = input('Enter the file name you want to read: ').strip()
            read_file(filename)
        elif choice=="4":
            filename = input('Enter the file name you want to read: ').strip()
            read_binary_as_zeros_ones_hex(filename)

        elif choice == '5':
            print('Exiting program. Goodbye!')
            break

        else:
            print('Invalid choice. Please try again.')

# Run the main function
# main()
