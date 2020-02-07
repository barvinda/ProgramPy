import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def colour_(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 < elevation < 3000:
        return "orange"
    elif elevation > 3000:
            return "red"

map = folium.Map(location=[38.58, -99.09],zoom_start=10, tiles="Stamen Watercolor")

fgv=folium.FeatureGroup(name="Volcanoes")

for lt, lo, el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt, lo], radius=6, popup=str(el)+ "m", tooltip = str(el)+ "m",
    fill_color = colour_(el), color = "grey", fill_opacity = 1))

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
    style_function = lambda x: {'fillColor': "green" if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 < x['properties']['POP2005'] < 50000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
