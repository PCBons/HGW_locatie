import streamlit as st
import streamlit.components.v1 as components
import folium
import shapely
import time
from datetime import datetime
import geopandas as gpd

st.set_page_config(layout="wide")

@st.cache_data
def import_data(filename):
    gdf = gpd.read_file(filename)
    polygon = gdf.iloc[0]['geometry']
    return polygon

@st.cache_data
def import_route(filename):
    gdf = gpd.read_file(filename)
    line = gdf.iloc[0]['geometry']
    return line

st.title('Zoektocht naar de HGW-locatie')

@st.fragment(run_every=1)
def countdown():
    target = datetime(2026, 4, 25, 18, 0, 0)
    remaining = target - datetime.now()

    if remaining.total_seconds() <= 0:
        st.success("🎉 De nieuwe hints moeten nu bekendgemaakt worden!!")
        return

    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    st.metric("Aftellen tot de volgende hints bekendgemaakt worden...",
              f"{days}d {hours:02}u {minutes:02}m {seconds:02}s")

countdown()

st.caption('Verken hieronder het gebied wat in 2u bereikbaar is vanaf Utrecht met de auto (uitgaande van een vertrektijd 16:00 op 25-09-2026).')
st.caption('In het rood een benadering van de beroemde voettocht van Jacob van Lennep. De verbindt plaatsnamen geëxtraheerd uit zijn dagboek in chronologische volgorde.')
with st.popover("Van Lennep over Drente"):
    st.markdown("""
<i>“De Drenthenaar bezit alle deugden en gebreken welke onafscheidelijk zijn van zijn 
eenzaam landlijk leven. - Wanneer men in een gering gehucht eene kleine stulp bewoont, 
zelve onbemiddeld en onkundig is en tot naburen en medeburgers alleen dezulken heeft, 
wanneer men niet in de gelegenheid is meer grond te bebouwen dan men voor zijn eigen 
huisgezin van nooden heeft en er dus weinig of niets overschiet om in grootere plaatsen ter 
markt te brengen, dan kunnen er tusschen zoodanigen en de inwooners van grootere plaatsen 
weinige of geene naauwe betrekkingen stand grijpen: dan leeren zij de overtollige dingen niet 
kennen, welke de stedeling als noodzakelijke beschouwt; dan geven zij zich aan de weelde 
niet over welke deze najaagt; maar leven stil, eenvoudig, onnoozel voort als hunne ouders en 
voorouders deden; verlangen niet wat zij niet kennen, zijn onbezorgd voor het vervolg, en 
geven weer aan hun nakroost hetzelfde voorbeeld dat zij van hun voorgeslacht ontfangen 
hebben.”</i>
""",  unsafe_allow_html=True)

#@st.cache_data
def make_map(_polygon, _line):

    m = folium.Map(location=[_polygon.centroid.y, _polygon.centroid.x], zoom_start=7, width="100%", height="100%")
    folium.GeoJson(shapely.to_geojson(_polygon)).add_to(m)
    folium.GeoJson(
        shapely.to_geojson(_line),
        style_function=lambda feature: {
            'color': 'red',     # lijnkleur
            'weight': 5,        # dikte
            'opacity': 0.8      # transparantie
        }
).add_to(m)

    return m

polygon = import_data('data/polygon_HGW.geojson')
line = import_route('data/van_lennep_1823_route_only.geojson')
m = make_map(polygon, line)

components.html(m._repr_html_(), height=1500)

