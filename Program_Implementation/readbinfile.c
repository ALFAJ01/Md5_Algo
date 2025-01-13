#include <stdio.h>
#include <stdlib.h>
#include <string.h>  // Add this to use strcspn()

// Function to read and display the content of a binary file
void readBinaryFile(const char *filename) {
    FILE *file = fopen(filename, "rb");  // Open file in binary mode

    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    unsigned char byte;  // Variable to hold each byte read from the file
    printf("Reading binary file: %s\n", filename);

    // Read the file byte by byte
    while (fread(&byte, sizeof(byte), 1, file)) {
        // Print each byte in hexadecimal format
        printf("%02X ", byte);
    }
    
    printf("\nEnd of file reached.\n");
    fclose(file);
}

int main() {
    char filename[256];

    // Ask the user for the binary file name
    printf("Enter the name of the .bin file to read: ");
    fgets(filename, sizeof(filename), stdin);
    filename[strcspn(filename, "\n")] = 0;  // Remove newline character if present

    // Call the function to read and display the binary file content
    readBinaryFile(filename);

    return 0;
}
