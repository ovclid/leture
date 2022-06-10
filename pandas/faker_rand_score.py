#%%
import pandas as pd
import faker
f = faker.Faker('ko-kr')

# %%
def rand_next_num(rand_num):
    rand_min = rand_num - 10
    rand_max = rand_num + 10

    if rand_min < 0:
        rand_min = 0

    if rand_max > 100:
        rand_max = 100

    next_rand_num = f.random_int(rand_min, rand_max)
    
    return next_rand_num
#%%
students = []

for i in range(1000):
    student = []
    student.append(f.name())

    subject_score = f.random_int(1, 100)
    #print("init random num : ", subject_score)

    student.append(subject_score)

    for j in range(6): 
        subject_score = rand_next_num(subject_score)
        #print("next random num : ", subject_score)
        student.append(subject_score)

    students.append(student)

print(students[:5])
# %%
cols = ["이름", "국어", "영어", "수학", "과학", "정보", "체육", "미술"]
df = pd.DataFrame(students, columns = cols)

df["총계"] = df[cols[1]] + df[cols[2]] + df[cols[3]] + df[cols[4]] + df[cols[5]] + df[cols[6]] + df[cols[7]] 
df["평균"] = df["총계"] / (len(cols) - 1)
print(df[df["평균"] == df["평균"].max()])
print(df[df["평균"] == df["평균"].min()])
#%%
print(df[df["평균"] >= df["평균"].mean()])

df.to_excel("test.xlsx")
# %%
