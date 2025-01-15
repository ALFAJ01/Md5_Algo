def binary_to_original(binary_filename, output_filename):
    """
    Reads a binary file (containing byte data, not a string of '1's and '0's)
    and writes it to an output file, effectively reversing the previous process.

    Args:
        binary_filename (str): Path to the binary file.
        output_filename (str): Path to the output file (original data).
    """
    try:
        with open(binary_filename, 'rb') as binary_file, open(output_filename, 'wb') as output_file:
            binary_data = binary_file.read()
            output_file.write(binary_data)  # Directly write the bytes

        print(f"File successfully restored to: {output_filename}")
        return True

    except FileNotFoundError:
        print(f"Error: Binary file '{binary_filename}' not found.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


def read_and_write_binary_file(filename_read, filename_write):
    """
    Reads binary data from a file, prints it in 8-bit groups (optional), and writes it back
    to a new file.

    Args:
        filename_read (str): Path to the file to read from.
        filename_write (str): Path to the written file.
    """

    try:
        with open(filename_read, 'rb') as f_read, open(filename_write, 'wb') as f_write:
            file_content = f_read.read()

            binary_string = ""
            for byte in file_content:
                byte_string = format(byte, '08b')
                f_write.write(byte_string)
                print(byte_string, end=" ")  # Print in 8-bit groups (optional)
                binary_string += byte_string

            # f_write.write(file_content)  # Write the original binary data

            num_bits = len(binary_string)
            print(f"\nThe message length: {num_bits}")

        return True

    except FileNotFoundError:
        print(f"Error: File '{filename_read}' not found.")
        return False

# Example Usage (Demonstrates the round trip):
original_filename = "/home/mr./Downloads/20241115_163705.jpg"  # Replace with your actual file
binary_output_filename = "output.bin"
restored_filename = "restored_image.jpg"

if read_and_write_binary_file(original_filename, binary_output_filename):
    if binary_to_original(binary_output_filename, restored_filename):
        print("Restoration process complete.")
    else:
        print("Restoration process failed.")
else:
    print("Binary file writing failed.")


original_filename_text = "test.txt"  # Replace with your actual file
binary_output_filename_text = "output_text.bin"
restored_filename_text = "restored_text.txt"

if read_and_write_binary_file(original_filename_text, binary_output_filename_text):
    if binary_to_original(binary_output_filename_text, restored_filename_text):
        print("Restoration process complete for text file.")
    else:
        print("Restoration process failed for text file.")
else:
    print("Binary file writing failed for text file.")
# original_filename_text = "/home/mr./Downloads/wbpsc.ucanapply.com_process-hallticket-page_eyJpdiI6InhSSW94NWRVbk5lenBmMTQ4aVZtNEE9PSIsInZhbHVlIjoiOGZZKytPMGNXaEVMXC9EdWNnYU1ZQ0E9PSIsIm1hYyI6IjJmNWU5YjY0OGQ4NDE1Y2RmNDZjZDU4MzM4N2Y5ODI0YWNhMjIzN2E1NTNhYzRlMzI1ZjFkNTZmNGQzNjEyMGMifQ==_eyJpdiI6IkZVdj.pdf"
# binary_output_filename_text = "output_text_bin.bin"
# restored_filename_text = "restored_text.pdf"
# if read_and_write_binary_file(original_filename_text, binary_output_filename_text):
#     if binary_to_original(binary_output_filename_text, restored_filename_text):
#         print("Restoration process complete for text file.")
#     else:
#         print("Restoration process failed for text file.")
# else:
#     print("Binary file writing failed for text file.")
# original_filename_text = "/home/mr./Downloads/VideoDownloader/Comp Desig/Lec-1： Compiler Design Syllabus Discussion for Competitive & College⧸University Exams.webm"
# binary_output_filename_text = "output_video_bin.bin"
# restored_filename_text = "restored_Video.webm"

# if read_and_write_binary_file(original_filename_text, binary_output_filename_text):
#     if binary_to_original(binary_output_filename_text, restored_filename_text):
#         print("Restoration process complete for text file.")
#     else:
#         print("Restoration process failed for text file.")
# else:
#     print("Binary file writing failed for text file.")