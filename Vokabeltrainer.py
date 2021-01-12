from Vokabellisten import vokabeldeutschspanischextern,vokabelspanischextern, vokabelenglischextern,vokabeldeutschenglischextern, vokabeldeutschfranz,vokabelfranzoesisch
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
import sys

class Ui_FirstWindow(object):


    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.resize(602, 324)
        self.centralwidget = QtWidgets.QWidget(FirstWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(65, 230, 90, 23))
        self.pushButton.setObjectName("ButtonSpanisch")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 230, 90, 23))
        self.pushButton_2.setObjectName("ButtonEnglisch")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 230, 90, 23))
        self.pushButton_3.setObjectName("ButtonFranzösisch")

        self.label_spanisch = QtWidgets.QLabel(self.centralwidget)
        self.label_spanisch.setGeometry(QtCore.QRect(40, 120, 140,80))
        self.label_spanisch.setText("")
        self.label_spanisch.setScaledContents(True)
        self.label_spanisch.setObjectName("label_spanisch")
        self.label_spanisch.setPixmap(QtGui.QPixmap("Spanien.jpg"))

        self.label_englisch = QtWidgets.QLabel(self.centralwidget)
        self.label_englisch.setGeometry(QtCore.QRect(230, 120, 140, 80))
        self.label_englisch.setText("")
        self.label_englisch.setScaledContents(True)
        self.label_englisch.setObjectName("label_englisch")
        self.label_englisch.setPixmap(QtGui.QPixmap("England.jpg"))

        self.label_französisch = QtWidgets.QLabel(self.centralwidget)
        self.label_französisch.setGeometry(QtCore.QRect(425, 120, 140, 80))
        self.label_französisch.setText("")
        self.label_französisch.setScaledContents(True)
        self.label_französisch.setObjectName("französisch")
        self.label_französisch.setPixmap(QtGui.QPixmap("Frankreich.jpg"))

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(192, 50, 220, 50))
        self.label_3.setFont(QFont('Arial', 10))
        self.label_3.setText("Welche Sprache möchtest du üben?")
        self.label_3.setObjectName("Frage")

        FirstWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FirstWindow)
        self.statusbar.setObjectName("statusbar")
        FirstWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "Vokabeltrainer"))
        self.pushButton.setText(_translate("Firstbutton", "Spanisch"))
        self.pushButton_2.setText(_translate("Secondbutton", "Englisch"))
        self.pushButton_3.setText(_translate("Thirdbutton", "Französisch"))

    def LoadSpanishwindow(self):
        Spanishwindow = QtWidgets.QFirstWindow()
        ui = Ui_Spanishwindow()
        ui.setupUi(Spanishwindow)
        Spanishwindow.show()



