# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/randomTaking.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_randomTakingFrame(object):
    def setupUi(self, randomTakingFrame):
        randomTakingFrame.setObjectName("randomTakingFrame")
        randomTakingFrame.resize(656, 561)
        randomTakingFrame.setStyleSheet("background-color: rgb(255, 255, 242);")
        randomTakingFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.horizontalLayout = QtWidgets.QHBoxLayout(randomTakingFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(randomTakingFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.testNameLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(20)
        font.setItalic(True)
        self.testNameLabel.setFont(font)
        self.testNameLabel.setObjectName("testNameLabel")
        self.verticalLayout_2.addWidget(self.testNameLabel)
        self.scoreLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scoreLabel.sizePolicy().hasHeightForWidth())
        self.scoreLabel.setSizePolicy(sizePolicy)
        self.scoreLabel.setObjectName("scoreLabel")
        self.verticalLayout_2.addWidget(self.scoreLabel)
        self.taskFrame = QtWidgets.QFrame(self.frame)
        self.taskFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.taskFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.taskFrame.setObjectName("taskFrame")
        self.taskLayout = QtWidgets.QHBoxLayout(self.taskFrame)
        self.taskLayout.setContentsMargins(0, 0, 0, 0)
        self.taskLayout.setSpacing(0)
        self.taskLayout.setObjectName("taskLayout")
        self.verticalLayout_2.addWidget(self.taskFrame)
        self.nextQButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setItalic(False)
        self.nextQButton.setFont(font)
        self.nextQButton.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(246, 247, 200);\n"
"")
        self.nextQButton.setObjectName("nextQButton")
        self.verticalLayout_2.addWidget(self.nextQButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.frame)
        self.askLepFrame = QtWidgets.QFrame(randomTakingFrame)
        self.askLepFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.askLepFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.askLepFrame.setObjectName("askLepFrame")
        self.askLepLayout = QtWidgets.QHBoxLayout(self.askLepFrame)
        self.askLepLayout.setContentsMargins(0, 0, 0, 0)
        self.askLepLayout.setSpacing(0)
        self.askLepLayout.setObjectName("askLepLayout")
        self.horizontalLayout.addWidget(self.askLepFrame)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        self.retranslateUi(randomTakingFrame)
        QtCore.QMetaObject.connectSlotsByName(randomTakingFrame)

    def retranslateUi(self, randomTakingFrame):
        _translate = QtCore.QCoreApplication.translate
        randomTakingFrame.setWindowTitle(_translate("randomTakingFrame", "Frame"))
        self.testNameLabel.setText(_translate("randomTakingFrame", "Random Question!"))
        self.scoreLabel.setText(_translate("randomTakingFrame", "Score:"))
        self.nextQButton.setText(_translate("randomTakingFrame", "Next Question"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    randomTakingFrame = QtWidgets.QFrame()
    ui = Ui_randomTakingFrame()
    ui.setupUi(randomTakingFrame)
    randomTakingFrame.show()
    sys.exit(app.exec_())
