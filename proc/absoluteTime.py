import calendar
import datetime
import numpy as np
import pandas as pd

df2019 = pd.read_csv("cat2019.csv")
print(df2019)

df2019 = df2019.assign(DATE = df2019.YEAR.astype(str)) 
print(df2019) 

# df2019['DATE'] = df2019[df2019.columns[0:3]].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
# print(df2019)

# df2019['TIME'] = df2019[df2019.columns[3:6]].apply(lambda x: ':'.join(x.dropna().astype(str)), axis=1)
# print(df2019)


