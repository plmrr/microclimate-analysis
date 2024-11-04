import pandas as pd

file_path_synop = 'data/stacje_synop.csv'
file_path_klimat = 'data/stacje_klimat.csv'

stacje_synop = pd.read_csv(file_path_synop, delimiter=";", encoding='ISO-8859-2', engine='python')
stacje_klimat = pd.read_csv(file_path_klimat, delimiter=";", encoding='ISO-8859-2', engine='python')

stacje_synop['szerokosc_geo'] = stacje_synop['dlugosc_stopnie'] + (stacje_synop['dlugosc_minuty'] / 60) + (stacje_synop['dlugosc_sekundy'] / 3600)
stacje_synop['dlugosc_geo'] = stacje_synop['szerokosc_stopnie'] + (stacje_synop['szerokosc_minuty'] / 60) + (stacje_synop['szerokosc_sekundy'] / 3600)

stacje_klimat['szerokosc_geo'] = stacje_klimat['dlugosc_stopnie'] + (stacje_klimat['dlugosc_minuty'] / 60) + (stacje_klimat['dlugosc_sekundy'] / 3600)
stacje_klimat['dlugosc_geo'] = stacje_klimat['szerokosc_stopnie'] + (stacje_klimat['szerokosc_minuty'] / 60) + (stacje_klimat['szerokosc_sekundy'] / 3600)

stacje_synop_cleaned = stacje_synop.drop(columns=['szerokosc_stopnie', 'szerokosc_minuty', 'szerokosc_sekundy', 'dlugosc_stopnie', 'dlugosc_minuty', 'dlugosc_sekundy'])
stacje_klimat_cleaned = stacje_klimat.drop(columns=['szerokosc_stopnie', 'szerokosc_minuty', 'szerokosc_sekundy', 'dlugosc_stopnie', 'dlugosc_minuty', 'dlugosc_sekundy', 'Unnamed: 8'])

output_path_synop = 'data/stacje_synop_converted.csv'
output_path_klimat = 'data/stacje_klimat_converted.csv'
stacje_synop_cleaned.to_csv(output_path_synop, sep=',', index=False)
stacje_klimat_cleaned.to_csv(output_path_klimat, sep=',', index=False)
