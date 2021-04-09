import numpy as np
import pandas as pd

df = pd.read_csv("full.csv")

int_month_map = dict(JAN=1, FEB=2, MAR=3, APR=4, MAY=5, JUN=6, JUL=7, AUG=8, SEP=9, OCT=10, NOV=11, DEC=12)
df['MONTH'] = df['MONTH'].replace(int_month_map)
df["MONTH"] = df.MONTH.map("{:02}".format)

df["DAY"] = df.DAY.map("{:02}".format)
df["HOUR"] = df.HOUR.map("{:02}".format)
df["MINUTE"] = df.MINUTE.map("{:02}".format)
df["SECOND"] = df.SECOND.map("{:04.1F}".format)
df["LATITUDE"] = df.LATITUDE.map("{:+09.4F}".format)
df["LONGITUDE"] = df.LONGITUDE.map("{:+09.4F}".format)

df["DEPTH"] = df.DEPTH.map("{:03}".format)
# df["DEPTH"] = - df["DEPTH"] * 1000
# df["DEPTH"] = df.DEPTH.map("{:+07}".format)


df = df.assign(DATETIME = df.YEAR.astype(str) + '-' + df.MONTH.astype(str) + '-' + df.DAY.astype(str) + 'T' + df.HOUR.astype(str) + ':' + df.MINUTE.astype(str) + ':' + df.SECOND.astype(str) + 'Z') 
df = df.assign(LOCATION = df.LATITUDE.astype(str) + df.LONGITUDE.astype(str)+ "/")
# df = df.assign(LOCATION = df.LATITUDE.astype(str) + df.LONGITUDE.astype(str) + df.DEPTH.astype(str) + "CRSWGS_84" + "/")
# df = df.assign(_DATETIME = pd.to_datetime(df["DATETIME"]))


df.to_csv('out.csv', index = False)

print(df)

