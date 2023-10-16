from gui import Window
import sys
from PyQt6.QtWidgets import QApplication


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
