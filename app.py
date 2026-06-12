import streamlit as st

st.title("Mi primera aplicación en python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Alia Ortega")

sesion = st.sidebar.selectbox("Selecione una sesión", ["Sesión 1", "Sesión 2", "Sesión 3", "Sesión 4"])

if sesion == "Sesión 1":
  st.write("Bienvenido la sesión 1")

elif sesion == "Sesión 2":
  st.write("Bienvenido la sesión 2")

elif sesion == "Sesión 3":
  st.write("Bienvenido la sesión 3")

else:
  st.write("Bienvenido la sesión 4")
