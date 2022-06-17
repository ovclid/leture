import pandas as pd

df = pd.DataFrame()
print(df)

df["이름"] = ''
print(df)

df["영어"] = 0
print(df)

df["국어"] = 0
print(df)

df["수학"]
print(df)


score_list = [90, 40, 30]
df["영어"] = score_list


import random
score_list = [random.randint(1, 100) for i in range(10)]
df["국어"] = score_list

df.fillna(0)

df = df.fillna(0)

import faker
f = faker.Faker('ko-kr')

df['이름']= [f.name() for i in range(3)]

df['과학'] = [random.randint(1, 100) for i in range(3)]

df.append([i for i in range(100)]
df= df.append([i for i in range(100)])
          
df = df.DataFrame()
df = df.append([f.name() for i in range(100)]
df.rename(columns={0 : "이름"})

df = df.rename(columns={0 : "이름"})
df.rename(columns={0 : "이름"}, inplace=True)
df.index = range(1, 201)
pd.set_option('display.max_rows', 500)
               
               
df.drop(["영어"], axis = 1, inplace = True)
             
df = pd.DataFrame()
df = df.append([f.name() for i in range(100)])
df = df.rename(columns={0 : "이름"})
               
df["국어"] = [random.randint(1, 100)]
