// 어떤 언어로 작성된 프로그램 일까요?
// 무슨 작업을 하는 프로그램 일까요?

#include <stdio.h>

int main () 
{
    int age;
    int over_age = 0;
    int under_age = 0;

    for (int i = 0; i < 3; i++) {
        printf("당신의 나이는 : ");
        scanf("%d", &age);

        if (age > 19) {
            printf("당신은 성년입니다. \n\n");
            over_age = over_age + 1;
        }
        else {
            printf("당신은 미성년자입니다. \n\n");
            under_age = under_age + 1;
        }
    }

    printf("성년 : %d 명\n", over_age);
    printf("미성년 %d 명", under_age) ;

    return 0;
}