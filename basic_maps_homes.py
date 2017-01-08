

"""
### @Author - Aashish
### Testing basic Map with folium
### locating my home, paternal home, maternal home
### Kathmandu lat-long [27.7162385, 85.4277276]
"""

import folium
import os


working_directory = os.getcwd()
webpages_directory = working_directory + '/webpages'

if not os.path.exists(webpages_directory):
    os.makedirs(webpages_directory)

map_osm = folium.Map(location=[27.7162385, 85.4277276])
map_osm.save(webpages_directory + '/map_kathmandu.html')

#map_osm = folium.Map(location=[27.7162385, 85.4277276], tiles='OpenStreetMap', zoom_start=13)
map_osm = folium.Map(location=[27.7162385, 85.4277276], tiles='Stamen Terrain', zoom_start=13)
#map_osm = folium.Map(location=[45.5236, -122.6750], tiles='Mapbox',API_key='your.API.key')
#map_osm = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles='http://{s}.tiles.yourtiles.com/{z}/{x}/{y}.png', attr='My Data Attribution')

map_1 = folium.Map(location=[27.7162385, 85.4277276], zoom_start=12, tiles='OpenStreetMap')
folium.Marker(location=[27.705584, 85.418216], popup='Mamaghar', icon=folium.Icon(color='blue')).add_to(map_1)
#folium.Marker(location=[27.692936, 85.327303], popup='BabarMahal_home', icon=folium.Icon(color='green', icon='cloud')).add_to(map_1)
folium.Marker(location=[27.645642, 85.384611], popup='Lubhu_home', icon=folium.Icon(color='pink',icon='info-sign')).add_to(map_1)
folium.CircleMarker(location=[27.692936, 85.327303], radius=500, popup='BabarMahal_home', color='#3186cc', fill_color='#3186cc').add_to(map_1)

map_1.save(webpages_directory + '/map_homes.html')

# LatLong function - wherever u click on map, you ll have LAT LONG displayed
map_2 = map_1.add_child(folium.LatLngPopup())
map_2.save(webpages_directory + '/map_latlong_homes.html')


map_polygon = folium.Map(location=[27.705, 85.48], zoom_start=13)
folium.RegularPolygonMarker([27.705, 85.48], popup='Kathmandu', fill_color='#132b5e', number_of_sides=3, radius=10).add_to(map_polygon)
map_polygon.save('c:/temp/homes_polygon.html')

