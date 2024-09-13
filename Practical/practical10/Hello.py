# This is the code done by ronit and send by him for reference
import streamlit as st
R = st.slider('R',0, 255)
G = st.slider('G',0, 255)
B = st.slider('B',0, 255)
RGB="#{:02X}{:02X}{:02X}".format(R, G, B)



st.write(RGB)
st.markdown(f"<div style='width:1000px; height:1000px; background-color:{RGB};'></div>",unsafe_allow_html=True) 