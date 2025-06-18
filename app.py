import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit Sample App')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.subheader('Line chart')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

if st.checkbox('Show dataframe'):
    st.write(chart_data)

st.subheader('Slider')
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
