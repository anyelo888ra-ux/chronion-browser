import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView

class ChronioñDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana principal de la Demo
        self.setWindowTitle("Chronioñ Browser v1.1 [DEMO]")
        self.setGeometry(100, 100, 1024, 768)

        # Crear el motor de renderizado de páginas
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # Configurar Google como la página de inicio por defecto
        self.url_inicio = "https://google.com"
        self.browser.setUrl(QUrl(self.url_inicio))

        # Configurar la barra de herramientas superior
        barra_herramientas = QToolBar()
        self.addToolBar(barra_herramientas)

        # Botón Atrás
        btn_atras = QAction("⬅️", self)
        btn_atras.triggered.connect(self.browser.back)
        barra_herramientas.addAction(btn_atras)

        # Botón Adelante
        btn_adelante = QAction("➡️", self)
        btn_adelante.triggered.connect(self.browser.forward)
        barra_herramientas.addAction(btn_adelante)

        # Botón Recargar
        btn_recargar = QAction("🔄", self)
        btn_recargar.triggered.connect(self.browser.reload)
        barra_herramientas.addAction(btn_recargar)
        
        # Botón de Inicio (Home) - Ahora te regresa a Google directamente
        btn_inicio = QAction("🏠", self)
        btn_inicio.triggered.connect(lambda: self.browser.setUrl(QUrl(self.url_inicio)))
        barra_herramientas.addAction(btn_inicio)

        # Barra de direcciones superior
        self.barra_url = QLineEdit()
        self.barra_url.returnPressed.connect(self.navegar_a_url)
        barra_herramientas.addWidget(self.barra_url)

        # Rastrear cuando cambia la dirección de navegación para actualizar la barra
        self.browser.urlChanged.connect(self.actualizar_barra_url)

    def navegar_a_url(self):
        url_texto = self.barra_url.text().strip()
        if not url_texto:
            return
            
        # Si contiene espacios o no tiene un punto (ej: "hola"), busca limpiamente en Google Search
        if " " in url_texto or "." not in url_texto:
            url_texto = "https://google.com/search?q=" + url_texto.replace(" ", "+")
        else:
            # Si es una URL directa (ej: "youtube.com"), le ponemos https de forma segura
            if not url_texto.startswith("http://") and not url_texto.startswith("https://"):
                url_texto = "https://" + url_texto
                
        self.browser.setUrl(QUrl(url_texto))

    def actualizar_barra_url(self, url):
        self.barra_url.setText(url.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_navegador = ChronioñDemo()
    mi_navegador.show()
    sys.exit(app.exec_())
