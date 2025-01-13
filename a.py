import os

def create_and_write_file(file_name):
    """Creates a file and writes initial content."""
    with open(file_name, 'w') as file:
        file.write("This is the first line.\n")
        file.write("This is the second line.\n")
    print(f"File '{file_name}' created and written successfully.")

def read_file(file_name):
    """Reads the content of a file."""
    with open(file_name, 'r') as file:
        content = file.read()
    print(f"Content of '{file_name}':\n{content}")
    return content

def modify_file(file_name, additional_content):
    """Modifies the file by adding new content."""
    with open(file_name, 'a') as file:
        file.write(additional_content + "\n")
    print(f"File '{file_name}' modified successfully.")

def delete_word_from_file(file_name, word_to_delete):
    """Deletes a specific word from the file content."""
    with open(file_name, 'r') as file:
        content = file.read()

    words = content.split()
    updated_content = ' '.join(word for word in words if word != word_to_delete)

    with open(file_name, 'w') as file:
        file.write(updated_content)

    print(f"Word '{word_to_delete}' deleted from '{file_name}' successfully.")

def convert_to_binary_file(text_file, binary_file):
    """Converts a text file to binary format."""
    with open(text_file, 'r') as file:
        content = file.read()

    with open(binary_file, 'wb') as binary:
        binary.write(content.encode())

    print(f"File '{text_file}' converted to binary file '{binary_file}'.")

def main():
    text_file = "example.txt"
    binary_file = "example.bin"

    # 1. Create and write to a file
    create_and_write_file(text_file)

    # 2. Read the file
    content = read_file(text_file)

    # 3. Modify the file
    additional_content = "This is a new line added during modification."
    modify_file(text_file, additional_content)

    # 4. Append to the file
    append_content = "This is an appended line."
    modify_file(text_file, append_content)

    # 5. Delete a specific word
    word_to_delete = "second"
    delete_word_from_file(text_file, word_to_delete)

    # 6. Convert text file to binary format
    convert_to_binary_file(text_file, binary_file)

if __name__ == "__main__":
    main()
