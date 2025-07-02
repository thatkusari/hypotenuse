import sys
import math
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QFile
from PySide6.QtGui import QIcon
from output import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.form_widget = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.form_widget)
        self.setCentralWidget(self.form_widget)
        self.setWindowTitle("Hypotenuse Calculator")
        self.setWindowIcon(QIcon("hippo.png"))
        self.ui.calculateButton.released.connect(self.calculate_hypotenuse)

    def calculate_hypotenuse(self):
        triWidth = self.ui.widthLineEdit.text()
        triHeight = self.ui.heightLineEdit.text()
        try:
            hypotenuse = math.sqrt(
                float(triWidth) ** 2 + float(triHeight) ** 2)
            self.ui.resultLineEdit.setText(str(hypotenuse))
        except ValueError:
            self.ui.resultLineEdit.setText("Please enter valid numbers.")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
