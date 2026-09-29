import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QPushButton,
)
from PySide6.QtCore import Slot
import os

@Slot()
def choose_folder():
    print("Choose a folder")
    folder_path = QFileDialog.getExistingDirectory()
    print(f"Choose : {folder_path}")
    return folder_path

def list_image(path):
    files = os.listdir(path=path)
    files.sort(key=lambda x: int(x.split(".")[0]))
    files = [os.path.join(path,f) for f in files]
    return files