import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd

data = pd.read_csv('test.csv')
st.title('CSV Test Data Viewer')

# Display the DataFrame
st.dataframe(data)
