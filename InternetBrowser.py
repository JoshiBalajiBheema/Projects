#### NOt working at the moment : issue with the module
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.urlbar = QLineEdit()
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished(self.update_title)

        self.status = QStatusBar()

        self.setCentralWidget(self.browser)

        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction("Forward", self)
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction("home", self)
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.Seperator()

        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navtb.addWidget(self.urlbar)

        stop_btn = QAction("Stop", self)
        stop_btn.triggered.connect(self, browser.stop)
        navtb.addAction(stop_btn)

        self.show()

    def navigate_to_url(self):
        q = QUrl(self.utlbar.text())
        if q.scheme() == "":
            self.setScheme("http")

        self.browser.setUrl(q)

    def navigate_home(self):
        self.browser.seturl(QUrl("https://google.com"))

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def update_title(self):
        title = set.browser.page().title()
        self.setWindowTitle(f"{title} - My Browser")


app = QApplication(sys.argv)
app.setApplicationName("My Browser")
window = MainWindow()
app.exec_()
