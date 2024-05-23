#include <stdio.h>
#include <string.h>

int main() {
    FILE *file_pointer;
    char input[1000];
    char filename[100];
    int flag;

    printf("생성할 메모장 파일의 이름을 입력하세요 (확장자를 포함하여): ");
    fgets(filename, sizeof(filename), stdin);

    filename[strcspn(filename, "\n")] = '\0';

    file_pointer = fopen(filename, "w");

    if (file_pointer == NULL) {
        printf("파일을 열 수 없습니다.\n");
        return 1;
    }

    printf("메모장에 작성할 내용을 입력하세요. 작성을 마치려면 엔터를 두 번 누르세요:\n");

    do {
        fgets(input, sizeof(input), stdin);
        // 사용자가 엔터만 입력하면 종료
        flag = (input[0] == '\n') ? 0 : 1;
        // 엔터가 아닌 경우에만 파일에 입력 내용을 저장
        if (flag) {
            fprintf(file_pointer, "%s", input);
        }
    } while (flag);

    fclose(file_pointer);

    printf("%s 파일이 성공적으로 생성되었습니다.\n", filename);

    return 0;
}
