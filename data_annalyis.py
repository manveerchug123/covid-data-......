import pandas as pd
import plotly.express as px 
df = pd.read_csv("covid_data.csv")
fig = px.line(df, x="date", y= "cases",color ="country",title= "Covid Cases")
fig.show()