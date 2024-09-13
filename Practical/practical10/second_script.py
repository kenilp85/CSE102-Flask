# This is similar to first script just uses the write fucntion
import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table: ")
st.write(pd.DataFrame({
    'first columm':[1,2,3,4],
    'second column':[10,20,30,40]
}))