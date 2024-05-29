#include <stdio.h>
#include <string.h>

int MAX_USERS = 100;

struct User {
    char name[50];
    int age;
    char email[50];
};

int main() {
    struct User users[MAX_USERS];
    int numUsers = 0;

    int choice = 0;
    while (choice != 3) {
        printf("---------------------------\n");
        printf("1. 사용자 정보 입력\n");
        printf("2. 저장된 사용자 데이터를 출력\n");
        printf("3. 종료\n");
        printf("---------------------------\n");
        printf("선택하세요: ");
        scanf("%d", &choice); 
        printf("---------------------------\n");

        if (choice == 1) {
            if (numUsers < MAX_USERS) {
                printf("이름을 입력하세요: ");
                scanf("%s", users[numUsers].name);
                printf("나이를 입력하세요: ");
                scanf("%d", &users[numUsers].age);
                printf("이메일을 입력하세요: ");
                scanf("%s", users[numUsers].email);
                numUsers++;
            } else {
                printf("더 이상 사용자를 추가할 수 없습니다.\n");
            }
        } else if (choice == 2) {
            if (numUsers > 0) {
                printf("저장된 사용자 데이터:\n");
                for (int i = 0; i < numUsers; i++) {
                    printf("이름: %s, 나이: %d, 이메일: %s\n", users[i].name, users[i].age, users[i].email);
                }
            } else {
                printf("저장된 사용자 데이터가 없습니다.\n");
            }
        } else if (choice == 3) {
            printf("프로그램을 종료합니다.\n");
        } else {
            printf("범위 밖 숫자를 선택했습니다.\n");
        }
    }
}
