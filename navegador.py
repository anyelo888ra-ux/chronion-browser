import sys
import sqlite3
import re
import os
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (QApplication, QMainWindow, QToolBar,
                             QLineEdit, QDialog, QVBoxLayout, QLabel, 
                             QPushButton, QHBoxLayout, QMessageBox, QFileDialog)
from PyQt6.QtGui import QAction
from PyQt6.QtWebEngineCore import QWebEngineProfile
from PyQt6.QtWebEngineWidgets import QWebEngineView

# --- 1. BASE DE DATOS LOCAL PARA CUENTAS DE CHRONIOÑ ---
def InicializarBaseDatos():
    conexion = sqlite3.connect("chronion_data.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE,
            clave TEXT,
            email TEXT UNIQUE
        )
    """)
    conexion.commit()
    conexion.close()

# --- 2. VENTANA DE REGISTRO E INICIO DE SESIÓN ---
class VentanaLogin(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chronioñ ID & Accounts")
        self.setFixedSize(360, 320)
        self.usuario_actual = None
        self.email_actual = None
        
        self.setStyleSheet("""
            QDialog { background-color: #121212; }
            QLabel { color: #ffffff; font-family: 'Segoe UI'; font-size: 13px; }
            QLineEdit { 
                background-color: #1e1e1e; color: white; 
                border: 1px solid #333; border-radius: 6px; 
                padding: 8px; font-size: 14px; 
            }
            QLineEdit:focus { border: 1px solid #00d2ff; }
            QPushButton { 
                background-color: #00d2ff; color: #121212; 
                border-radius: 6px; padding: 8px 15px; 
                font-weight: bold; font-size: 13px;
            }
            QPushButton:hover { background-color: #00b5dc; }
        """)
        
        layout = QVBoxLayout()
        self.lbl_info = QLabel("<h2 style='color:#00d2ff; margin-bottom:0;'>Chronioñ Accounts</h2><p style='color:#888; margin-top:0;'>Crea tu correo personalizado @chronion.com</p>")
        layout.addWidget(self.lbl_info)
        
        self.txt_usuario = QLineEdit()
        self.txt_usuario.setPlaceholderText("Nombre de usuario")
        layout.addWidget(self.txt_usuario)
        
        self.txt_clave = QLineEdit()
        self.txt_clave.setPlaceholderText("Contraseña")
        self.txt_clave.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.txt_clave)
        
        btn_layout = QHBoxLayout()
        self.btn_login = QPushButton("Iniciar Sesión")
        self.btn_registro = QPushButton("Registrarse")
        self.btn_registro.setStyleSheet("background-color: #222; color: white; border: 1px solid #444;")
        
        btn_layout.addWidget(self.btn_login)
        btn_layout.addWidget(self.btn_registro)
        layout.addLayout(btn_layout)
        self.setLayout(layout)
        
        self.btn_login.clicked.connect(self.verificar_login)
        self.btn_registro.clicked.connect(self.registrar_usuario)

    def verificar_login(self):
        user = self.txt_usuario.text().strip()
        password = self.txt_clave.text().strip()
        
        if not user or not password:
            QMessageBox.warning(self, "Campos Vacíos", "Por favor completa todos los campos.")
            return

        conexion = sqlite3.connect("chronion_data.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT usuario, email FROM usuarios WHERE usuario = ? AND clave = ?", (user, password))
        resultado = cursor.fetchone()
        conexion.close()
        
        if resultado:
            self.usuario_actual = resultado[0]
            self.email_actual = resultado[1]
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")

    def registrar_usuario(self):
        user = self.txt_usuario.text().strip()
        password = self.txt_clave.text().strip()
        
        if not user or not password:
            QMessageBox.warning(self, "Error", "Rellena todos los campos para el registro.")
            return
            
        if not re.match("^[a-zA-Z0-9_]+$", user):
            QMessageBox.warning(self, "Usuario Inválido", "El usuario solo puede contener letras, números o guiones bajos.")
            return

        email_custom = f"{user.lower()}@chronion.com"
            
        try:
            conexion = sqlite3.connect("chronion_data.db")
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO usuarios (usuario, clave, email) VALUES (?, ?, ?)", (user, password, email_custom))
            conexion.commit()
            conexion.close()
            QMessageBox.information(self, "¡Bienvenido!", f"¡Cuenta de Chronioñ Creada!\n\nTu correo asignado es:\n{email_custom}")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Error", "El nombre de usuario ya está registrado.")

# --- 3. HTML INTERNO PARA PÁGINAS ESPECIALES CHRONION:// Y CHRONIOÑ:// ---
PAGINAS_INTERNAS = {
    "about": """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Acerca de Chronioñ</title>
            <style>
                body { background-color: #121212; color: #e2e8f0; font-family: 'Segoe UI', Tahoma, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
                .card { background: #1e1e24; padding: 40px; border-radius: 16px; border: 1px solid #2d2d38; max-width: 500px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
                h1 { color: #00d2ff; margin-bottom: 5px; }
                p { color: #94a3b8; font-size: 0.95rem; line-height: 1.6; }
                .badge { background: #00d2ff; color: #121212; padding: 4px 10px; border-radius: 12px; font-weight: bold; font-size: 0.8rem; }
                .info-box { background: #141419; padding: 15px; border-radius: 8px; margin-top: 20px; text-align: left; font-family: monospace; font-size: 0.85rem; color: #38bdf8; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🛸 Chronioñ Browser</h1>
                <p><span class="badge">v1.3 Multi-Lang</span></p>
                <p>Navegador web ultra ligero, minimalista y seguro optimizado con PyQt y motor Chromium.</p>
                <div class="info-box">
                    • Motor: Blink / WebEngine<br>
                    • ID & Accounts: Integrado (@chronion.com)<br>
                    • Esquemas soportados: chronion:// y chronioñ://<br>
                    • Desarrollador: Anyeloxp / anyelo888ra-ux
                </div>
            </div>
        </body>
        </html>
    """,
    "version": """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Versión de Chronioñ</title>
            <style>
                body { background-color: #121212; color: #e2e8f0; font-family: 'Segoe UI', sans-serif; padding: 40px; }
                h2 { color: #00d2ff; }
                table { width: 100%; border-collapse: collapse; margin-top: 20px; }
                td, th { border-bottom: 1px solid #2d2d38; padding: 12px; text-align: left; }
                th { color: #94a3b8; }
            </style>
        </head>
        <body>
            <h2>Información de Versión - Chronioñ Browser</h2>
            <table>
                <tr><th>Componente</th><th>Detalle</th></tr>
                <tr><td>Navegador</td><td>Chronioñ Browser v1.3</td></tr>
                <tr><td>Motor Web</td><td>PyQtWebEngine (Chromium Core)</td></tr>
                <tr><td>Base de Datos</td><td>SQLite3 (chronion_data.db)</td></tr>
                <tr><td>Protocolos Internos</td><td>chronion://, chronioñ://, about:chronion, about:chronioñ</td></tr>
            </table>
        </body>
        </html>
    """,
    "flags": """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Configuración Experimental</title>
            <style>
                body { background-color: #121212; color: #e2e8f0; font-family: 'Segoe UI', sans-serif; padding: 40px; }
                h2 { color: #00d2ff; }
                .flag { background: #1e1e24; padding: 15px; border-radius: 8px; margin-bottom: 10px; border: 1px solid #2d2d38; }
                .flag-title { color: #38bdf8; font-weight: bold; }
            </style>
        </head>
        <body>
            <h2>⚙️ Chronioñ Flags & Experimentos</h2>
            <div class="flag">
                <span class="flag-title">#enable-hardware-acceleration</span>
                <p>Aceleración por GPU para la renderización de páginas WebGL.</p>
            </div>
            <div class="flag">
                <span class="flag-title">#chronion-id-sync</span>
                <p>Sincronización automática de perfil de usuario local @chronion.com.</p>
            </div>
        </body>
        </html>
    """
}

# --- 4. VENTANA PRINCIPAL DEL NAVEGADOR ---
class ChronioñCompleto(QMainWindow):
    def __init__(self, usuario, email):
        super().__init__()
        self.usuario_sesion = usuario
        self.email_sesion = email
        self.setWindowTitle(f"Chronioñ Browser v1.3 - [{self.usuario_sesion}]")
        self.setGeometry(100, 100, 1024, 768)
        self.setStyleSheet("QMainWindow { background-color: #121212; }")

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # ⚙️ --- CONFIGURAR EL SISTEMA DE DESCARGAS ---
        perfil = QWebEngineProfile.defaultProfile()
        perfil.downloadRequested.connect(self.gestionar_descarga)

        # 🌐 --- MOTOR DE BÚSQUEDA Y PÁGINA DE INICIO OFICIAL CHRONIOÑ ---
        self.url_inicio = "https://chronion-search.duckdns.org/"
        self.browser.setUrl(QUrl(self.url_inicio))

        # --- BARRA DE HERRAMIENTAS MODO OSCURO ---
        barra_herramientas = QToolBar()
        barra_herramientas.setStyleSheet("""
            QToolBar { background-color: #1e1e1e; border-bottom: 1px solid #2d2d2d; padding: 6px; spacing: 12px; }
        """)
        self.addToolBar(barra_herramientas)

        btn_atras = QAction("⬅️", self)
        btn_atras.triggered.connect(self.browser.back)
        barra_herramientas.addAction(btn_atras)

        btn_adelante = QAction("➡️", self)
        btn_adelante.triggered.connect(self.browser.forward)
        barra_herramientas.addAction(btn_adelante)

        btn_recargar = QAction("🔄", self)
        btn_recargar.triggered.connect(self.browser.reload)
        barra_herramientas.addAction(btn_recargar)
        
        btn_inicio = QAction("🏠", self)
        btn_inicio.triggered.connect(lambda: self.browser.setUrl(QUrl(self.url_inicio)))
        barra_herramientas.addAction(btn_inicio)

        self.barra_url = QLineEdit()
        self.barra_url.returnPressed.connect(self.navegar_a_url)
        self.barra_url.setStyleSheet("""
            QLineEdit {
                background-color: #2a2a2a; color: #ffffff; border: 1px solid #3d3d3d;
                border-radius: 15px; padding: 6px 15px; font-size: 14px; font-family: 'Segoe UI', Arial;
            }
            QLineEdit:focus { border: 1px solid #00d2ff; background-color: #333333; }
        """)
        barra_herramientas.addWidget(self.barra_url)

        self.lbl_perfil = QLabel(f" 👤 {self.email_sesion} ")
        self.lbl_perfil.setStyleSheet("color: #00d2ff; font-weight: bold; font-family: 'Segoe UI'; font-size: 12px; margin-right: 5px;")
        barra_herramientas.addWidget(self.lbl_perfil)

        self.browser.urlChanged.connect(self.actualizar_barra_url)

    # 📥 --- FUNCIÓN PARA DETECTAR Y EJECUTAR DESCARGAS ---
    def gestionar_descarga(self, item):
        nombre_archivo = item.suggestedFileName()
        ruta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
        ruta_completa = os.path.join(ruta_descargas, nombre_archivo)
        
        ruta_guardado, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", ruta_completa)
        
        if ruta_guardado:
            item.setDownloadDirectory(os.path.dirname(ruta_guardado))
            item.setDownloadFileName(os.path.basename(ruta_guardado))
            item.accept()
            QMessageBox.information(self, "Descarga Iniciada", f"Descargando:\n{nombre_archivo}\n\nRevisa tu carpeta de Descargas.")

    # 🔍 --- NAVEGACIÓN CON SOPORTE INTERNO PARA CHRONION:// Y CHRONIOÑ:// ---
    def navegar_a_url(self):
        url_texto = self.barra_url.text().strip()
        if not url_texto:
            return

        # Detección de esquema de URL interna (chronion://, chronioñ://, about:chronion, etc.)
        pattern_internal = r'^(chronion|chronioñ|about)[:/]+([a-zA-Z0-9_-]+)$'
        match = re.match(pattern_internal, url_texto.lower())
        
        if match:
            pagina = match.group(2)
            if pagina in PAGINAS_INTERNAS:
                self.browser.setHtml(PAGINAS_INTERNAS[pagina])
                return
            else:
                self.browser.setHtml(f"<body style='background:#121212;color:white;font-family:sans-serif;'><h2>404 - Página Interna chronion://{pagina} no encontrada</h2></body>")
                return

        if " " in url_texto or "." not in url_texto:
            url_texto = "https://chronion-search.duckdns.org/search.html?q=" + url_texto.replace(" ", "+")
        else:
            if not url_texto.startswith("http://") and not url_texto.startswith("https://"):
                url_texto = "https://" + url_texto
                
        self.browser.setUrl(QUrl(url_texto))

    def actualizar_barra_url(self, url):
        self.barra_url.setText(url.toString())

if __name__ == "__main__":
    InicializarBaseDatos()
    app = QApplication(sys.argv)
    
    login = VentanaLogin()
    if login.exec() == QDialog.DialogCode.Accepted:
        mi_navegador = ChronioñCompleto(login.usuario_actual, login.email_actual)
        mi_navegador.show()
        sys.exit(app.exec())
