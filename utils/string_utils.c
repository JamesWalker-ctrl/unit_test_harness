// utils/string_utils.c

#include <ctype.h>
#include <string.h>

// Capitalizes the first character and lowercases the rest
void capitalize(const char* input, char* output) {
    size_t len = strlen(input);
    if (len == 0) {
        output[0] = '\0';
        return;
    }

    output[0] = toupper(input[0]);
    for (size_t i = 1; i < len; ++i) {
        output[i] = tolower(input[i]);
    }
    output[len] = '\0';
}
