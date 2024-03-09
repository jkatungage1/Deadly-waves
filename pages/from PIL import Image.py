from PIL import Image
import plotly.express as px

df = px.data.gapminder().query("year==2007")

fig = px.scatter(
    df,
    x="lifeExp",
    y="gdpPercap",
    hover_name="country",
    hover_data=["lifeExp", "gdpPercap", "pop"]
)
fig.update_traces(marker_color="rgba(0,0,0,0)")

maxDim = df[["lifeExp", "gdpPercap"]].max().idxmax()
maxi = df[maxDim].max()
for i, row in df.iterrows():
    country = row['country'].replace(" ", "-")
    fig.add_layout_image(
        dict(
            source=Image.open(f"flags/png/512/{country}.png"),
            xref="x",
            yref="y",
            xanchor="center",
            yanchor="middle",
            x=row["lifeExp"],
            y=row["gdpPercap"],
            sizex=np.sqrt(row["pop"] / df["pop"].max()) * maxi * 0.2 + maxi * 0.05,
            sizey=np.sqrt(row["pop"] / df["pop"].max()) * maxi * 0.2 + maxi * 0.05,
            sizing="contain",
            opacity=0.8,
            layer="above"
        )
    )

fig.update_layout(height=600, width=1000, yaxis_range=[-5e3, 55e3], plot_bgcolor="#dfdfdf")

fig.show()