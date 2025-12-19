import folium
from IPython.display import display
map_center = [52.5200, 13.4050]
mymap=folium.Map(location=map_center, zoom_start=15)
folium.Marker(
    [52.5200, 13.4050],
popup='Berlin',
icon=folium.Icon(color='green',icon='info-sign')
).add_to(mymap)

mymap.save("map.html")

display(mymap)