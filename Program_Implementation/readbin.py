# Function to read and display the content of a binary file in both hexadecimal and binary formats
def read_binary_file(filename):
    try:
        with open(filename, "rb") as file:
            print(f"Reading binary file: {filename}")

            # Read the file byte by byte
            byte = file.read(1)
            while byte:
                byte_value = ord(byte)

                # Print the byte in binary format
                print(f"Binary: {bin(byte_value)[2:].zfill(8)}", end=" ")

                # Print the byte in hexadecimal format
                print(f"Hexadecimal: {byte_value:02X}")

                byte = file.read(1)

            print("\nEnd of file reached.")
    except FileNotFoundError:
        print("Error opening file")

def main():
    # Ask the user for the binary file name
    filename = input("Enter the name of the .bin file to read: ")

    # Call the function to read and display the binary file content
    read_binary_file(filename)

if __name__ == "__main__":
    main()
