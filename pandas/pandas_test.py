#%%
import pandas as pd
import faker
import random

f = faker.Faker("ko-kr")
data = [ [f.name()] + [random.randint(1, 100) for i in range(5)] for j in range(100)]

df = pd.DataFrame(data, columns = ["이름", "국어", "영어", "수학", "사회", "정보"])

df.to_csv("score.csv")
df.to_excel("score.xlsx", index = False)

#%%
df = pd.read_csv("https://raw.githubusercontent.com/ovclid/leture/main/pandas/score.csv", index_col = 0)
