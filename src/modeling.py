import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('data/featured_coaster_data.csv')

df['Popularity'] = (df['Speed_mph'] * 0.4 + df['Height_ft'] * 0.3 + df['Inversions'] * 0.2 + df['Gforce'] * 0.1)

num_features = ['Speed_mph', 'Height_ft', 'Inversions', 'Gforce', 'Year_Introduced']
cat_features = ['Location', 'Manufacturer', 'Type_Main']
target = 'Popularity'

X = df[num_features + cat_features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_features),
    ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), cat_features)
])

model_pipeline = Pipeline([
    ('preprocessing', preprocessor),
    ('model', LinearRegression())
])

model_pipeline.fit(X_train, y_train)

y_pred = model_pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")
