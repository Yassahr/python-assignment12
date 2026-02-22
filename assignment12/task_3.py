import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

df['strength']=df['strength'].str.replace(r'[^0-9.]', '', regex=True).astype(float)
print(df.tail(10), df.head(10))
fig = px.scatter(df, x="strength", y="frequency", color="frequency", color_continuous_scale="Viridis")
fig.show()

fig.write_html("wind.html",  auto_open=True)

