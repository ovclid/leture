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


df["영어"] = score_list


import random
score_list = [random.randint(1, 100) for i in range(10)]
df["국어"] = score_list
