// 어떤 언어로 작성된 프로그램 일까요?
// 무슨 작업을 하는 프로그램 일까요?

#include <iostream>

int main()
{
    int age;
    int over_age = 0;
    int under_age = 0;

    for (int i = 0; i < 3; i++) {
        std::cout << "당신의 나이는 : ";
        std::cin >> age;

        if (age > 19) {
            std::cout << "당신은 성년입니다. \n\n";
            over_age = over_age + 1;
        }
        else {
            std::cout << "당신은 미성년자입니다. \n\n";
            under_age = under_age + 1;
        }
    }

    std::cout << "성년 : " << over_age << " 명\n";
    std::cout << "미성년 :" << under_age << " 명";

    return 0;
}