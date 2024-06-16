#include <stdio.h>
int main(void)
{
    double a , b , c , score ;
    int d , e , f;
    printf("점수계산\n");
    printf("중간 비율/점수 \n");
    scanf("%lf %d",&a, &d);
    printf("기말 비율/점수 \n");
    scanf("%lf %d",&b, &e);
    printf("수행 비율/점수 \n");
    scanf("%lf %d",&c, &f);
    score = a*d + b*e + c*f ;
    printf("점수는 %.1lf 입니다 ", score);

}
