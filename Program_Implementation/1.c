#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Function to convert text file to binary file (serialize content)
void convert(const char *filename, const char *newfilename) {
    FILE *inFile = fopen(filename, "r");
    if (inFile == NULL) {
        printf("File not found, please try again\n");
        sleep(1);
        return;
    }

    FILE *outFile = fopen(newfilename, "wb");
    if (outFile == NULL) {
        printf("Error opening new file for writing\n");
        fclose(inFile);
        return;
    }

    char line[1024];
    while (fgets(line, sizeof(line), inFile)) {
        // Write each line as a binary block
        size_t lineLength = strlen(line) + 1;  // Include null terminator
        fwrite(&lineLength, sizeof(size_t), 1, outFile);  // Write length of line
        fwrite(line, sizeof(char), lineLength, outFile);  // Write the line content
    }

    printf("Text file %s converted to %s successfully!\n", filename, newfilename);
    fclose(inFile);
    fclose(outFile);
    sleep(2);
}

// Function to read binary file and display its contents
void fileread(const char *filename) {
    FILE *inFile = fopen(filename, "rb");
    if (inFile == NULL) {
        printf("File not found, please try again\n");
        sleep(1);
        return;
    }

    printf("========= The contents of the file %s are: \n", filename);
    size_t lineLength;
    char *line = NULL;

    // Read and print each line in binary file
    while (fread(&lineLength, sizeof(size_t), 1, inFile) == 1) {
        line = (char *)malloc(lineLength);
        if (line == NULL) {
            printf("Memory allocation error\n");
            fclose(inFile);
            return;
        }
        fread(line, sizeof(char), lineLength, inFile);
        printf("%s", line);
        free(line);  // Free the allocated memory for the line
    }

    printf("\n ========= File read successfully! ========= \n");
    fclose(inFile);
    sleep(1);
}

int main() {
    char filename[256], newfilename[256];
    char choice;

    while (1) {
        printf("========== C Text to Binary file converter program ==========\n");
        printf("1. Convert a Text file to Binary file\n");
        printf("2. Read any Binary file\n");
        printf("3. Exit.\n");
        printf("Enter your choice: 1-3: ");
        scanf(" %c", &choice);
        getchar();  // To consume the newline character left by scanf

        if (choice == '1') {
            printf("Enter the name of the text file you want to convert: ");
            fgets(filename, sizeof(filename), stdin);
            filename[strcspn(filename, "\n")] = 0;  // Remove newline character from input

            printf("Enter the name for the converted file: ");
            fgets(newfilename, sizeof(newfilename), stdin);
            newfilename[strcspn(newfilename, "\n")] = 0;  // Remove newline character

            convert(filename, newfilename);
        } else if (choice == '2') {
            printf("Enter the name of the Binary file you want to read: ");
            fgets(filename, sizeof(filename), stdin);
            filename[strcspn(filename, "\n")] = 0;  // Remove newline character

            fileread(filename);
        } else if (choice == '3') {
            printf("Thank you!\n");
            break;
        } else {
            printf("Incorrect input, please try again...\n");
            sleep(2);
        }
    }

    return 0;
}