class Ui_Spanishwindow(object):

    def startbutton(self):
        randomvocesp = random.choice(vokabelspanischextern)
        index = vokabelspanischextern.index(randomvocesp)
        indexdeutsch = vokabeldeutschspanischextern[index]
        self.lineEdit.setText(randomvocesp)
        self.lineEdit_2.setText(indexdeutsch)
        self.lineEdit_2.setEchoMode(1)
        self.lineEdit_3.setFocus(1)


    def aufloesungsbutton(self):
        self.lineEdit_2.setEchoMode(0)
        self.lineEdit_3.clearFocus()
        self.pushButton2.setDefault(True)
        self.pushButton2.setFocus(1)

        if self.lineEdit_3.text():
            if self.lineEdit_3.text() in self.lineEdit_2.text().lower():
                self.labelrichtig.setHidden(0)
            elif self.lineEdit_3.text() in self.lineEdit_2.text():
                self.labelrichtig.setHidden(0)
            else:
                self.labelfalsch.setHidden(0)
        else:
            return

    def nextbutton(self):
        randomvocesp = random.choice(vokabelspanischextern)
        index = vokabelspanischextern.index(randomvocesp)
        indexdeutsch1 = vokabeldeutschspanischextern[index]
        self.lineEdit.setText(randomvocesp)
        self.lineEdit_2.setText(indexdeutsch1)
        self.lineEdit_2.setEchoMode(1)
        self.labelfalsch.setHidden(1)
        self.labelrichtig.setHidden(0)
        self.lineEdit_3.clear()
        self.lineEdit_3.setFocus(1)
        self.labelrichtig.setHidden(1)
        self.labelfalsch.setHidden(1)
        self.pushButton2.setDefault(False)

    def setupUi(self, Button1):
        Button1.setObjectName("Button1")
        Button1.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Button1)
        self.centralwidget.setObjectName("centralwidget")

        self.labelspanien = QtWidgets.QLabel(self.centralwidget)
        self.labelspanien.setGeometry(QtCore.QRect(100, 70, 271, 131))
        self.labelspanien.setText("")
        self.labelspanien.setPixmap(QtGui.QPixmap("Spanien.jpg"))
        self.labelspanien.setScaledContents(True)
        self.labelspanien.setObjectName("labelspanien")

        self.labeldeutschland = QtWidgets.QLabel(self.centralwidget)
        self.labeldeutschland.setGeometry(QtCore.QRect(440, 70, 271, 131))
        self.labeldeutschland.setText("")
        self.labeldeutschland.setPixmap(QtGui.QPixmap("Deutsch.jpg"))
        self.labeldeutschland.setScaledContents(True)
        self.labeldeutschland.setObjectName("labeldeutschland")

        self.labelrichtig = QtWidgets.QLabel(self.centralwidget)
        self.labelrichtig.setGeometry(QtCore.QRect(280, 420, 271, 131))
        self.labelrichtig.setText("")
        self.labelrichtig.setPixmap(QtGui.QPixmap("Richtig.jpg"))
        self.labelrichtig.setScaledContents(True)
        self.labelrichtig.setObjectName("labelrichtig")
        self.labelrichtig.setHidden(1)

        self.labelfalsch = QtWidgets.QLabel(self.centralwidget)
        self.labelfalsch.setGeometry(QtCore.QRect(280, 420, 271, 131))
        self.labelfalsch.setText("")
        self.labelfalsch.setPixmap(QtGui.QPixmap("Falsch.jpg"))
        self.labelfalsch.setScaledContents(True)
        self.labelfalsch.setObjectName("labelfalsch")
        self.labelfalsch.setHidden(1)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(102, 230, 271, 41))
        self.lineEdit.setObjectName("Vokabelspanisch")
        self.lineEdit.returnPressed.connect(self.aufloesungsbutton)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(442, 229, 271, 41))
        self.lineEdit_2.setObjectName("Vokabeldeutsch")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(102, 289, 271, 41))
        self.lineEdit_3.setObjectName("Inputfeld")
        self.lineEdit_3.setPlaceholderText("Übersetzung")
        self.lineEdit_3.returnPressed.connect(self.aufloesungsbutton)

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(100, 0, 610, 50))
        self.startButton.setObjectName("Startbutton")
        self.startButton.setText("Start")
        self.startButton.clicked.connect(self.startbutton)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 350, 120, 41))
        self.pushButton.setObjectName("Auflösungsbutton")
        self.pushButton.clicked.connect(self.aufloesungsbutton)

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(180, 350, 120, 41))
        self.pushButton2.setObjectName("Nextbutton")
        self.pushButton2.setText("Nächste")
        self.pushButton2.clicked.connect(self.nextbutton)

        Button1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Button1)
        self.statusbar.setObjectName("statusbar")
        Button1.setStatusBar(self.statusbar)

        self.retranslateUi(Button1)
        QtCore.QMetaObject.connectSlotsByName(Button1)

    def retranslateUi(self, Button1):
        _translate = QtCore.QCoreApplication.translate
        Button1.setWindowTitle(_translate("Button1", "Spanishwindow"))
        self.pushButton.setText(_translate("Button1", "Auflösung (Enter)"))






