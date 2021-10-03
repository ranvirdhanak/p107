import pandas as pd
import csv
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('data107p.csv')
mean = df.groupby(["student_id","level"],as_index = False)['attempt'].mean()
fig = px.scatter(mean,x = "student_id",y = "level",color = "attempt",size = "attempt")
fig.show()
