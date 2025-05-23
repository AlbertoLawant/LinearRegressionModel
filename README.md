# 🎢 Rollercoaster Popularity Prediction using Linear Regression

This project uses historical rollercoaster data to predict a synthetic "popularity score" based on physical and categorical ride attributes. It demonstrates a complete, production-style machine learning workflow using **Python**, **pandas**, **scikit-learn**, and **Jupyter Notebooks**.

---

## 📌 Highlights

✅ End-to-end data science pipeline  
✅ Clean modular structure (`src/` and `notebooks/`)  
✅ Data cleaning, feature engineering, modeling, and evaluation  
✅ Visual pipeline representation in Jupyter  
✅ Production-grade code that’s reusable and scalable

---

## 🧠 Project Motivation

Rollercoasters are exciting engineering feats, but which features make them more “popular”?  
While real popularity data isn't available, we simulate it using a weighted formula combining ride speed, height, number of inversions, and G-force. This lets us focus on building and evaluating a real regression pipeline.

---


## 🗂️ Project Structure

rollercoaster-regression/
├── data/
│ ├── coaster_db.csv # Raw dataset
│ ├── cleaned_coaster_data.csv # Cleaned dataset (optional)
│ └── featured_coaster_data.csv # Post-feature-engineering dataset (optional)
│
├── notebooks/
│ ├── cleaning.ipynb # Data cleaning notebook
│ ├── feature_engineering.ipynb # Imputation and type conversion
│ ├── modeling.ipynb # Regression modeling & evaluation
│ └── Modeling.png # Pipeline diagram screenshot
│
├── src/
│ ├── cleaning.py # Python version of cleaning.ipynb
│ ├── feature_engineering.py # Python version of feature_engineering.ipynb
│ └── modeling.py # Python version of modeling.ipynb
│
├── .gitignore
├── LICENSE
├── README.md


---

## 🔍 Features and Target

### 📥 Input Features
- Numerical: `Speed_mph`, `Height_ft`, `Inversions`, `Gforce`, `Year_Introduced`
- Categorical: `Location`, `Manufacturer`, `Type_Main`

### 🎯 Target Variable
A synthetic "popularity" score is calculated as:

```python
Popularity = (
    Speed_mph * 0.4 +
    Height_ft * 0.3 +
    Inversions * 0.2 +
    Gforce * 0.1
)

---

## 🧪 How to Run

Follow these steps to run the full machine learning pipeline or interact with the project through Jupyter Notebooks.

---

### 🔁 1. Clone the Repository

Start by cloning the repo to your local machine:

```bash
git clone https://github.com/yourusername/rollercoaster-regression.git
cd rollercoaster-regression


### 📂 2. Add the Dataset

This project uses the `coaster_db.csv` dataset, which is **not included** in the repository due to file size or licensing.

To proceed:

- Download or locate `coaster_db.csv`
- Move it into the `data/` folder

> 📌 Final path should be: `data/coaster_db.csv`

---

### 📦 3. Install Dependencies

Use `pip` to install the required Python packages:

```bash
pip install -r requirements.txt

### 🚀 4. Run the Full Pipeline (Optional)

To execute the entire workflow from data cleaning to model evaluation:

```bash
python main.py


---

Let me know if you want to follow that with a list of the notebooks to open next!
