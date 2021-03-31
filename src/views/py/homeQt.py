# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/home.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainFrame(object):
    def setupUi(self, mainFrame):
        mainFrame.setObjectName("mainFrame")
        mainFrame.resize(1147, 874)
        mainFrame.setStyleSheet("background-color: rgb(255, 255, 242);\n"
"border-color: rgb(255, 255, 242);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(mainFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(mainFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.myLibraryLabel = QtWidgets.QLabel(self.frame)
        self.myLibraryLabel.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(36)
        self.myLibraryLabel.setFont(font)
        self.myLibraryLabel.setObjectName("myLibraryLabel")
        self.verticalLayout.addWidget(self.myLibraryLabel)
        self.testScrollArea = QtWidgets.QScrollArea(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testScrollArea.sizePolicy().hasHeightForWidth())
        self.testScrollArea.setSizePolicy(sizePolicy)
        self.testScrollArea.setMinimumSize(QtCore.QSize(0, 500))
        self.testScrollArea.setMaximumSize(QtCore.QSize(1500, 16777215))
        self.testScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.testScrollArea.setWidgetResizable(True)
        self.testScrollArea.setObjectName("testScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 298, 682))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.testsAreaContents = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.testsAreaContents.setObjectName("testsAreaContents")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.testsAreaContents.addItem(spacerItem1)
        self.testScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.testScrollArea)
        self.horizontalLayout.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.decor = QtWidgets.QLabel(mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decor.sizePolicy().hasHeightForWidth())
        self.decor.setSizePolicy(sizePolicy)
        self.decor.setMinimumSize(QtCore.QSize(0, 0))
        self.decor.setText("")
        self.decor.setPixmap(QtGui.QPixmap("../res/decor.png"))
        self.decor.setScaledContents(True)
        self.decor.setObjectName("decor")
        self.horizontalLayout.addWidget(self.decor)

        self.retranslateUi(mainFrame)
        QtCore.QMetaObject.connectSlotsByName(mainFrame)

    def retranslateUi(self, mainFrame):
        _translate = QtCore.QCoreApplication.translate
        mainFrame.setWindowTitle(_translate("mainFrame", "Frame"))
        self.myLibraryLabel.setText(_translate("mainFrame", "Main Library"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = QtWidgets.QFrame()
    ui = Ui_mainFrame()
    ui.setupUi(mainFrame)
    mainFrame.show()
    sys.exit(app.exec_())