class Ui_EnglishWindow(object):

    def startbutton(self):
        randomvoceng = random.choice(vokabelenglischextern)
        indexeng = vokabelenglischextern.index(randomvoceng)
        indexdeutscheng = vokabeldeutschenglischextern[indexeng]
        self.lineEdit.setText(randomvoceng)
        self.lineEdit_2.setText(indexdeutscheng)
        self.lineEdit_2.setEchoMode(1)
        self.lineEdit_3.setFocus()


    def aufloesungsbutton(self):
        self.lineEdit_2.setEchoMode(0)
        self.lineEdit_3.clearFocus()
        self.pushButton2.setDefault(True)
        self.pushButton2.setFocus(1)

        if self.lineEdit_3.text():
            if self.lineEdit_3.text() in self.lineEdit_2.text().lower():
                self.labelrichtig.setHidden(0)
            elif self.lineEdit_3.text() in self.lineEdit_2.text():
                self.labelrichtig.setHidden(0)
            else:
                self.labelfalsch.setHidden(0)
        else:
            return

    def nextbutton(self):
        randomvoceng = random.choice(vokabelenglischextern)
        indexeng = vokabelenglischextern.index(randomvoceng)
        indexdeutscheng1 = vokabeldeutschenglischextern[indexeng]
        self.lineEdit.setText(randomvoceng)
        self.lineEdit_2.setText(indexdeutscheng1)
        self.lineEdit_2.setEchoMode(1)
        self.labelfalsch.setHidden(1)
        self.labelrichtig.setHidden(0)
        self.lineEdit_3.clear()
        self.lineEdit_3.setFocus(1)
        self.labelrichtig.setHidden(1)
        self.labelfalsch.setHidden(1)
        self.pushButton2.setDefault(False)

    def setupUi(self, Button1):
        Button1.setObjectName("Button1")
        Button1.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Button1)
        self.centralwidget.setObjectName("centralwidget")

        self.labelengland = QtWidgets.QLabel(self.centralwidget)
        self.labelengland.setGeometry(QtCore.QRect(100, 70, 271, 131))
        self.labelengland.setText("")
        self.labelengland.setPixmap(QtGui.QPixmap("England.jpg"))
        self.labelengland.setScaledContents(True)
        self.labelengland.setObjectName("labelengland")

        self.labeldeutschland = QtWidgets.QLabel(self.centralwidget)
        self.labeldeutschland.setGeometry(QtCore.QRect(440, 70, 271, 131))
        self.labeldeutschland.setText("")
        self.labeldeutschland.setPixmap(QtGui.QPixmap("Deutsch.jpg"))
        self.labeldeutschland.setScaledContents(True)
        self.labeldeutschland.setObjectName("labeldeutschland")

        self.labelrichtig = QtWidgets.QLabel(self.centralwidget)
        self.labelrichtig.setGeometry(QtCore.QRect(280, 420, 271, 131))
        self.labelrichtig.setText("")
        self.labelrichtig.setPixmap(QtGui.QPixmap("Richtig.jpg"))
        self.labelrichtig.setScaledContents(True)
        self.labelrichtig.setObjectName("labelrichtig")
        self.labelrichtig.setHidden(1)

        self.labelfalsch = QtWidgets.QLabel(self.centralwidget)
        self.labelfalsch.setGeometry(QtCore.QRect(280, 420, 271, 131))
        self.labelfalsch.setText("")
        self.labelfalsch.setPixmap(QtGui.QPixmap("Falsch.jpg"))
        self.labelfalsch.setScaledContents(True)
        self.labelfalsch.setObjectName("labelfalsch")
        self.labelfalsch.setHidden(1)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(102, 230, 271, 41))
        self.lineEdit.setObjectName("Vokabelenglisch")
        self.lineEdit.returnPressed.connect(self.aufloesungsbutton)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(442, 229, 271, 41))
        self.lineEdit_2.setObjectName("Vokabeldeutsch")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(102, 289, 271, 41))
        self.lineEdit_3.setObjectName("Inputfeld")
        self.lineEdit_3.setPlaceholderText("Übersetzung")
        self.lineEdit_3.returnPressed.connect(self.aufloesungsbutton)

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(100, 0, 610, 50))
        self.startButton.setObjectName("Startbutton")
        self.startButton.setText("Start")
        self.startButton.clicked.connect(self.startbutton)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 350, 120, 41))
        self.pushButton.setObjectName("Auflösungsbutton")
        self.pushButton.clicked.connect(self.aufloesungsbutton)

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(180, 350, 120, 41))
        self.pushButton2.setObjectName("Nextbutton (space)")
        self.pushButton2.setText("Next")
        self.pushButton2.clicked.connect(self.nextbutton)

        Button1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Button1)
        self.statusbar.setObjectName("statusbar")
        Button1.setStatusBar(self.statusbar)

        self.retranslateUi(Button1)
        QtCore.QMetaObject.connectSlotsByName(Button1)

    def retranslateUi(self, Button1):
        _translate = QtCore.QCoreApplication.translate
        Button1.setWindowTitle(_translate("Button1", "EnglishWindow"))
        self.pushButton.setText(_translate("Button1", "Auflösung (Enter)"))



