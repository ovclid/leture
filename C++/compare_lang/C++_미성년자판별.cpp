// � ���� �ۼ��� ���α׷� �ϱ��?
// ���� �۾��� �ϴ� ���α׷� �ϱ��?

#include <iostream>

int main()
{
    int age;
    int over_age = 0;
    int under_age = 0;

    for (int i = 0; i < 3; i++) {
        std::cout << "����� ���̴� : ";
        std::cin >> age;

        if (age > 19) {
            std::cout << "����� �����Դϴ�. \n\n";
            over_age = over_age + 1;
        }
        else {
            std::cout << "����� �̼������Դϴ�. \n\n";
            under_age = under_age + 1;
        }
    }

    std::cout << "���� : " << over_age << " ��\n";
    std::cout << "�̼��� :" << under_age << " ��";

    return 0;
}