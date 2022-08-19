# 어떤 언어로 작성된 프로그램 일까요?
# 무슨 작업을 하는 프로그램 일까요?

under_age = 0
over_age = 0

for i in range(3):
    age = int(input("당신의 나이는 : "))

    if age < 19:
        print("당신은 미성년자입니다. \n")
        under_age = under_age + 1
    else:
        print("당신은 성년입니다. \n")
        over_age = over_age + 1

print("성년 : ", over_age, '명')
print("미성년 : ", under_age, '명')