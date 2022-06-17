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
for i in range(students_num):
    total = sum(students[i][1:])
    students[i].append(total)
    students[i].append(total/len(students[i][1:]))

print(students[:5])
# %%


col_dic = {0: '이름', 1: '국어', 2: '영어', 3: '수학', 4: '과학', 5: '정보', 6: '미술', 7:"체육"}
# %%
def show_info(num):
    for i in range(len(col_dic)):
        print(col_dic[i], students[num][i])
        
        
# %%
cols = ["이름", "국어", "영어", "수학", "과학", "정보", "체육", "미술"]
# cols = list(col_dic.values())
df = pd.DataFrame(students, columns = cols)

#df["총계"] = df[cols[1]] + df[cols[2]] + df[cols[3]] + df[cols[4]] + df[cols[5]] + df[cols[6]] + df[cols[7]] 

df["총계"] = 0
for sub_name in cols[1:]:
    df["총계"] = df["총계"] + df[sub_name]
# df["총계"] = df[df.columns[1:]].sum(axis=1)
# df.sum(axis=1, numeric_only=True)

df["평균"] = df["총계"] / (len(cols) - 1)
print(df[df["평균"] == df["평균"].max()])
print(df[df["평균"] == df["평균"].min()])
#%%
print(df[df["평균"] >= df["평균"].mean()])

df.to_excel("test.xlsx")
# %%
