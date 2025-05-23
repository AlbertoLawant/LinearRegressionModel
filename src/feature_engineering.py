import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer  
from sklearn.impute import IterativeImputer, SimpleImputer
from sklearn.compose import ColumnTransformer

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('data/cleaned_coaster_data.csv')

df = df.drop('Status', axis=1)

num_cols = df.select_dtypes(include=['number']).columns
cat_cols = df.select_dtypes(include=['object', 'category']).columns

num_imp = IterativeImputer(random_state=42)
cat_imp = SimpleImputer(strategy='most_frequent')

preprocessor = ColumnTransformer([
    ('num', num_imp, num_cols),
    ('cat', cat_imp, cat_cols)
])

df_imputed = preprocessor.fit_transform(df)

df_imputed = pd.DataFrame(df_imputed, columns=num_cols.tolist() + cat_cols.tolist())

df['Year_Introduced'] = pd.to_numeric(df['Year_Introduced']).fillna(df['Year_Introduced'].median()).astype(int)
df['Latitude'] = pd.to_numeric(df['Latitude'])
df['Longitude'] = pd.to_numeric(df['Longitude'])
df['Speed_mph'] = pd.to_numeric(df['Speed_mph']).fillna(df['Speed_mph'].median()).astype(int)
df['Height_ft'] = pd.to_numeric(df['Height_ft']).fillna(df['Height_ft'].median()).astype(int)
df['Inversions'] = pd.to_numeric(df['Inversions']).fillna(df['Inversions'].median()).astype(int)
df['Gforce'] = pd.to_numeric(df['Gforce'])
df['Opening_Date'] = pd.to_datetime(df['Opening_Date'])