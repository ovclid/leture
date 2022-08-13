# %%
import pandas as pd

df = pd.read_csv("http://bit.ly/uforeports")

df.Time = pd.to_datetime(df.Time)
df["Time2"] = df.Time.dt.day_name()

df.Time2.value_counts().plot(kind="bar")
# %%
df.Time.dt.hour.value_counts().plot(kind = 'bar')

# %%
df.Time.dt.hour.value_counts().sort_index().plot(kind='bar')
