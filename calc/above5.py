import numpy as np
import pandas as pd
import isofy

df = pd.read_csv("out.csv")

df = df[df["MAGNITUDE"] > 5.0]
df.to_csv('out5.csv', index = False)

print(df)

print(isofy(df))