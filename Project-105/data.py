import csv
import pandas as pd
import plotly.express as px
import math

with open("data.csv",newline="")as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
print(file_data)
total_marks = 0
total_entries = len(file_data)

for marks in file_data:
    total_marks+= float(marks[1])

mean = total_marks/total_entries
print("Mean is      " +str(mean))


df = pd.read_csv("data.csv")

fig = px.scatter(df,x="Student Number",y="Marks")

fig.update_layout(shapes=[dict(type='line',y0=mean,y1=mean,x0=0,x1=total_entries)])
fig.update_yaxes(rangemode='tozero')
fig.show()
squared_list = []
for number in file_data:
    a = int(number[0])-mean
    a = a**2
    squared_list.append(a)
    
sum = 0
for i in squared_list:
    sum = sum+i

result = sum/(total_entries)
standardDeviation = math.sqrt(result)
print(standardDeviation)