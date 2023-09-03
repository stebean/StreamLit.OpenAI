import streamlit as st
import googlemaps
import requests


def location():
    # Configurar la API de Google Maps
    google_maps_api_key = st.secrets["GOOGLEMAPS_API_KEY"]
    gmaps = googlemaps.Client(key=google_maps_api_key)
    places = googlemaps.Client(key=google_maps_api_key)

    # Obtener la ubicación del usuario utilizando la API de Google Maps
    location = gmaps.geolocate()

    # Obtener la ciudad y el estado en la que se encuentra el usuario utilizando la API de Google Maps
    reverse_geocode_result = gmaps.reverse_geocode((location["location"]["lat"], location["location"]["lng"]))[0]
    city = None
    state = None
    for component in reverse_geocode_result["address_components"]:
        if "locality" in component["types"]:
            city = component["long_name"]
        elif "administrative_area_level_1" in component["types"]:
            state = component["long_name"]

    # Mostrar la ciudad y el estado en la que se encuentra el usuario
    st.title(f"Estás en la ciudad de :blue[{city}], :green[{state}]")

    # Mostrar el subtítulo "Lugares turísticos"
    st.header("Lugares turísticos cercanos: ", divider='green')

    # Buscar lugares turísticos en la ciudad utilizando la API de Google Places
    places_result = places.places_nearby(
        location=(location["location"]["lat"], location["location"]["lng"]),
        radius=50000,
        keyword="atracciones",
    )

    # Mostrar todos los lugares turísticos en la ciudad con una imagen de cada lugar turístico
    for place in places_result["results"]:
        with st.container():
            st.subheader(f"{place['name']}: {place['vicinity']}")
            if "photos" in place:
                photo_reference = place["photos"][0]["photo_reference"]
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={google_maps_api_key}"
                response = requests.get(photo_url)
                st.image(response.content)
            st.header('' ,divider='rainbow')