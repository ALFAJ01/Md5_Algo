import os
import pickle

def convert_to_binary(filename, newfilename=None, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as f:
            pass  # Check if encoding is valid
    except (UnicodeEncodeError, UnicodeDecodeError):
        print(f"Invalid encoding: {encoding}. Using 'utf-8' encoding by default.")
        encoding = 'utf-8'
    
    # Add .bin extension if not provided
    if not newfilename.endswith('.bin'):
        newfilename += '.bin'
    
    # Check if file already exists
    if os.path.exists(newfilename):
        user_choice = input(f"The file '{newfilename}' already exists. Do you want to (O)verride or (C)hange the filename? (O/C): ").strip().lower()
        if user_choice == 'c':
            newfilename = input("Enter the new filename: ").strip()
            if not newfilename.endswith('.bin'):
                newfilename += '.bin'
        elif user_choice != 'o':
            print("Invalid choice. Exiting program.")
            return
    
    try:
        with open(filename, 'r', encoding=encoding) as f1:
            lines = f1.readlines()
            with open(newfilename, 'wb') as f2:
                for line in lines:
                    pickle.dump(line, f2)  # Write line to binary file
        print(f'Text file "{filename}" converted to binary file "{newfilename}" successfully!')
    except FileNotFoundError:
        print('File not found. Please try again.')

def read_binary_and_convert_to_text(filename):
    converted_text = ""
    try:
        with open(filename, 'rb') as f:
            while True:
                try:
                    line = pickle.load(f)  # Read line from binary file
                    converted_text += line  # Accumulate the text
                except EOFError:
                    break
        print("\nFile read successfully from binary to txt format!")
        return converted_text
    except FileNotFoundError:
        print('File not found. Please try again.')

def verify_conversion(original_txt_file, binary_file):
    print("\n===== Verifying Conversion =====\n")

    try:
        # Read and convert the binary file to text
        converted_text = read_binary_and_convert_to_text(binary_file)

        # Read the original text file for comparison
        with open(original_txt_file, 'r', encoding='utf-8') as f1:
            original_text = f1.read()
            print(f"Original Text File Content:\n{original_text}")
        
        print(f"Binary Converted Text File Content:\n{converted_text}")

    except FileNotFoundError:
        print(f'Original text file "{original_txt_file}" not found. Please try again.')
        return

    # Compare both texts to check if they match
    if original_text == converted_text:
        print("\nThe original text file and the converted binary file match!")
    else:
        print("\nThe original text file and the converted binary file do not match.")

filename = input('Enter the name of the text file you want to convert: ').strip()
newfilename = input('Enter the name for the converted binary file (or press Enter to keep the default): ').strip()
convert_to_binary(filename, newfilename)
original_message = input('Enter the name of the text file you want to convert: ').strip()
binary_message = input('Enter the name for the converted binary file (or press Enter to keep the default): ').strip()
verify_conversion(original_message, binary_message)
