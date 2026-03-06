import folium
import streamlit as st

from streamlit_folium import st_folium

st.title("Python maps using Folium")
st.subheader("click on an icon to see it's location")

style = 'NatGeo_World_Map'
m = folium. Map(
  location=[20,78], zoom_start=5,
  tiles =f"https://server.arcgisonline.com/ArcGIS/rest/services/{style}/MapServer/tile/{{z}}/{{y}}/{{x}}",
  attr = "Esri"
)

coordinates = [
    [40.7128, -74.0060],
    [51.5074, -0.1278],
    [35.6895, 139.6917],
    [19.0760, 72.8777],
    [28.6100, 77.2300],
    [12.9789, 77.5917],
    [13.0827, 80.2707],
    [-26.2041, 28.0473],
    [45.4215, -75.6972],
    [-33.8688, 151.2093]
]
names = ["New York", "London", "Tokyo", "Mumbai", "Delhi", "Bangalore", "Chennai", "Johannesburg", "Ottawa", "Sydney"]

for i in range(10):
  folium. Marker (
    location = coordinates[i],
    popup = names[i],
    icon = folium. Icon(color = 'red')
    ).add_to(m)

st_folium(m)