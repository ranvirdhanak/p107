import pandas as pd
import csv
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('data107p.csv')
student_df = df.loc[df['student_id']=="TRL_xsl"]
print(student_df.groupby("level")['attempt'].mean())
fig = go.Figure(go.Bar(
    x = student_df.groupby("level")['attempt'].mean(),
    y = ['level 1','level 2','level 3','level 4'],
    orientation = 'h'
))

df = pd.read_csv("data107p.csv")
fig = px.scatter(df,x = "attempt",y = "level",color = "student_id")
fig.show()

fig.show()