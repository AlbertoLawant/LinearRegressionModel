import pandas as pd

df = pd.read_csv('data/coaster_db.csv')

print(df.shape)

print(df.head())


df = df[['coaster_name', 'Length', 'Speed', 'Location', 'Status',
         'Manufacturer', 'year_introduced', 'latitude', 'longitude',
         'Type_Main', 'opening_date_clean', 'speed_mph', 'height_ft',
         'Inversions_clean', 'Gforce_clean']].copy()


df = df.rename(columns={
    'coaster_name': 'Coaster_Name',
    'year_introduced': 'Year_Introduced',
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'opening_date_clean': 'Opening_Date',
    'speed_mph': 'Speed_mph',
    'height_ft': 'Height_ft',
    'Inversions_clean': 'Inversions',
    'Gforce_clean': 'Gforce'
})


df = df.loc[~df.duplicated(subset='Coaster_Name')].reset_index(drop=True)


print("Cleaned shape:", df.shape)


