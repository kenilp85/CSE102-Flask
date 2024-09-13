import streamlit as st

col1, col2, col3 = st.columns(3)
with col1:
    st.button("Red")
    colorSelect = "Red"
with col2:    
    st.button("Green")
    colorSelect = "Green"
with col3:    
    st.button("Blue")
    colorSelect = "Blue"

value = st.slider("select Color value",0,255)

# hex(value);

if (colorSelect == 'Red'):
    value1 = hex([hex(value),0,0]);
elif (colorSelect == 'Green'):
    pass
elif (colorSelect == 'Blue'):
    pass
st.color_picker("Pick A Color", "#00f00")