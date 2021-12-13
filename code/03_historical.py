import folium
import pandas as pd

df = pd.read_csv("data/deaths.csv")

locations = df[['X coordinate', 'Y coordinate']].values.tolist()

m = folium.Map(location=[51.5132119,-0.13666], zoom_start=20, tiles="Stamen Toner")
for location in locations:
    folium.CircleMarker(location, radius=4, color='red', fill=True, fill_color='red', opacity = 0.4).add_to(m)
m.save('03_historical.html')