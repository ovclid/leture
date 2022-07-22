
import pandas as pd
import datetime

df = pd.read_csv("http://bit.ly/uforeports")

week_day = {0 : "월요일", 1 : "화요일", 2 : "수요일", 3 : "목요일", 4 : "금요일", 5 : "토요일", 6 : "일요일"}

#%%
for i in range(len(df)):
	dt = datetime.datetime.strptime(df.loc[i, "Time"], '%m/%d/%Y %H:%M')
	#print(week_day[dt.weekday()])
	df.loc[i, "day"] = week_day[dt.weekday()]

print(df["day"].value_counts())

#%%
df['day2']  = df['Time'].map(lambda x : week_day[datetime.datetime.strptime(x, '%m/%d/%Y %H:%M').weekday()])
print(df["day2"].value_counts())
