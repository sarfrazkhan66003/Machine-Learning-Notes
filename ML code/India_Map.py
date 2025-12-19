import folium
from IPython.display import display

map_center = [20.5937, 78.9629]
mymap = folium.Map(location=map_center, zoom_start=5)
folium.Marker(
    [20.5937, 78.9629],
    popup='India',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(mymap)

mymap.save("map.html")

display(mymap)