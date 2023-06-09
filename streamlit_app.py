import streamlit as st
import pandas as pd
data = pd.read_csv('test.csv')
st.title('CSV Data Viewer')

# Display the DataFrame
st.dataframe(data)
