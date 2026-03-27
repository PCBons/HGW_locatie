import streamlit as st
import streamlit.components.v1 as components
import folium
import shapely
import time
import re
from datetime import datetime
import geopandas as gpd

st.set_page_config(layout="wide")

@st.cache_data
def import_data(filename):
    gdf = gpd.read_file(filename)
    polygon = gdf.iloc[0]['geometry']
    return polygon

st.title('Zoektocht naar de HGW-locatie')

@st.fragment(run_every=1)
def countdown():
    target = datetime(2026, 4, 3, 18, 0, 0)
    remaining = target - datetime.now()

    if remaining.total_seconds() <= 0:
        st.success("🎉 De hint moeten nu bekendgemaakt worden!!")
        return

    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    st.metric("Aftellen tot de volgende hints bekendgemaakt worden...",
              f"{days}d {hours:02}u {minutes:02}m {seconds:02}s")

countdown()

st.caption('Verken hieronder het gebied wat in 2u bereikbaar is vanaf Utrecht met de auto (uitgaande van een vertrektijd 16:00 op 25-09-2026).')

@st.cache_data
def make_map(_polygon):

    m = folium.Map(location=[_polygon.centroid.y, _polygon.centroid.x], zoom_start=8, width="100%", height="100%")
    folium.GeoJson(shapely.to_geojson(_polygon)).add_to(m)
    return m

polygon = import_data('polygon_HGW.geojson')
m = make_map(polygon)

html = m._repr_html_()

# Vervang vaste pixel breedtes/hoogtes en de padding-bottom truc die folium gebruikt
html = re.sub(r'width: \d+\.?\d*px', 'width: 100%', html)
html = re.sub(r'height: \d+\.?\d*px', 'height: 100vh', html)
html = re.sub(r'padding-bottom: \d+\.?\d*%', 'padding-bottom: 0; height: 100vh', html)

components.html(html, height=1000)

