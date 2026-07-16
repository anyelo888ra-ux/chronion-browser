# 🚀 Chronioñ Browser v1.0

¡Bienvenido a **Chronioñ**, un navegador web ultra ligero, minimalista y rápido desarrollado completamente en Python! 

Chronioñ está diseñado para ser portable: no necesita instaladores complejos, es solo un archivo ejecutable `.exe` listo para correr de forma nativa en Windows. Su motor gráfico utiliza la tecnología de Google Chrome (Blink) gracias a las librerías de PyQt5.

---

## 🎨 Características principales
* 🏎️ **Ultra ligero:** Corre directamente desde un archivo único en tu escritorio.
* 🛡️ **Portable:** Llévalo en tu pendrive o pásalo por Discord/WhatsApp a tus amigos sin instalar dependencias.
* 🌐 **Navegación fluida:** Botones de navegación esenciales (Atrás, Adelante, Recargar) y barra de direcciones inteligente.
* 🛸 **Identidad propia:** Icono personalizado tecnológico en forma de átomo azul orbital.

---

## 📦 Estructura del Proyecto

El repositorio está organizado de la siguiente manera:
* `/.pythons`: Código fuente original escrito en Python.
* `/bats`: Scripts de acceso rápido automatizados para Windows.
* `/icon`: Recursos visuales del navegador (formatos `.png` y `.ico`).
* `/exe`: La versión final compilada e independiente de Chronioñ listísima para usar.

---

## 🚀 Cómo usar Chronioñ

### Opción A: Solo quiero usar el navegador (Para usuarios)
1. Entra a la carpeta `/exe`.
2. Descarga el archivo `Chronioñ.exe`.
3. ¡Haz doble clic en tu escritorio y a navegar!
*(Nota: Al ser un ejecutable nuevo y personal, tu antivirus o Windows SmartScreen podría lanzar una advertencia flotante. Solo debes darle a "Ejecutar de todas formas" o añadir la exclusión en tu antivirus).*

### Opción B: Quiero ver o modificar el código (Para programadores)
Si quieres probar el código fuente, necesitas tener instalado Python 3.11+. Sigue estos comandos en tu consola:

1. Instala las dependencias necesarias:
   ```bash
   pip install PyQt5 PyQtWebEngine Pillow
   ```
2. Ejecuta el archivo de la carpeta de scripts:
   ```bash
   python .pythons/navegador.py
   ```

---

## 🛠️ Tecnologías utilizadas
* **Python 3.11** - Lenguaje base del proyecto.
* **PyQt5 & PyQtWebEngine** - Interfaz gráfica y motor del navegador.
* **PyInstaller** - Compilador para empaquetar el código en un ejecutable único.
* **Pillow** - Procesador de imágenes para la creación del icono nativo.

---
Creado con 💻 por **Anyeloxp**
