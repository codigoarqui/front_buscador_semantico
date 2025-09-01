import requests
import streamlit as st
import uuid

API_BASE_URL = "http://localhost:8000"
BUSQUEDA_URL = f"{API_BASE_URL}/rag_memory/"

st.set_page_config(page_title="Asistente RAG con Memoria", page_icon=":rocket:")

st.title("🤖 Asistente RAG con Memoria")

if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Haz una pregunta sobre tu documento..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Pensando...")

        payload = {
            "session_id": st.session_state.session_id,
            "consulta": prompt
        }

        try:
            response = requests.post(BUSQUEDA_URL, json=payload)
            response.raise_for_status()
            full_response = response.json().get("respuesta", "No se recibió respuesta.")
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except requests.exceptions.RequestException as e:
            st.error(f"Error al contactar la API: {e}")