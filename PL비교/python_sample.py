#####################################################################
# 무엇을 하는(어떤 작업을 수행하는) 프로그램 일까요?
# 어떤 프로그램 언어로 작성된 코드 일까요?
# 색깔은 총 몇 종류인가요? 왜 다를까요?
# 특수 기호들의 종류는 몇 개 되나요? 어떤 의미로 왜 사용되었을까요? 
# 사용된 변수의 갯수 총 몇 개일까요?
# 선언문, 조건문, 반복문은 코드의 어느 부분에서 사용되었을까요?
#####################################################################


under_age = 0
over_age = 0

for i in range(3):
    age = int(input("당신의 나이는 : "))

    if age >= 19:
        print("당신은 성년입니다. \n")
        over_age = over_age + 1
    else:
        print("당신은 미성년자입니다. \n")
        under_age = under_age + 1

print("성년 : ", over_age, '명')
print("미성년 : ", under_age, '명')
