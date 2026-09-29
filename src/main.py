import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QLabel,
    QFileDialog,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal


from helper import *

class ClickableLabel(QLabel):

    next_page = Signal()
    previous_page = Signal()

    def mousePressEvent(self, event):
        size = self.size()

        if event.position().x() > size.width() / 2:
            self.next_page.emit()
            print("Next Page")
        else:
            self.previous_page.emit()
            print("Previous Page")

        print(event.position())

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.original_image = None
        self.original_pixmap = None
        central = QWidget()
        layout  = QVBoxLayout(central)

        self.image_label = ClickableLabel("Pick a folder")
        self.image_label.next_page.connect(self.next_image)
        self.image_label.previous_page.connect(self.previous_image)

        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button  = QPushButton("Open Folder")
        button.clicked.connect(self.pick_folder)

        layout.addWidget(self.image_label)
        layout.addWidget(button)

        self.setCentralWidget(central)

        self.image_idx = 0

    def next_image(self):
        self.image_idx = min(self.image_idx+1,len(self.files)-1)
        self.render_image()

    def previous_image(self):
        self.image_idx = max(self.image_idx-1,0)
        self.render_image()

    def pick_folder(self):
        self.image_idx = 0
        folder = choose_folder()

        files  = list_image(folder)
        self.files = files
        self.render_image()

    def render_image(self):
        print(self.image_idx)
        self.original_pixmap = QPixmap(self.files[self.image_idx])
        scaled = self.original_pixmap.scaled(
            self.image_label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.image_label.setPixmap(scaled)

    def resizeEvent(self, event):
        if self.original_pixmap is None:
            return
        self.image_label.setPixmap(
            self.original_pixmap.scaled(
                self.image_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )


app = QApplication(sys.argv)

window = ImageViewer()
window.show()
window.setStyleSheet("""
QMainWindow {
    background-color: #181818;
}

QLabel {
    color: white;
    font-size: 18px;
}

QPushButton {
    background-color: #2d2d2d;
    color: white;
    border: 1px solid #444;
    border-radius: 8px;
    padding: 8px 16px;
}

QPushButton:hover {
    background-color: #3a3a3a;
}

QPushButton:pressed {
    background-color: #555;
}
""")
app.exec()