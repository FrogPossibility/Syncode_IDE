import sys
from PyQt6.QtCore import QUrl, pyqtSlot, QObject
from PyQt6.QtWidgets import QApplication, QFileDialog
from PyQt6.QtQml import QQmlApplicationEngine

class FileHandler(QObject):
    def __init__(self):
        super().__init__()
        self.current_file = ""

    @pyqtSlot()
    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(None, "Open File", "", "Text Files (*.txt);;Python Files (*.py);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r') as file:
                content = file.read()
                engine.rootObjects()[0].findChild(QObject, 'textArea').setProperty('text', content)
            self.current_file = file_name

    @pyqtSlot()
    def save_file(self):
        options = QFileDialog.Options()
        if not self.current_file:
            file_name, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Text Files (*.txt);;Python Files (*.py);;All Files (*)", options=options)
            if file_name:
                self.current_file = file_name
        else:
            file_name = self.current_file

        with open(file_name, 'w') as file:
            content = engine.rootObjects()[0].findChild(QObject, 'textArea').property('text')
            file.write(content)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()

    file_handler = FileHandler()
    engine.rootContext().setContextProperty("fileHandler", file_handler)

    engine.load(QUrl("editor.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())