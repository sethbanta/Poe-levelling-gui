#gui.py
#Gui to be created in hopes of showing the different progression of quests needed in order to complete each act in Path of Exile
from PyQt6.QtWidgets import *
import sys


#Create instance of QApplication
app = QApplication([])
#Create GUI
window = QStackedWidget()
window.setWindowTitle("Poe quest GUI")
#Place it somewhere on the screen
window.setGeometry(0, 0, 800, 600)

class mainMenu(QMainWindow): #page 1
    #Create a label to fill in the window
    helloMsg = QLabel("<h1>Hello, world!</h1>", parent=window)
    helloMsg.adjustSize() #this is needed for the label to not get cut off
    #Place the message in a specific area of the window, used some weird math to make it look relatively centered
    helloMsg.move(((window.width() // 2) - (window.width() // 9) - 20),0)

    #Create act one button
    button1 = QPushButton(window)
    button1.setText("Act One")
    button1.move(((window.width() // 2) - (window.width() // 9) - 66),(window.height() // 10))

    #Create act two button
    button2 = QPushButton(window)
    button2.setText("Act Two")
    button2.move(((window.width() // 2) + (window.width() // 14) - 66),(window.height() // 10))

    #Create act three button
    button3 = QPushButton(window)
    button3.setText("Act Three")
    button3.move(((window.width() // 2) - (window.width() // 9) - 66),(window.height() // 10) + 50)

    #Create act four button
    button4 = QPushButton(window)
    button4.setText("Act Four")
    button4.move(((window.width() // 2) + (window.width() // 14) - 66),(window.height() // 10) + 50)

    #Create act five button
    button5 = QPushButton(window)
    button5.setText("Act Five")
    button5.move(((window.width() // 2) - (window.width() // 9) - 66),(window.height() // 10) + 100)
    
    #Create act six button
    button6 = QPushButton(window)
    button6.setText("Act Six")
    button6.move(((window.width() // 2) + (window.width() // 14) - 66),(window.height() // 10) + 100)
    
    #Create act seven button
    button7 = QPushButton(window)
    button7.setText("Act Seven")
    button7.move(((window.width() // 2) - (window.width() // 9) - 66),(window.height() // 10) + 150)
    
    #Create act eight button
    button8 = QPushButton(window)
    button8.setText("Act Eight")
    button8.move(((window.width() // 2) + (window.width() // 14) - 66),(window.height() // 10) + 150)
    
    #Create act nine button
    button9 = QPushButton(window)
    button9.setText("Act Nine")
    button9.move(((window.width() // 2) - (window.width() // 9) - 66),(window.height() // 10) + 200)
    
    #Create act ten button
    button10 = QPushButton(window)
    button10.setText("Act Ten")
    button10.move(((window.width() // 2) + (window.width() // 14) - 66),(window.height() // 10) + 200)


#Show the window
window.show()
sys.exit(app.exec())