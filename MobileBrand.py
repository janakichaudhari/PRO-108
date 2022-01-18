import pandas as p
import plotly.figure_factory as f

df=p.read_csv("brand.csv")
h=df["Avg Rating"].tolist()

fig=f.create_distplot([h],["Avg Rating"])
fig.show()