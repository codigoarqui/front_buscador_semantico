import requests
import streamlit as st
import uuid
import base64

API_BASE_URL = "http://127.0.0.1:8000"
BUSQUEDA_URL = f"{API_BASE_URL}/agente-maestro-vision"

st.set_page_config(page_title="Asistente con Visión Gemini", page_icon=":eyes:")

st.title("🤖 Asistente con Visión Gemini")

if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if isinstance(message["content"], dict) and "image_data" in message["content"]:
            st.image(message["content"]["image_data"], caption="Imagen enviada", use_container_width=True)
            st.markdown(message["content"]["prompt"])
        else:
            st.markdown(message["content"])

if 'uploader_key' not in st.session_state:
    st.session_state.uploader_key = 0

uploaded_file = st.file_uploader(
    "Sube una imagen para que el agente la analice",
    type=["jpg", "jpeg", "png"],
    key=st.session_state.uploader_key
)

if prompt := st.chat_input("Haz una pregunta o describe la imagen..."):
    message_content_for_display = prompt
    image_base64_for_payload = None

    if uploaded_file is not None:
        image_bytes = uploaded_file.getvalue()
        image_base64_for_payload = base64.b64encode(image_bytes).decode('utf-8')
        
        message_content_for_display = {"image_data": image_bytes, "prompt": prompt}
        
        st.session_state.uploader_key += 1
        
    st.session_state.messages.append({"role": "user", "content": message_content_for_display})
    with st.chat_message("user"):
        if isinstance(message_content_for_display, dict):
            st.image(message_content_for_display["image_data"], caption="Imagen enviada", use_container_width=True)
            st.markdown(message_content_for_display["prompt"])
        else:
            st.markdown(message_content_for_display)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Pensando...")

        payload = {
            "session_id": st.session_state.session_id,
            "consulta": prompt,
            "image_base64": image_base64_for_payload
        }

        try:
            response = requests.post(BUSQUEDA_URL, json=payload)
            response.raise_for_status()
            full_response = response.json().get("respuesta", "No se recibió respuesta.")
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except requests.exceptions.RequestException as e:
            st.error(f"Error al contactar la API: {e}")
