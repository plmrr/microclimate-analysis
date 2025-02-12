import requests
import pandas as pd
from pyproj import Transformer

stations_df = pd.read_csv('data/imgw/stacje_synop_converted.csv')

def calculate_bounds(lat, lon, distance_km=5):
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:2180")
    x_center, y_center = transformer.transform(lat, lon)
    
    buffer_m = distance_km * 1000 / 2
    x_min, x_max = x_center - buffer_m, x_center + buffer_m
    y_min, y_max = y_center - buffer_m, y_center + buffer_m
    
    print(x_min, x_max, y_min, y_max)

    return x_min, x_max, y_min, y_max

for index, row in stations_df.iterrows():
    station_name = row['nazwa_stacji']
    lat, lon = row['szerokosc_geo'], row['dlugosc_geo']

    x_min, x_max, y_min, y_max = calculate_bounds(lat, lon)

    wcs_url = "https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/GRID1/WCS/DigitalTerrainModelFormatTIFF?"

    params = {
        "SERVICE": "WCS",
        "VERSION": "2.0.1",
        "REQUEST": "GetCoverage",
        "COVERAGEID": "DTM_PL-KRON86-NH_TIFF",
        "FORMAT": "image/tiff",
        "SUBSET": [
            f"x({y_min},{y_max})", #TODO
            f"y({x_min},{x_max})"
        ],
        "scalefactor": "0.5"
    }

    response = requests.get(wcs_url, params=params)

    if response.status_code == 200:
        with open(f'data/geoportal/NMT_{station_name}.tiff', 'wb') as file:
            file.write(response.content)
        print(f"Dane dla stacji {station_name} zostały pobrane.")
    else:
        print(f"Błąd przy pobieraniu danych dla stacji {station_name}. Kod błędu: {response.status_code}")
        print("Treść odpowiedzi:", response.text)






