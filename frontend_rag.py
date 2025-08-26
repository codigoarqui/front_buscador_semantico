import requests
import streamlit as st

API_BASE_URL = "http://localhost:8000"
BUSQUEDA_URL = f"{API_BASE_URL}/rag/"

st.set_page_config(page_title="Buscador semántico", page_icon=":rocket:")
st.title('Motor de Búsqueda Semántica')
st.subheader('Consulta la API')

consulta = st.text_input("Escribe tu consulta aquí:")

if st.button("Buscar"):
    if consulta:
        payload = {
            "consulta": consulta,
            "top_k": 5
        }

        with st.spinner('Buscando...'):
            try:
                response = requests.post(BUSQUEDA_URL, json=payload)
                if response.status_code == 200:
                    resultados = response.json().get("respuesta", [])
                    st.subheader("Resultados encontrados:")
                    if resultados:
                        st.write(f"- **Texto:** {resultados}")
                    else:
                        st.info("No se encontraron documentos similares.")
                else:
                    st.error(f"Error en la API: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"No se pudo conectar a la API. Asegúrate de que está corriendo en {API_BASE_URL}. Error: {e}")
    else:
        st.warning("Por favor, ingresa una consulta para buscar.")