#include <stdio.h>
#include <stdlib.h>

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

void convertToBinary(const char *inputFile, const char *outputFile) {
    FILE *input = fopen(inputFile, "rb");  // Open the input file in binary mode
    FILE *output = fopen(outputFile, "w"); // Open the output file in text mode (to write '1's and '0's)

    if (input == NULL) {
        perror("Error opening input file");
        return;
    }

    if (output == NULL) {
        perror("Error opening output file");
        fclose(input);
        return;
    }

    unsigned char ch; // Variable to hold each character
    while (fread(&ch, 1, 1, input) > 0) { // Read one byte at a time
        // Convert the character to its binary representation
        for (int i = 7; i >= 0; i--) {
            fputc(((ch >> i) & 1) ? '1' : '0', output); // Write '1' or '0' to the output file
        }
        fputc(' ', output); // Add a space between binary representations for readability
    }

    fclose(input);
    fclose(output);

    printf("File successfully converted to binary format: %s\n", outputFile);
}

int main() {
     const char *inputFile = "example.txt";  // Replace with your input file name
    const char *outputFile = "ctobin.bin"; // Replace with your output file name

     convertToBinary(inputFile, outputFile);

    int choice;
    printf("\nWould you like to view the file contents?\n");
    printf("1. View text file\n");
    printf("2. View binary file\n");
    printf("3. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            viewFile(inputFile, "r");
            break;
        case 2:
            viewFile(outputFile, "rb");
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
