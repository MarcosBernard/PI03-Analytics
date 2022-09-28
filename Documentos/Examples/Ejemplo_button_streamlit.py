import streamlit as st

st.title("Making a Button")

result = st.button("Click Here")

st.write(result)

if result:
    st.write(":smile:")

# To run this go to this path:
# /OneDrive/Documentos/2. DataScience/HENRY/5. Proyectos Individuales/3. PI03_DATA03/2. PI03-Analytics/Documentos/Examples
#
# And execute:
# py -m streamlit run Ejemplo_button_streamlit.py