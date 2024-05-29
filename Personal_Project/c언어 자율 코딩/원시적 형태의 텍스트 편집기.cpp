#include <stdio.h>
#include <string.h>

int main() {
    FILE *file_pointer;
    char input[1000];
    char filename[100];
    int flag;

    printf("생성할 메모장 파일의 이름을 입력 (확장자명 포함): ");
    fgets(filename, sizeof(filename), stdin);

    filename[strcspn(filename, "\n")] = '\0';

    file_pointer = fopen(filename, "w");

    if (file_pointer == NULL) {
        printf("error\n");
    }

    printf("편집기에 작성할 내용을 입력. 끝내려면 엔터를 두 번:\n");

    do {
        fgets(input, sizeof(input), stdin);
        if (input[0] == '\n') {
            flag = 0;
        } else {
            flag = 1;
        }
        if (flag) {
            fprintf(file_pointer, "%s", input);
        }
    } while (flag);

    fclose(file_pointer);

    printf("%s 파일이 생성 완료.\n", filename);

    return 0;
}
