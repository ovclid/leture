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
# %%
import requests
import pandas as pd
url = 'https://github.com/ovclid/leture/blob/main/pandas/score.xlsx?raw=true'
r = requests.get(url)


with open('temp.xlsx', 'wb') as f:
    f.write(r.content)

    
"""
f = open('temp.xlsx', 'wb')
f.write(r.content)
f.close()
"""

df = pd.read_excel('temp.xlsx')

# %%
