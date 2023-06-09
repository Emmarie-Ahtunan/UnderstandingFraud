import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd

data = pd.read_csv('sample.csv')
st.title('CSV Sample Data Viewer')
# Display the DataFrame
st.dataframe(data)

data = pd.read_csv('test.csv')
st.title('CSV Test Data Viewer')

# Display the DataFrame
st.dataframe(data)
