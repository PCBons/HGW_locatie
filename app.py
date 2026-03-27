import streamlit as st
import streamlit.components.v1 as components
import folium
import shapely
import geopandas as gpd

st.set_page_config(layout="wide")

@st.cache_data
def import_data(filename):
    gdf = gpd.read_file(filename)
    polygon = gdf.iloc[0]['geometry']
    return polygon

st.title('Zoektocht naar de HGW-locatie')
st.caption('Verken hieronder het gebied wat in 2u bereikbaar is vanaf Utrecht met de auto (uitgaande van een vertrektijd 16:00 op 25-09-2026).')

@st.cache_data
def make_map(_polygon):

    m = folium.Map(location=[_polygon.centroid.y, _polygon.centroid.x], zoom_start=8)
    folium.GeoJson(shapely.to_geojson(_polygon)).add_to(m)
    return m

polygon = import_data('polygon_HGW.geojson')
m = make_map(polygon)
components.html(m._repr_html_(), height=800)

