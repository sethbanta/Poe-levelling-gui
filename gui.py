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

#Define a function for switching to the main menu
def mainMenuSwitch(event):
    window.setCurrentIndex(0)

#Define a function for switching to the act one menu
def actOneSwitch(event):
    window.setCurrentIndex(1)

#Define a function for switching to the act two menu
def actTwoSwitch(event):
    window.setCurrentIndex(2)
    
def actThreeSwitch(event):
    window.setCurrentIndex(3)

def actFourSwitch(event):
    window.setCurrentIndex(4)
    
def actFiveSwitch(event):
    window.setCurrentIndex(5)

def actSixSwitch(event):
    window.setCurrentIndex(6)

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
    button1.clicked.connect(actOneSwitch)

    #Create act two button
    button2 = QPushButton(mainMenuWidget)
    button2.setText("Act Two")
    button2.move(((mainMenuWidget.width() // 2) + (mainMenuWidget.width() // 14) - 66),(mainMenuWidget.height() // 10))
    button2.clicked.connect(actTwoSwitch)

    #Create act three button
    button3 = QPushButton(mainMenuWidget)
    button3.setText("Act Three")
    button3.move(((mainMenuWidget.width() // 2) - (mainMenuWidget.width() // 9) - 66),(mainMenuWidget.height() // 10) + 50)
    button3.clicked.connect(actThreeSwitch)

    #Create act four button
    button4 = QPushButton(mainMenuWidget)
    button4.setText("Act Four")
    button4.move(((mainMenuWidget.width() // 2) + (mainMenuWidget.width() // 14) - 66),(mainMenuWidget.height() // 10) + 50)
    button4.clicked.connect(actFourSwitch)

    #Create act five button
    button5 = QPushButton(mainMenuWidget)
    button5.setText("Act Five")
    button5.move(((mainMenuWidget.width() // 2) - (mainMenuWidget.width() // 9) - 66),(mainMenuWidget.height() // 10) + 100)
    button5.clicked.connect(actFiveSwitch)
    
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
    #Set the widget up
    actOneWidget.setWindowTitle("Poe quest GUI")
    actOneWidget.setGeometry(0, 0, 800, 600)
    #Add the title and position it
    title = QLabel("<h1>Act One</h1>", parent=actOneWidget)
    title.adjustSize()
    title.move(((mainMenuWidget.width() // 2) - (mainMenuWidget.width() // 9) - 20),0)
    #Begin adding each quest
    twilightStrand = QLabel("<b>01.</b> Find and kill Hillock", parent=actOneWidget)
    twilightStrand.move(0, 20)
    coast = QLabel("<b>02.</b> Find the Mud Flats", parent=actOneWidget)
    coast.move(0,35)
    coastWaypoint = QLabel("<b>02a.</b> Grab the waypoint before entering the Mud Flats", parent=actOneWidget)
    coastWaypoint.move(0,50)
    mudFlats = QLabel("<b>03.</b> Find all three Glyphs then open the Submerged Passage", parent=actOneWidget)
    mudFlats.move(0,65)
    submergedPassage = QLabel("<b>04.</b> Find the Ledge", parent=actOneWidget)
    submergedPassage.move(0,80)
    submergedPassageWaypoint = QLabel("<b>04a.</b> Grab the waypoint for the Dweller skill quest", parent=actOneWidget)
    submergedPassageWaypoint.move(0,95)
    ledge = QLabel("<b>05.</b> Find the climb", parent=actOneWidget)
    ledge.move(0,110)
    dwellerOne = QLabel("<b>05a.</b> Take the waypoint to the Submerged Passage (optional quest, rewards skill point)", parent=actOneWidget)
    dwellerOne.move(0,125)
    dwellerTwo = QLabel("<b>05b.</b> Find the Flooded Depths", parent=actOneWidget)
    dwellerTwo.move(0,140)
    dwellerThree = QLabel("<b>05c.</b> Kill the Dweller of the Deep", parent=actOneWidget)
    dwellerThree.move(0,155)
    climb = QLabel("<b>06.</b> Find the Lower Prison", parent=actOneWidget)
    climb.move(0,170)
    lowerPrison = QLabel("<b>07.</b> Find the Upper Prison", parent=actOneWidget)
    lowerPrison.move(0,185)
    prisonTrial = QLabel("<b>07a.</b> Find and solve the Trial of Ascendancy (optional, can be finished later but should we done right away to avoid back tracking)", parent=actOneWidget)
    prisonTrial.move(0,200)
    upperPrison = QLabel("<b>08.</b> Find the Wardens Chambers", parent=actOneWidget)
    upperPrison.move(0,215)
    wardensChambers = QLabel("<b>09.</b> Kill Brutus", parent=actOneWidget)
    wardensChambers.move(0,230)
    prisonersGate = QLabel("<b>10.</b> Find the Ship Graveyard", parent=actOneWidget)
    prisonersGate.move(0,245)
    shipGraveyardWaypoint = QLabel("<b>10a.</b> Grab the Ship Graveyard Waypoint", parent=actOneWidget)
    shipGraveyardWaypoint.move(0,260)
    shipGraveyardSkillOne = QLabel("<b>10a.</b> Find the Ship Graveyard Cave", parent=actOneWidget)
    shipGraveyardSkillOne.move(0,275)
    shipGraveyardSkillTwo = QLabel("<b>10b.</b> Find the Allflame", parent=actOneWidget)
    shipGraveyardSkillTwo.move(0,290)
    shipGraveyardSkillThree = QLabel("<b>10c.</b> Find Fairgraves", parent=actOneWidget)
    shipGraveyardSkillThree.move(0,305)
    shipGraveyardSkillFour = QLabel("<b>10d.</b> Kill Fairgraves (optional quest, rewards skill point)", parent=actOneWidget)
    shipGraveyardSkillFour.move(0,320)
    shipGraveyard = QLabel("<b>11.</b> Find the Cavern of Wrath", parent=actOneWidget)
    shipGraveyard.move(0,335)
    cavernWrath = QLabel("<b>12. </b> Find the Cavern of Anger", parent=actOneWidget)
    cavernWrath.move(0,350)
    cavernAnger = QLabel("<b>13.</b> Find Merveil, the Siren", parent=actOneWidget)
    cavernAnger.move(0,365)
    killMerv = QLabel("<b>14.</b> Kill Merveil, the Siren", parent=actOneWidget)
    killMerv.move(0,380)
    southernForest = QLabel("<b>15.</b> Travel to the Southern Forest", parent=actOneWidget)
    southernForest.move(0,395)
    actTwoButton = QPushButton(actOneWidget)
    actTwoButton.setText("Act Two")
    actTwoButton.move(0,415)
    mainMenuButton = QPushButton(actOneWidget)
    mainMenuButton.setText("Main Menu")
    mainMenuButton.move(100,415)
    mainMenuButton.clicked.connect(mainMenuSwitch)
    actTwoButton.clicked.connect(actTwoSwitch)

#Create and fill the act two widget
class actTwoMenu(QMainWindow):
    #Set the widget up
    actTwoWidget.setWindowTitle("Poe quest GUI")
    actTwoWidget.setGeometry(0, 0, 800, 600)
    title = QLabel("<b>Act Two</b>", parent=actTwoWidget)
    findTown = QLabel("<b>01.</b> Find the Forest Encampment", parent=actTwoWidget)
    findTown.move(0,15)
    oldFields = QLabel("<b>02.</b> Travel to the Old Fields", parent=actTwoWidget)
    oldFields.move(0,30)
    crossroads = QLabel("<b>03.</b> Find the Crossroads", parent=actTwoWidget)
    crossroads.move(0,45)
    crossroadsWp = QLabel("<b>03a.</b> Grab the Crossroads waypoint", parent=actTwoWidget)
    crossroadsWp.move(0,60)
    fellshrine = QLabel("<b>03b.</b> Find the Fellshrine Ruins", parent=actTwoWidget)
    fellshrine.move(0,75)
    crypt = QLabel("<b>01.</b> Find the Crypt and solve the trial of ascendancy", parent=actTwoWidget)
    crypt.move(0,90)
    chamberSin = QLabel("<b>04.</b> Find the Chamber of Sin", parent=actTwoWidget)
    chamberSin.move(0,105)
    chamberSinTwo = QLabel("<b>05.</b> Find the Chamber of Sins Level 2", parent=actTwoWidget)
    chamberSinTwo.move(0,120)
    chamberSinTrial = QLabel("<b>05a.</b> Find and solve the Trial of Ascendancy", parent=actTwoWidget)
    chamberSinTrial.move(0,135)
    chamberSinBoss = QLabel("<b>06.</b> Find and rescue Helena", parent=actTwoWidget)
    chamberSinBoss.move(0,150)
    crossroadsTwo = QLabel("<b>07.</b> Travel to the Crossroads", parent=actTwoWidget)
    crossroadsTwo.move(0,165)
    brokenBridge = QLabel("<b>08.</b> Find the Broken Bridge", parent=actTwoWidget)
    brokenBridge.move(0,180)
    kraityn = QLabel("<b>09.</b> Find and kill Kraityn", parent=actTwoWidget)
    kraityn.move(0,195)
    riverways = QLabel("<b>10.</b> Travel to the Riverways", parent=actTwoWidget)
    riverways.move(0,210)
    riverwaysWp = QLabel("<b>10a.</b> Grab the Riverways waypoint", parent=actTwoWidget)
    riverwaysWp.move(0,225)
    westernForest = QLabel("<b>11.</b> Find the Western Forest", parent=actTwoWidget)
    westernForest.move(0,240)
    westernWp = QLabel("<b>11a.</b> Grab the Western Forest waypoint", parent=actTwoWidget)
    westernWp.move(0,255)
    alira = QLabel("<b>12.</b> Find and kill Alira", parent=actTwoWidget)
    alira.move(0,270)
    wayForward = QLabel("<b>12a.</b> Find and kill the Black Captain, take the emblem and use to open the path", parent=actTwoWidget)
    wayForward.move(0,285)
    weaver = QLabel("<b>13.</b> Find the Weavers Chambers", parent=actTwoWidget)
    weaver.move(0,300)
    weaverNest = QLabel("<b>14.</b> Find the Weavers Nest", parent=actTwoWidget)
    weaverNest.move(0,315)
    weaverKill = QLabel("<b>15.</b> Kill the Weaver", parent=actTwoWidget)
    weaverKill.move(0,330)
    weaverSpike = QLabel("<b>16.</b> Take Maligaros Spike", parent=actTwoWidget)
    weaverSpike.move(0,345)
    riverwayTwo = QLabel("<b>17.</b> Travel to the Riverways", parent=actTwoWidget)
    riverwayTwo.move(0,360)
    wetlands = QLabel("<b>18.</b> Find the Wetlands", parent=actTwoWidget)
    wetlands.move(0,375)
    oak = QLabel("<b>19.</b> Find and kill Oak", parent=actTwoWidget)
    oak.move(0,390)
    ruins = QLabel("<b>20.</b> Find the Vaal Ruins", parent=actTwoWidget)
    ruins.move(0,405)
    ruinsWp = QLabel("<b>20a.</b> Grab the Wetlands waypoint", parent=actTwoWidget)
    ruinsWp.move(0,420)
    ruinsTwo = QLabel("<b>21.</b> Travel to the Forest Encampment", parent=actTwoWidget)
    ruinsTwo.move(0,435)
    apex = QLabel("<b>22.</b> Talk to Eramir and take the Apex", parent=actTwoWidget)
    apex.move(0,450)
    ruinsThree = QLabel("<b>23.</b> Travel to the Wetlands", parent=actTwoWidget)
    ruinsThree.move(0,465)
    ruinsFour = QLabel("<b>24.</b> Use Maligaros Spike to clear the roots and travel to the Vaal Ruins", parent=actTwoWidget)
    ruinsFour.move(0,480)
    ball = QLabel("<b>25.</b> Find the seal and release it then travel to the Nothern Forest", parent=actTwoWidget)
    ball.move(0,495)
    northern = QLabel("<b>26.</b> Find the Caverns", parent=actTwoWidget)
    northern.move(0,510)
    caverns = QLabel("<b>27.</b> Find the Ancient Pyramid", parent=actTwoWidget)
    caverns.move(0,525)
    pyramid = QLabel("<b>28.</b> Find the Pyramid Apex", parent=actTwoWidget)
    pyramid.move(0,540)
    killPyramid = QLabel("<b>29.</b> Kill the Vaal Oversoul", parent=actTwoWidget)
    killPyramid.move(0,555)
    city = QLabel("<b>30.</b> Travel to the City of Sarn", parent=actTwoWidget)
    city.move(0,570)
    actThreeButton = QPushButton(actTwoWidget)
    actThreeButton.setText("Act Three")
    actThreeButton.move(200,525)
    mainMenuButton = QPushButton(actTwoWidget)
    mainMenuButton.setText("Main Menu")
    mainMenuButton.move(200,555)
    mainMenuButton.clicked.connect(mainMenuSwitch)
    actThreeButton.clicked.connect(actThreeSwitch)
    
#Create and fill the act three widget
class actThreeMenu(QMainWindow):
    actThreeWidget.setWindowTitle("Poe quest GUI")
    actThreeWidget.setGeometry(0, 0, 800, 600)
    title = QLabel("<b>Act Three</b>", parent=actThreeWidget)
    clarissa = QLabel("<b>01.</b> Find and help Clarissa", parent=actThreeWidget)
    clarissa.move(0,15)
    sarn = QLabel("<b>02.</b> Find the City of Sarn", parent=actThreeWidget)
    sarn.move(0,30)
    slums = QLabel("<b>03.</b> Travel to the Slums", parent=actThreeWidget)
    slums.move(0,45)
    crema = QLabel("<b>04.</b> Find the Crematorium", parent=actThreeWidget)
    crema.move(0,60)
    #trial skip 15
    cremaPiety = QLabel("<b>05.</b> Find and solve the trial of Ascendancy then kill Piety", parent=actThreeWidget)
    cremaPiety.move(0,75)
    cremaTolman = QLabel("<b>06.</b> Take Tolmans bracelet", parent=actThreeWidget)
    cremaTolman.move(0,90)
    cremaClarissa = QLabel("<b>07.</b> Travel to the Sarn Encampment and take the keys from Clarissa", parent=actThreeWidget)
    cremaClarissa.move(0,105)
    slumsTwo = QLabel("<b>08.</b> Travel to the Slums", parent=actThreeWidget)
    slumsTwo.move(0,120)
    sewerGrate = QLabel("<b>09.</b> Find the sewer grate and enter the Sewers", parent=actThreeWidget)
    sewerGrate.move(0,135)
    sewerWp = QLabel("<b>09a.</b> Grab the Sewers waypoint", parent=actThreeWidget)
    sewerWp.move(0,150)
    busts = QLabel("<b>09b.</b> Find all three of Victarios Busts", parent=actThreeWidget)
    busts.move(0,165)
    sewers = QLabel("<b>10.</b> Find the Marketplace", parent=actThreeWidget)
    sewers.move(0,180)
    marketplaceWp = QLabel("<b>10a.</b> Grab the Marketplace waypoint", parent=actThreeWidget)
    marketplaceWp.move(0,195)
    catacombs = QLabel("<b>10b.</b> Find and travel to the Catacombs", parent=actThreeWidget)
    catacombs.move(0,210)
    catacombsTrial = QLabel("<b>10c.</b> Find and solve the trial of ascendancy", parent=actThreeWidget)
    catacombsTrial.move(0,225)
    marketplace = QLabel("<b>11.</b> Find the Battlegrounds", parent=actThreeWidget)
    marketplace.move(0,240)
    battlegrounds = QLabel("<b>12.</b> Find and take the Ribbon Spool", parent=actThreeWidget)
    battlegrounds.move(0,255)
    battlegroundWp = QLabel("<b>12a.</b> Grab the Battlegrounds waypoint", parent=actThreeWidget)
    battlegroundWp.move(0,270)
    docks = QLabel("<b>13.</b> Find the Docks", parent=actThreeWidget)
    docks.move(0,285)
    sulphite = QLabel("<b>14.</b> Find and take the Sulphite", parent=actThreeWidget)
    sulphite.move(0,300)
    battlegroundsTwo = QLabel("<b>15.</b> Travel to the Battlegrounds", parent=actThreeWidget)
    battlegroundsTwo.move(0,315)
    solaris = QLabel("<b>16.</b> Find the Solaris Temple level 1", parent=actThreeWidget)
    solaris.move(0,330)
    solarisTwo = QLabel("<b>17.</b> Find the Solaris Temple level 2", parent=actThreeWidget)
    solarisTwo.move(0,345)
    dialla = QLabel("<b>18.</b> Find and talk to Dialla for the Infernal Talc", parent=actThreeWidget)
    dialla.move(0,360)
    sewersTwo = QLabel("<b>19.</b> Travel to the Sewers and burn the blockage and travel to Ebony Barracks", parent=actThreeWidget)
    sewersTwo.move(0,375)
    ebonyWp = QLabel("<b>19a.</b> Grab the Ebony Barracks waypoint", parent=actThreeWidget)
    ebonyWp.move(0,390)
    ebony = QLabel("<b>20.</b> Find the Lunaris Temple", parent=actThreeWidget)
    ebony.move(0,405)
    lunaris = QLabel("<b>21.</b> Find the Lunaris Temple level 2", parent=actThreeWidget)
    lunaris.move(0,420)
    piety = QLabel("<b>22.</b> Find and kill Piety for the Tower Key", parent=actThreeWidget)
    piety.move(0,435)
    ebonyTwo = QLabel("<b>23.</b> Travel to the Ebony Barracks", parent=actThreeWidget)
    ebonyTwo.move(0,450)
    garden = QLabel("<b>24.</b> Find the Imperial Gardens", parent=actThreeWidget)
    garden.move(0,465)
    gardenTrial = QLabel("<b>24a.</b> Find and solve the trial of ascendancy", parent=actThreeWidget)
    gardenTrial.move(0,480)
    tower = QLabel("<b>25.</b> Find the Sceptre of God", parent=actThreeWidget)
    tower.move(0,495)
    lower = QLabel("<b>26.</b> Find the Upper Sceptre of God", parent=actThreeWidget)
    lower.move(0,510)
    upper = QLabel("<b>27.</b> Find Dominus", parent=actThreeWidget)
    upper.move(0,525)
    dominus = QLabel("<b>28.</b> Kill Dominus and travel to the Aqueducts", parent=actThreeWidget)
    dominus.move(0,540)
    actFourButton = QPushButton(actThreeWidget)
    actFourButton.setText("Act Four")
    actFourButton.move(0,560)
    mainMenuButton = QPushButton(actThreeWidget)
    mainMenuButton.setText("Main Menu")
    mainMenuButton.move(100,560)
    mainMenuButton.clicked.connect(mainMenuSwitch)
    actFourButton.clicked.connect(actFourSwitch)
    
#Create and fill the act four widget
class actFourMenu(QMainWindow):
    actFourWidget.setWindowTitle("Poe quest GUI")
    actFourWidget.setGeometry(0, 0, 800, 600)
    title = QLabel("<b>Act Four</b>", parent=actFourWidget)
    aqueduct = QLabel("<b>01.</b> Find Highgate", parent=actFourWidget)
    aqueduct.move(0,15)
    highgate = QLabel("<b>02.</b> Find The Dried Lake", parent=actFourWidget)
    highgate.move(0,30)
    dried = QLabel("<b>03.</b> Find Deshret's Banner", parent=actFourWidget)
    dried.move(0,45)
    mines = QLabel("<b>04.</b> Head to Highgate and open the Mines", parent=actFourWidget)
    mines.move(0,60)
    minesOne = QLabel("<b>05.</b> Find The Mines Level 2", parent=actFourWidget)
    minesOne.move(0,75)
    spirit = QLabel("<b>05a.</b> Free Deshret", parent=actFourWidget)
    spirit.move(0,90)
    minesTwo = QLabel("<b>06.</b> Find The Crystal Veins", parent=actFourWidget)
    minesTwo.move(0,105)
    crystal = QLabel("<b>07.</b> Find Dialla and head in Daresso's Dream", parent=actFourWidget)
    crystal.move(0,120)
    crystalWaypoint = QLabel("<b>07a.</b> Grab the Crystal Veins waypoint", parent=actFourWidget)
    crystalWaypoint.move(0,135)
    daresso = QLabel("<b>08.</b> Find The Grand Arena", parent=actFourWidget)
    daresso.move(0,150)
    arena = QLabel("<b>09.</b> Find the Ring of Blades and kill Daresso to collect the Eye of Desire", parent=actFourWidget)
    arena.move(0,165)
    kaom = QLabel("<b>10.</b> Head to Crystal Veins and to Kaom's Dream", parent=actFourWidget)
    kaom.move(0,180)
    kaomDream = QLabel("<b>11.</b> Find Kaom's Stronghold", parent=actFourWidget)
    kaomDream.move(0,195)
    stronghold = QLabel("<b>12.</b> Find Kaom and kill to collect the Eye of Fury", parent=actFourWidget)
    stronghold.move(0,210)
    dialla = QLabel("<b>13.</b> Head to Crystal Veins and talk to Dialla to open the Belly of the Beast", parent=actFourWidget)
    dialla.move(0,225)
    bellyOne = QLabel("<b>14.</b> Find the Belly of the Beast Level 2", parent=actFourWidget)
    bellyOne.move(0,240)
    bellyTwo = QLabel("<b>15.</b> Find and kill Piety", parent=actFourWidget)
    bellyTwo.move(0,255)
    harvest = QLabel("<b>16.</b> Proceed to the Harvest", parent=actFourWidget)
    harvest.move(0,270)
    harvestWaypoint = QLabel("<b>16a.</b> Grab the Harvest waypoint", parent=actFourWidget)
    harvestWaypoint.move(0,285)
    organs = QLabel("<b>17.</b> Collect Malachais organs", parent=actFourWidget)
    organs.move(0,300)
    core = QLabel("<b>18.</b> Enter the Black Core and kill Malachai", parent=actFourWidget)
    core.move(0,315)
    ascent = QLabel("<b>19.</b> Head to Highgate and travel to the Ascent", parent=actFourWidget)
    ascent.move(0,330)
    mainMenu = QPushButton(actFourWidget)
    mainMenu.setText("Main Menu")
    mainMenu.move(0,350)
    mainMenu.clicked.connect(mainMenuSwitch)
    actFive = QPushButton(actFourWidget)
    actFive.setText("Act Five")
    actFive.move(100,350)
    actFive.clicked.connect(actFiveSwitch)
    
#Create and fill the act five widget
class actFiveMenu(QMainWindow):
    actFiveWidget.setWindowTitle("Poe quest GUI")
    actFiveWidget.setGeometry(0, 0, 800, 600)
    title = QLabel("<b>Act Five</b>", parent=actFiveWidget)
    ascent = QLabel("<b>01.</b> Find the switch to Oriath and take the portal", parent=actFiveWidget)
    ascent.move(0,15)
    pens = QLabel("<b>02.</b> Find and kill Overseer Krow then go to Overseer's Tower", parent=actFiveWidget)
    pens.move(0,30)
    oblock = QLabel("<b>03.</b> Find and kill the Justicar then head to The Templar Courts", parent=actFiveWidget)
    oblock.move(0,45)
    miasmeter = QLabel("<b>03a.</b> Find the Miasmeter", parent=actFiveWidget)
    miasmeter.move(0,60)
    templarCourts = QLabel("<b>04.</b> Find The Chamber of Innocence", parent=actFiveWidget)
    templarCourts.move(0,75)
    chamber = QLabel("<b>05.</b> Find the Sanctum of Innocence", parent=actFiveWidget)
    chamber.move(0,90)
    sanctum = QLabel("<b>06.</b> Find and kill Avarius", parent=actFiveWidget)
    sanctum.move(0,105)
    torched = QLabel("<b>07.</b> Head to the Torched Courts", parent=actFiveWidget)
    torched.move(0,120)
    torchedCourts = QLabel("<b>08.</b> Find The Ruined Square", parent=actFiveWidget)
    torchedCourts.move(0,135)
    waypoint = QLabel("<b>08a.</b> Find the waypoint to The Ruined Square", parent=actFiveWidget)
    waypoint.move(0,150)
    ossuary = QLabel("<b>09.</b> Find The Ossuary", parent=actFiveWidget)
    ossuary.move(0,165)
    insideOssuary = QLabel("<b>10.</b> Find and take the Sign of Purity then head back to The Ruined Square", parent=actFiveWidget)
    insideOssuary.move(0,180)
    reliquary = QLabel("<b>10a.</b> Find the Reliquary and collect Kitava's torments", parent=actFiveWidget)
    reliquary.move(0,195)
    square = QLabel("<b>11.</b> Find the Cathedral Rooftop", parent=actFiveWidget)
    square.move(0,210)
    rooftop = QLabel("<b>10.</b> Find the Cathedral Apex and kill Kitava", parent=actFiveWidget)
    rooftop.move(0,225)
    dock = QLabel("<b>11.</b> Find Lily and sail to Wraeclast", parent=actFiveWidget)
    dock.move(0,240)
    mainMenu = QPushButton(actFiveWidget)
    mainMenu.setText("Main Menu")
    mainMenu.move(0,260)
    mainMenu.clicked.connect(mainMenuSwitch)
    actSix = QPushButton(actFiveWidget)
    actSix.setText("Act Six")
    actSix.move(100,260)
    actSix.clicked.connect(actSixSwitch)
    
#Create and fill the act six widget
class actSixMenu(QMainWindow):
    actSixWidget.setWindowTitle("Poe quest GUI")
    actSixWidget.setGeometry(0, 0, 800, 600)
    title = QLabel("<b>Act Six</b>", parent=actSixWidget)
    coast = QLabel("<b>01.</b> Head to The Coast and find The Mud Flats", parent=actSixWidget)
    coast.move(0,15)
    flats = QLabel("<b>02.</b> Find and kill The Dishonoured Queen and take the Eye of Conquest", parent=actSixWidget)
    flats.move(0,30)
    flatsTwo = QLabel("<b>03.</b> Use the Eye of Conquest to open the Karui Fortress", parent=actSixWidget)
    flatsTwo.move(0,45)
    #skill point, 60
    fortress = QLabel("<b>04.</b> Find the Ridge", parent=actSixWidget)
    fortress.move(0,75)
    ridge = QLabel("<b>05.</b> Find The Lower Prison", parent=actSixWidget)
    ridge.move(0,90)
    #trial, 105
    lower = QLabel("<b>06.</b> Find Shavronne's Tower", parent=actSixWidget)
    lower.move(0,120)
    tower = QLabel("<b>07.</b> Find the Prison Rooftop and kill Shavronne & Reassembled Brutus", parent=actSixWidget)
    tower.move(0,135)
    towerTwo = QLabel("<b>08.</b> Head to the Warden's Chambers then Prisoner's Gate", parent=actSixWidget)
    towerTwo.move(0,150)
    #skill point, 165
    gate = QLabel("<b>09.</b> Find The Western Forest", parent=actSixWidget)
    gate.move(0,180)
    western = QLabel("<b>10.</b> Find the Riverways", parent=actSixWidget)
    western.move(0,195)
    riverwaysWp = QLabel("<b>10a.</b> Find the Riverways Waypoint", parent=actSixWidget)
    riverwaysWp.move(0,210)
    #wetlands travel for skill point, 225
    #find grounds and kill boss, 240
    riverways = QLabel("<b>11.</b> Find the Southern Forest", parent=actSixWidget)
    riverways.move(0,255)
    southern = QLabel("<b>12.</b> Find the Cavern of Anger", parent=actSixWidget)
    southern.move(0,270)
    cavern = QLabel("<b>13.</b> Take the Black Flag and find The Beacon", parent=actSixWidget)
    cavern.move(0,285)
    beacon = QLabel("<b>14.</b> Light the Beacon and throw in the Black Flag", parent=actSixWidget)
    beacon.move(0,300)
    beaconTwo = QLabel("<b>15.</b> Talk to Waylam Roth and sail to The Brine King's Reef", parent=actSixWidget)
    beaconTwo.move(0,315)
    reef = QLabel("<b>16.</b> Find the Brine King's Throne and kill the Brine King", parent=actSixWidget)
    reef.move(0,330)
    reefTwo = QLabel("<b>17.</b> Sail to The Bridge Encampment", parent=actSixWidget)
    reefTwo.move(0,345)
    
window.addWidget(mainMenuWidget)
window.addWidget(actOneWidget)
window.addWidget(actTwoWidget)
window.addWidget(actThreeWidget)
window.addWidget(actFourWidget)
window.addWidget(actFiveWidget)
window.addWidget(actSixWidget)
window.setCurrentWidget(mainMenuWidget)
#Show the window
sys.exit(app.exec())