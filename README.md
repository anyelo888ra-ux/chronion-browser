# 🚀 Chronioñ Browser

¡Bienvenido a **Chronioñ**, un navegador web ultra ligero, minimalista y rápido desarrollado completamente en Python! 

Chronioñ está diseñado para ser portable y directo. En este repositorio encontrarás la versión **Chronioñ Demo**, la cual inicia de forma limpia cargando el buscador oficial de Google y cuenta con un motor inteligente para resolver búsquedas directamente desde la barra superior.

---

## 🎨 Características de la versión Demo
* 🏎️ **Ultra ligero:** Interfaz minimalista optimizada para consumir el mínimo de recursos.
* 🏠 **Inicio Estable:** Carga directamente la página principal de Google al arrancar.
* 🔍 **Buscador Inteligente:** Detecta automáticamente si escribiste una URL (ej. `youtube.com`) o palabras sueltas para redirigirte a Google Search de forma limpia.
* 🛸 **Identidad Visual:** Incluye los recursos visuales nativos (formato `.png` y `.ico`) con el diseño de átomo orbital azul.

---

## 📦 Estructura actual del repositorio

El proyecto está organizado de la siguiente manera de forma pública:
* 📁 **`chronioñ demo/`**
  * 📄 `navegador.py` -> Código fuente principal corregido de la Demo.
  * ⚙️ `Chronion.bat` -> Script de arranque rápido para Windows.
  * 🖼️ `icon.png` e `icon.ico` -> Logotipos oficiales en alta resolución.
* 📜 **`README.md`** -> Guía de presentación del proyecto.

---

## 🛠️ Cómo descargar y ejecutar la Demo

⚠️ **Nota Importante:** Para que el archivo ejecutable `.bat` funcione, es obligatorio que se descargue la carpeta completa o que mantengas los archivos `Chronion.bat` y `navegador.py` juntos en el mismo directorio.

### Paso 1: Clonar o descargar el proyecto
Puedes descargar el repositorio completo en formato `.ZIP` desde el botón verde **Code** de arriba y descomprimirlo en tu computadora.

### Paso 2: Instalar los requisitos básicos
Para que el motor gráfico de Chromium y las librerías de Python funcionen en tu PC, abre tu consola (CMD) e instala lo siguiente:
```bash
pip install PyQt5 PyQtWebEngine
```

### Paso 3: ¡A navegar!
Entra en la carpeta `chronioñ demo` y haz doble clic sobre el archivo **`Chronion.bat`**. Se abrirá el navegador Chronioñ de forma inmediata y automática sin dejar consolas negras de fondo.

---
## 💻 Tecnologías utilizadas
* **Python 3.11** - Lenguaje de programación base.
* **PyQt5 & PyQtWebEngine** - Interfaz de usuario y motor de renderizado web (Blink/Chromium).

---
Creado con 💻 por **Anyeloxp**
