import calendar
import datetime
import numpy as np
import pandas as pd

#monthnums = dict(JAN='01', FEB='02', MAR='03', APR='04', MAY='05', JUN='06', JUL='07', AUG='08', SEP='09', OCT='10', NOV='11', DEC='12')
#daynums = {1:"01",2:"02",3:"03",4:"04",5:"05",6:"06",7:"07",8:"08",9:"09"}

monthnums = dict(JAN=1, FEB=2, MAR=3, APR=4, MAY=5, JUN=6, JUL=7, AUG=8, SEP=9, OCT=10, NOV=11, DEC=12)


df = pd.read_csv("full.csv")

df['MONTH'] = df['MONTH'].replace(monthnums)

df["MONTH"] = df.MONTH.map("{:02}".format)
df["DAY"] = df.DAY.map("{:02}".format)
df["HOUR"] = df.HOUR.map("{:02}".format)
df["MINUTE"] = df.MINUTE.map("{:02}".format)
df["SECOND"] = df.SECOND.map("{:03.1f}".format)
# df['DAY'] = df['DAY'].replace(daynums)
#print(df)

df = df.assign(DATETIME = df.YEAR.astype(str) + '-' + df.MONTH.astype(str) + '-' + df.DAY.astype(str) + 'T' + df.HOUR.astype(str) + ':' + df.MINUTE.astype(str) + ':' + df.SECOND.astype(str) + '+00:00') 


# df2019['DATE'] = df2019[df2019.columns[0:3]].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
# print(df2019)

# df2019['TIME'] = df2019[df2019.columns[3:6]].apply(lambda x: ':'.join(x.dropna().astype(str)), axis=1)
# print(df2019)

df["DATETIME"] = pd.to_datetime(df["DATETIME"])
print(df) 
