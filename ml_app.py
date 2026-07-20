import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="California House Price Prediction",
    page_icon="🏡",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# -----------------------------
# Title
# -----------------------------
st.title("🏡 California House Price Prediction")
st.markdown(
    "Predict the median house value using a trained Machine Learning model."
)

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Enter House Information")

housing_median_age = st.sidebar.slider(
    "Housing Median Age",
    min_value=1,
    max_value=60,
    value=25
)

total_rooms = st.sidebar.number_input(
    "Total Rooms",
    min_value=1,
    value=2000
)

total_bedrooms = st.sidebar.number_input(
    "Total Bedrooms",
    min_value=1,
    value=400
)

population = st.sidebar.number_input(
    "Population",
    min_value=1,
    value=1500
)

households = st.sidebar.number_input(
    "Households",
    min_value=1,
    value=350
)

median_income = st.sidebar.slider(
    "Median Income",
    min_value=0.5,
    max_value=15.0,
    value=4.0,
    step=0.1
)

ocean_proximity = st.sidebar.selectbox(
    "Ocean Proximity",
    [
        "<1H OCEAN",
        "INLAND",
        "ISLAND",
        "NEAR BAY",
        "NEAR OCEAN"
    ]
)

# -----------------------------
# Create DataFrame
# -----------------------------
input_df = pd.DataFrame({
    "housing_median_age": [housing_median_age],
    "total_rooms": [total_rooms],
    "total_bedrooms": [total_bedrooms],
    "population": [population],
    "households": [households],
    "median_income": [median_income],
    "ocean_proximity": [ocean_proximity]
})

# -----------------------------
# Show Inputs
# -----------------------------
st.subheader("Input Features")

st.dataframe(input_df, use_container_width=True)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict House Price"):

    prediction = model.predict(input_df)[0]

    st.success(
        f"🏠 Predicted House Value: **${prediction:,.0f}**"
    )

# -----------------------------
# Feature Description
# -----------------------------
with st.expander("Feature Descriptions"):

    st.markdown("""
| Feature | Description |
|---------|-------------|
| housing_median_age | Median age of houses in the block |
| total_rooms | Total number of rooms |
| total_bedrooms | Total number of bedrooms |
| population | Population living in the block |
| households | Number of households |
| median_income | Median income (tens of thousands of dollars) |
| ocean_proximity | Location relative to the ocean |
""")