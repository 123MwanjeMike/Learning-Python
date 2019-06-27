Mike=['sex','drink','sleep']
for i in Mike:
  print(i)

a=[1,2,3,[4,9,[8]]]

for i in a:
  print(i)

print(a[3][2][0])


import pandas as pd
import csv

url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

data=pd.read_csv(url)
print (data)
c = data[data.Region == 'AFRICA']
print (c)
c.to_csv("africa.csv")