class Ui_frenchWindow(object):

    def startbutton(self):
        randomvocfr = random.choice(vokabelfranzoesisch)
        indexfr = vokabelfranzoesisch.index(randomvocfr)
        indexdeutschfr = vokabeldeutschfranz[indexfr]
        self.lineEdit.setText(randomvocfr)
        self.lineEdit_2.setText(indexdeutschfr)
        self.lineEdit_2.setEchoMode(1)
        self.lineEdit_3.setFocus()


    def aufloesungsbutton(self):
        self.lineEdit_2.setEchoMode(0)
        self.lineEdit_3.clearFocus()
        self.pushButton2.setDefault(True)
        self.pushButton2.setFocus(1)

        if self.lineEdit_3.text():
            if self.lineEdit_3.text() in self.lineEdit_2.text().lower():
                self.labelrichtig.setHidden(0)
            elif self.lineEdit_3.text() in self.lineEdit_2.text():
                self.labelrichtig.setHidden(0)
            else:
                self.labelfalsch.setHidden(0)
        else:
            return

    def nextbutton(self):
        randomvocfr = random.choice(vokabelfranzoesisch)
        indexfr = vokabelfranzoesisch.index(randomvocfr)
        indexdeutschfr1 = vokabeldeutschfranz[indexfr]
        self.lineEdit.setText(randomvocfr)
        self.lineEdit_2.setText(indexdeutschfr1)
        self.lineEdit_2.setEchoMode(1)
        self.labelfalsch.setHidden(1)
        self.labelrichtig.setHidden(0)
        self.lineEdit_3.clear()
        self.lineEdit_3.setFocus(1)
        self.labelrichtig.setHidden(1)
        self.labelfalsch.setHidden(1)
        self.pushButton2.setDefault(False)

    def setupUi(self, Button1):
        Button1.setObjectName("Button1")
        Button1.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Button1)
        self.centralwidget.setObjectName("centralwidget")

        self.labelengland = QtWidgets.QLabel(self.centralwidget)
        self.labelengland.setGeometry(QtCore.QRect(100, 70, 271, 131))
        self.labelengland.setText("")
        self.labelengland.setPixmap(QtGui.QPixmap("Frankreich.jpg"))
        self.labelengland.setScaledContents(True)
        self.labelengland.setObjectName("labelfrankreich")

        self.labeldeutschland = QtWidgets.QLabel(self.centralwidget)
        self.labeldeutschland.setGeometry(QtCore.QRect(440, 70, 271, 131))
        self.labeldeutschland.setText("")
        self.labeldeutschland.setPixmap(QtGui.QPixmap("Deutsch.jpg"))
        self.labeldeutschland.setScaledContents(True)
        self.labeldeutschland.setObjectName("labeldeutschland")

        self.labelrichtig = QtWidgets.QLabel(self.centralwidget)
        self.labelrichtig.setGeometry(QtCore.QRect(280, 420, 271, 131))
        self.labelrichtig.setText("")
        self.labelrichtig.setPixmap(QtGui.QPixmap("Richtig.jpg"))
        self.labelrichtig.setScaledContents(True)
        self.labelrichtig.setObjectName("labelrichtig")
        self.labelrichtig.setHidden(1)

        self.labelfalsch = QtWidgets.QLabel(self.centralwidget)
        self.labelfalsch.setGeometry(QtCore.QRect(280, 420, 271, 131))
        self.labelfalsch.setText("")
        self.labelfalsch.setPixmap(QtGui.QPixmap("Falsch.jpg"))
        self.labelfalsch.setScaledContents(True)
        self.labelfalsch.setObjectName("labelfalsch")
        self.labelfalsch.setHidden(1)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(102, 230, 271, 41))
        self.lineEdit.setObjectName("Vokabelfranz")
        self.lineEdit.returnPressed.connect(self.aufloesungsbutton)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(442, 229, 271, 41))
        self.lineEdit_2.setObjectName("Vokabeldeutsch")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(102, 289, 271, 41))
        self.lineEdit_3.setObjectName("Inputfeld")
        self.lineEdit_3.setPlaceholderText("Übersetzung")
        self.lineEdit_3.returnPressed.connect(self.aufloesungsbutton)

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(100, 0, 610, 50))
        self.startButton.setObjectName("Startbutton")
        self.startButton.setText("Start")
        self.startButton.clicked.connect(self.startbutton)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 350, 120, 41))
        self.pushButton.setObjectName("Auflösungsbutton")
        self.pushButton.clicked.connect(self.aufloesungsbutton)

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(180, 350, 120, 41))
        self.pushButton2.setObjectName("Nextbutton (space)")
        self.pushButton2.setText("Nächste")
        self.pushButton2.clicked.connect(self.nextbutton)

        Button1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Button1)
        self.statusbar.setObjectName("statusbar")
        Button1.setStatusBar(self.statusbar)

        self.retranslateUi(Button1)
        QtCore.QMetaObject.connectSlotsByName(Button1)

    def retranslateUi(self, Button1):
        _translate = QtCore.QCoreApplication.translate
        Button1.setWindowTitle(_translate("Button1", "FrenchhWindow"))
        self.pushButton.setText(_translate("Button1", "Lösung (Enter)"))



