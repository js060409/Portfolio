#include <stdio.h>
int main(void)
{
    int hour, min;
    printf("시간 분: ");
    scanf("%d %d", &hour, &min);
    printf("입력한 시간의 30 분 전 시간은");
    if (min >= 30)
        printf("%d시 %d분", hour, min-30);
    else
    {
        if (hour == 0)
            printf("%d시 %d분", 23 ,min + 30);
        else
            printf("%d시 %d분", hour-1 ,min + 30);
    }
}
