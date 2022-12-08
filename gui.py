#gui.py
#Gui to be created in hopes of showing the different progression of quests needed in order to complete each act in Path of Exile
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
import sys


#Create instance of QApplication
app = QApplication([])

#Create GUI
window = QWidget()
window.setWindowTitle("Poe quest GUI")
#Place it somewhere on the screen
window.setGeometry(100, 100, 280, 80)
#Create a label to fill in the window
helloMsg = QLabel("<h1>Hello, world!</h1>", parent=window)
helloMsg.move(60,15)

#Show the window
window.show()
sys.exit(app.exec())