#include <stdio.h>
#include <stdlib.h>

// Function to convert binary file back to text file
void convertToText(const char *inputFile, const char *outputFile) {
    FILE *input = fopen(inputFile, "rb");  // Open the input binary file
    FILE *output = fopen(outputFile, "w"); // Open the output text file

    if (input == NULL) {
        perror("Error opening input binary file");
        return;
    }

    if (output == NULL) {
        perror("Error opening output text file");
        fclose(input);
        return;
    }

    unsigned char byte;
    unsigned char ch = 0;
    int bitCount = 0;

    // Read the binary file byte by byte
    while (fread(&byte, 1, 1, input) > 0) {
        // Convert the byte into its 8-bit binary representation
        for (int i = 7; i >= 0; i--) {
            // Get each bit of the byte and set it in the correct place in 'ch'
            ch = (ch << 1) | ((byte >> i) & 1);
            bitCount++;

            // Once we've collected 8 bits, write the character to the output file
            if (bitCount == 8) {
                fputc(ch, output);  // Write the decoded character
                bitCount = 0;
                ch = 0;
            }
        }
    }

    fclose(input);
    fclose(output);

    printf("File successfully converted back to text format: %s\n", outputFile);
}

// Function to view the contents of a file in text or binary format
void viewFile(const char *fileName, const char *mode) {
    FILE *file = fopen(fileName, mode);
    if (file == NULL) {
        perror("Error opening file to view");
        return;
    }

    if (mode[0] == 'r') { // Text mode
        char ch;
        printf("\n--- Text File Content (%s) ---\n", fileName);
        while ((ch = fgetc(file)) != EOF) {
            putchar(ch);
        }
        printf("\n--- End of File ---\n\n");
    } else if (mode[0] == 'r' && mode[1] == 'b') { // Binary mode
        unsigned char byte;
        printf("\n--- Binary File Content (%s) in Binary Format ---\n", fileName);
        while (fread(&byte, 1, 1, file) > 0) {
            for (int i = 7; i >= 0; i--) {
                printf("%d", (byte >> i) & 1); // Display each bit
            }
            printf(" ");
        }
        rewind(file);
        printf("\n--- Binary File Content (%s) in Hexadecimal Format ---\n", fileName);
        while (fread(&byte, 1, 1, file) > 0) {
            printf("%02X ", byte); // Display byte in hexadecimal format
        }
        printf("\n--- End of File ---\n\n");
    }

    fclose(file);
}

int main() {
    const char *inputBinaryFile = "ctobin.bin";  // Replace with your input binary file name
    const char *outputTextFile = "converted_text.txt"; // Replace with your output text file name

    // Convert binary to text
    convertToText(inputBinaryFile, outputTextFile);

    int choice;
    printf("\nWould you like to view the file contents?\n");
    printf("1. View text file\n");
    printf("2. View binary file\n");
    printf("3. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            viewFile(outputTextFile, "r");
            break;
        case 2:
            viewFile(inputBinaryFile, "rb");
            break;
        case 3:
            printf("Exiting program.\n");
            break;
        default:
            printf("Invalid choice. Exiting program.\n");
            break;
    }

    return 0;
}
