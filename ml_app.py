import streamlit as st
import pandas as pd

st.title("Test")

df = pd.DataFrame({"A": [1, 2, 3]})

st.dataframe(df)