class Controller:

    def __init__(self):
        pass

    def Show_FirstWindow(self):
        self.FirstWindow = QtWidgets.QMainWindow()
        self.ui = Ui_FirstWindow()
        self.ui.setupUi(self.FirstWindow)
        self.ui.pushButton.clicked.connect(self.Show_Spanishwindow)
        self.ui.pushButton.clicked.connect(self.FirstWindow.close)
        self.ui.pushButton_2.clicked.connect(self.FirstWindow.close)
        self.ui.pushButton_2.clicked.connect(self.Show_EnglishWindow)
        self.ui.pushButton_3.clicked.connect(self.FirstWindow.close)
        self.ui.pushButton_3.clicked.connect(self.Show_FrenchWindow)
        self.FirstWindow.show()



    def Show_Spanishwindow(self):
        self.Spanishwindow = QtWidgets.QMainWindow()
        self.ui = Ui_Spanishwindow()
        self.ui.setupUi(self.Spanishwindow)

        self.Spanishwindow.show()

    def Show_EnglishWindow(self):
        self.Englishwindow = QtWidgets.QMainWindow()
        self.ui = Ui_EnglishWindow()
        self.ui.setupUi(self.Englishwindow)

        self.Englishwindow.show()

    def Show_FrenchWindow(self):
        self.frenchwindow = QtWidgets.QMainWindow()
        self.ui = Ui_frenchWindow()
        self.ui.setupUi(self.frenchwindow)

        self.frenchwindow.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.Show_FirstWindow()
    sys.exit(app.exec_())