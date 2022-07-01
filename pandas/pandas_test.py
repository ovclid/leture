#%%
import pandas as pd
import faker
import random
#%%
f = faker.Faker("ko-kr")
data = [ [f.name()] + [random.randint(1, 100) for i in range(5)] for j in range(100)]

df = pd.DataFrame(data, columns = ["이름", "국어", "영어", "수학", "사회", "정보"])

df.to_csv("score.csv")
df.to_excel("score.xlsx", index = False)

#%%
df = pd.read_csv("https://raw.githubusercontent.com/ovclid/leture/main/pandas/score.csv", index_col = 0)

for i in df.columns[1:6]:
    print(i)
    for j in range(len(df)):
        grade = ""
        if df.loc[j, i] >= 90: grade = "수"
        elif df.loc[j, i] >= 80: grade = "우"
        elif df.loc[j, i] >= 70: grade = "미"
        elif df.loc[j, i] >= 60: grade = "양"
        else : grade = "가"

        df.loc[j, i+"_등급"] = grade

df["국어_등급"].value_counts().sort_index()


gi = ["수", "우", "미", "양", "가"]
df["국어_등급"].value_counts().reindex(gi)

#%%
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

plt.title("국어 등급별 막대그래프")
plt.xlabel("등급")
plt.ylabel("성적")


#df["국어_등급"].value_counts().reindex(gi).plot()
df["국어_등급"].value_counts().reindex(gi).plot(kind="bar")

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
