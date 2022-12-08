#gui.py
#Gui to be created in hopes of showing the different progression of quests needed in order to complete each act in Path of Exile
from PyQt6.QtWidgets import *
import sys


#Create instance of QApplication
app = QApplication([])
#Create GUI
window = QWidget()
window.setWindowTitle("Poe quest GUI")
#Place it somewhere on the screen
window.setGeometry(0, 0, 800, 600)
#Create a label to fill in the window
helloMsg = QLabel("<h1>Hello, world!</h1>", parent=window)
#Place the message in a specific area of the window, used some weird math to make it look relatively centered
helloMsg.move(((window.width() // 2) - (window.width() // 9)),0)

#Create act one button
button1 = QPushButton(window)
button1.setText("Act One")
button1.move(((window.width() // 2) - (window.width() // 9)),(window.height() // 10))

#Create act two button
button2 = QPushButton(window)
button2.setText("Act Two")
button2.move(((window.width() // 2) + (window.width() // 14)),(window.height() // 10))

#Create act three button
button3 = QPushButton(window)
button3.setText("Act Three")
button3.move(((window.width() // 2) - (window.width() // 9)),(window.height() // 6))

#Create act four button
button4 = QPushButton(window)
button4.setText("Act Four")
button4.move(((window.width() // 2) + (window.width() // 14)),(window.height() // 6))

#Create act five button
button5 = QPushButton(window)
button5.setText("Act Five")
button5.move(((window.width() // 2) - (window.width() // 9)),(window.height() // 4)) #Fix this alignment


#Show the window
window.show()
sys.exit(app.exec())