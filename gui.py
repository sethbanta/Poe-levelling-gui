#gui.py
#Gui to be created in hopes of showing the different progression of quests needed in order to complete each act in Path of Exile
from PyQt6.QtWidgets import *
import sys


#Create instance of QApplication
app = QApplication([])
#Create widgets for each button
mainMenuWidget = QWidget()
actOneWidget = QWidget()
actTwoWidget = QWidget()
actThreeWidget = QWidget()
actFourWidget = QWidget()
actFiveWidget = QWidget()
actSixWidget = QWidget()
actSevenWidget = QWidget()
actEightWidget = QWidget()
actNineWidget = QWidget()
actTenWidget = QWidget()
#Create GUI
window = QStackedLayout()
mainMenuWidget.setWindowTitle("Poe quest GUI")
#Place it somewhere on the screen
mainMenuWidget.setGeometry(0, 0, 800, 600)

class mainMenu(QMainWindow): #page 1
    #Create a label to fill in the window
    helloMsg = QLabel("<h1>Hello, world!</h1>", parent=mainMenuWidget)
    helloMsg.adjustSize() #this is needed for the label to not get cut off
    #Place the message in a specific area of the window, used some weird math to make it look relatively centered
    helloMsg.move(((mainMenuWidget.width() // 2) - (mainMenuWidget.width() // 9) - 20),0)

    #Create act one button
    button1 = QPushButton(mainMenuWidget)
    button1.setText("Act One")
    button1.move(((mainMenuWidget.width() // 2) - (mainMenuWidget.width() // 9) - 66),(mainMenuWidget.height() // 10))

    #Create act two button
    button2 = QPushButton(mainMenuWidget)
    button2.setText("Act Two")
    button2.move(((mainMenuWidget.width() // 2) + (mainMenuWidget.width() // 14) - 66),(mainMenuWidget.height() // 10))

    #Create act three button
    button3 = QPushButton(mainMenuWidget)
    button3.setText("Act Three")
    button3.move(((mainMenuWidget.width() // 2) - (mainMenuWidget.width() // 9) - 66),(mainMenuWidget.height() // 10) + 50)

    #Create act four button
    button4 = QPushButton(mainMenuWidget)
    button4.setText("Act Four")
    button4.move(((mainMenuWidget.width() // 2) + (mainMenuWidget.width() // 14) - 66),(mainMenuWidget.height() // 10) + 50)

    #Create act five button
    button5 = QPushButton(mainMenuWidget)
    button5.setText("Act Five")
    button5.move(((mainMenuWidget.width() // 2) - (mainMenuWidget.width() // 9) - 66),(mainMenuWidget.height() // 10) + 100)
    
    #Create act six button
    button6 = QPushButton(mainMenuWidget)
    button6.setText("Act Six")
    button6.move(((mainMenuWidget.width() // 2) + (mainMenuWidget.width() // 14) - 66),(mainMenuWidget.height() // 10) + 100)
    
    #Create act seven button
    button7 = QPushButton(mainMenuWidget)
    button7.setText("Act Seven")
    button7.move(((mainMenuWidget.width() // 2) - (mainMenuWidget.width() // 9) - 66),(mainMenuWidget.height() // 10) + 150)
    
    #Create act eight button
    button8 = QPushButton(mainMenuWidget)
    button8.setText("Act Eight")
    button8.move(((mainMenuWidget.width() // 2) + (mainMenuWidget.width() // 14) - 66),(mainMenuWidget.height() // 10) + 150)
    
    #Create act nine button
    button9 = QPushButton(mainMenuWidget)
    button9.setText("Act Nine")
    button9.move(((mainMenuWidget.width() // 2) - (mainMenuWidget.width() // 9) - 66),(mainMenuWidget.height() // 10) + 200)
    
    #Create act ten button
    button10 = QPushButton(mainMenuWidget)
    button10.setText("Act Ten")
    button10.move(((mainMenuWidget.width() // 2) + (mainMenuWidget.width() // 14) - 66),(mainMenuWidget.height() // 10) + 200)

class actOneMenu(QMainWindow):
    actOneWidget.setWindowTitle("Poe quest GUI")
    actOneWidget.setGeometry(0, 0, 800, 600)
    title = QLabel("<h1>Act One</h1>", parent=actOneWidget)
    

window.addWidget(mainMenuWidget)
window.addWidget(actOneWidget)
window.setCurrentWidget(mainMenuWidget)
#Show the window
sys.exit(app.exec())