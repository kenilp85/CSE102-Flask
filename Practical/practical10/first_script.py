"""
This is first example to create a table using streamlit
"""
import streamlit as st
import pandas as pd
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

df