import plotly.express as px
import pandas as pd

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

fig.show()
