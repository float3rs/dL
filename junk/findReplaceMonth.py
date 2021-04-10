import os

directory = "./"

for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
        print(filename)
        print(os.path.join(directory, filename))