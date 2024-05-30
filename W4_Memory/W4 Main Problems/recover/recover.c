#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // Open memory card file
    FILE *inputFile = fopen(argv[1], "r");
    if (inputFile == NULL)
    {
        fprintf(stderr, "Could not open file %s.\n", argv[1]);
        return 1;
    }

    BYTE buffer[BLOCK_SIZE];
    FILE *outputFile = NULL;
    char filename[8]; // Enough space for "###.jpg" plus null terminator
    int fileCount = 0;

    // Read blocks of 512 bytes until end of card
    while (fread(buffer, BLOCK_SIZE, 1, inputFile) == 1)
    {
        // Check for start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close the previous file if it exists
            if (outputFile != NULL)
            {
                fclose(outputFile);
            }

            // Create a new file
            sprintf(filename, "%03d.jpg", fileCount++);
            outputFile = fopen(filename, "w");
            if (outputFile == NULL)
            {
                fprintf(stderr, "Could not create output JPEG file.\n");
                fclose(inputFile);
                return 1;
            }
        }

        // If a JPEG file is open, write to it
        if (outputFile != NULL)
        {
            fwrite(buffer, BLOCK_SIZE, 1, outputFile);
        }
    }

    // Close any remaining open files
    if (outputFile != NULL)
    {
        fclose(outputFile);
    }

    fclose(inputFile);

    return 0;
}
