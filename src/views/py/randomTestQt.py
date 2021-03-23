# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/randomTest.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_randomTestFrame(object):
    def setupUi(self, randomTestFrame):
        randomTestFrame.setObjectName("randomTestFrame")
        randomTestFrame.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(randomTestFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(randomTestFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.taskFrame = QtWidgets.QFrame(randomTestFrame)
        self.taskFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.taskFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.taskFrame.setObjectName("taskFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.taskFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addWidget(self.taskFrame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(randomTestFrame)
        QtCore.QMetaObject.connectSlotsByName(randomTestFrame)

    def retranslateUi(self, randomTestFrame):
        _translate = QtCore.QCoreApplication.translate
        randomTestFrame.setWindowTitle(_translate("randomTestFrame", "Frame"))
        self.titleLabel.setText(_translate("randomTestFrame", "Random Test"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    randomTestFrame = QtWidgets.QFrame()
    ui = Ui_randomTestFrame()
    ui.setupUi(randomTestFrame)
    randomTestFrame.show()
    sys.exit(app.exec_())
