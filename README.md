# Frontend para Motor de Búsqueda Semántica con Streamlit

En este proyecto, crearemos una interfaz web simple para interactuar con la **API REST de búsqueda semántica**.

Para construir el frontend, utilizaremos **Streamlit**, una librería de Python que nos permite crear aplicaciones web interactivas de manera rápida y sin necesidad de escribir código HTML, CSS o JavaScript.

---

## 🛠️ Requisitos

Para poder ejecutar este proyecto, necesitarás:

* **Python 3.8+** instalado.
* Haber clonado y configurado el repositorio (link del repo), ya que este frontend se conecta directamente a esta API.

---

## 💻 Configuración del Proyecto

Sigue estos pasos para poner a funcionar el frontend en tu máquina local.

### 1. Clonar el Repositorio

Si aún no lo has hecho, clona este repositorio a tu máquina local usando `git`:

```bash
git clone git@github.com:codigoarqui/front_buscador_semantico.git
cd front_buscador_semantico
```

### 2. Configurar el Entorno de Python

Desde la terminal, en la raíz del proyecto, crea y activa un entorno virtual de Python.

**Para Windows:**

```bash
python3 -m venv venv
venv\Scripts\activate
```

**Para macOS y Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

Con el entorno virtual activado, instala todas las librerías necesarias. Para este proyecto, solo necesitas `streamlit` y `requests`.

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar la Aplicación

```bash
streamlit run frontend.py --server.port 8501
streamlit run frontend_rag.py --server.port 8502
streamlit run frontend_rag_conversacional.py --server.port 8503
streamlit run frontend_vision.py --server.port 8504
```

Streamlit abrirá automáticamente la aplicación en tu navegador web. Si no lo hace, puedes acceder a ella en `http://localhost:8501`.

Ahora, puedes escribir consultas en el campo de texto y hacer clic en **"Buscar"** para interactuar con tu motor de búsqueda semántica.

---

Si te ha sido útil, no olvides suscribirte a mi canal **Del Código a la Arquitectura** para más. ¡Nos vemos en la próxima! 🚀
