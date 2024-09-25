#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char input_str[100];
    printf("역변환할 문자열을 입력하세요: ");
    fgets(input_str, sizeof(input_str), stdin);
    input_str[strcspn(input_str, "\n")] = '\0';

    int len = strlen(input_str);
    for (int i = 0; i < len; i++) {
        char ch = input_str[i];
        if (isalpha(ch)) {
            int shift = i + 1;
            char new_char = ch - shift;
            if (islower(ch)) {
                if (new_char < 'a') {
                    new_char += 26;
                }
            } else if (isupper(ch)) {
                if (new_char < 'A') {
                    new_char += 26;
                }
            }
            input_str[i] = new_char;
        }
    }
    printf("변환된 문자열: %s\n", input_str);

    return 0;
}
