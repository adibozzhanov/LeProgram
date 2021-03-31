# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1076, 119)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 119))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../../res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 242);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setKerning(True)
        self.centralwidget.setFont(font)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setMinimumSize(QtCore.QSize(0, 700))
        self.mainFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mainFrame.setLineWidth(0)
        self.mainFrame.setObjectName("mainFrame")
        self.mainFrameLayout = QtWidgets.QHBoxLayout(self.mainFrame)
        self.mainFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrameLayout.setSpacing(0)
        self.mainFrameLayout.setObjectName("mainFrameLayout")
        self.gridLayout.addWidget(self.mainFrame, 1, 0, 1, 1)
        self.menuBar = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBar.sizePolicy().hasHeightForWidth())
        self.menuBar.setSizePolicy(sizePolicy)
        self.menuBar.setMinimumSize(QtCore.QSize(0, 0))
        self.menuBar.setMaximumSize(QtCore.QSize(16777215, 150))
        self.menuBar.setStyleSheet("background-color: rgb(23, 161, 145);")
        self.menuBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuBar.setObjectName("menuBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.menuBar)
        self.horizontalLayout.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.logo = QtWidgets.QLabel(self.menuBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(48, 75))
        self.logo.setMaximumSize(QtCore.QSize(48, 75))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("ui/../../res/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.menuBar)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.homeButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy)
        self.homeButton.setMinimumSize(QtCore.QSize(120, 50))
        self.homeButton.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(False)
        self.homeButton.setFont(font)
        self.homeButton.setAutoFillBackground(False)
        self.homeButton.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(246, 247, 200);\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.homeButton.setIcon(icon1)
        self.homeButton.setIconSize(QtCore.QSize(24, 24))
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout_2.addWidget(self.homeButton)
        self.askLepButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.askLepButton.sizePolicy().hasHeightForWidth())
        self.askLepButton.setSizePolicy(sizePolicy)
        self.askLepButton.setMinimumSize(QtCore.QSize(130, 50))
        self.askLepButton.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.askLepButton.setFont(font)
        self.askLepButton.setAutoFillBackground(False)
        self.askLepButton.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);\n"
"selection-color:rgb(233, 234, 189);\n"
"selection-background-color: rgb(233, 234, 189);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/ask lep.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.askLepButton.setIcon(icon2)
        self.askLepButton.setIconSize(QtCore.QSize(24, 24))
        self.askLepButton.setObjectName("askLepButton")
        self.horizontalLayout_2.addWidget(self.askLepButton)
        self.randomQsButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.randomQsButton.sizePolicy().hasHeightForWidth())
        self.randomQsButton.setSizePolicy(sizePolicy)
        self.randomQsButton.setMinimumSize(QtCore.QSize(180, 50))
        self.randomQsButton.setMaximumSize(QtCore.QSize(180, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.randomQsButton.setFont(font)
        self.randomQsButton.setAutoFillBackground(False)
        self.randomQsButton.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);\n"
"selection-color:rgb(233, 234, 189);\n"
"selection-background-color: rgb(233, 234, 189);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/random q.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.randomQsButton.setIcon(icon3)
        self.randomQsButton.setIconSize(QtCore.QSize(24, 24))
        self.randomQsButton.setObjectName("randomQsButton")
        self.horizontalLayout_2.addWidget(self.randomQsButton)
        self.newTestButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newTestButton.sizePolicy().hasHeightForWidth())
        self.newTestButton.setSizePolicy(sizePolicy)
        self.newTestButton.setMinimumSize(QtCore.QSize(140, 50))
        self.newTestButton.setMaximumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.newTestButton.setFont(font)
        self.newTestButton.setAutoFillBackground(False)
        self.newTestButton.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);\n"
"selection-color:rgb(233, 234, 189);\n"
"selection-background-color: rgb(233, 234, 189);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/new test.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/new test.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/new test.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/new test.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/new test.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/new test.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/new test.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/new test.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.newTestButton.setIcon(icon4)
        self.newTestButton.setIconSize(QtCore.QSize(24, 24))
        self.newTestButton.setObjectName("newTestButton")
        self.horizontalLayout_2.addWidget(self.newTestButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.frame)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.userButton = QtWidgets.QPushButton(self.menuBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userButton.sizePolicy().hasHeightForWidth())
        self.userButton.setSizePolicy(sizePolicy)
        self.userButton.setMinimumSize(QtCore.QSize(140, 50))
        self.userButton.setMaximumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.userButton.setFont(font)
        self.userButton.setAutoFillBackground(False)
        self.userButton.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);\n"
"selection-color:rgb(233, 234, 189);\n"
"selection-background-color: rgb(233, 234, 189);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui/../../res/ui icons/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userButton.setIcon(icon5)
        self.userButton.setIconSize(QtCore.QSize(24, 24))
        self.userButton.setObjectName("userButton")
        self.horizontalLayout.addWidget(self.userButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addWidget(self.menuBar, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Leprogram"))
        self.homeButton.setText(_translate("MainWindow", "Home"))
        self.askLepButton.setText(_translate("MainWindow", "Ask LeP"))
        self.randomQsButton.setText(_translate("MainWindow", "Random Q\'s"))
        self.newTestButton.setText(_translate("MainWindow", "New Test"))
        self.userButton.setText(_translate("MainWindow", "User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
