# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/testPreview.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testPreviewFrame(object):
    def setupUi(self, testPreviewFrame):
        testPreviewFrame.setObjectName("testPreviewFrame")
        testPreviewFrame.resize(1241, 662)
        self.gridLayout = QtWidgets.QGridLayout(testPreviewFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.taskArea = QtWidgets.QScrollArea(testPreviewFrame)
        self.taskArea.setMinimumSize(QtCore.QSize(500, 500))
        self.taskArea.setMaximumSize(QtCore.QSize(1500, 16777215))
        self.taskArea.setWidgetResizable(True)
        self.taskArea.setObjectName("taskArea")
        self.taskAreaContents = QtWidgets.QWidget()
        self.taskAreaContents.setGeometry(QtCore.QRect(0, 0, 498, 642))
        self.taskAreaContents.setObjectName("taskAreaContents")
        self.taskAreaLayout = QtWidgets.QVBoxLayout(self.taskAreaContents)
        self.taskAreaLayout.setObjectName("taskAreaLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.taskAreaLayout.addItem(spacerItem)
        self.taskArea.setWidget(self.taskAreaContents)
        self.gridLayout.addWidget(self.taskArea, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 5, 1, 1)
        self.leftFrame = QtWidgets.QFrame(testPreviewFrame)
        self.leftFrame.setMinimumSize(QtCore.QSize(400, 0))
        self.leftFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.leftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftFrame.setObjectName("leftFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.testNameLabel = QtWidgets.QLabel(self.leftFrame)
        self.testNameLabel.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.testNameLabel.setFont(font)
        self.testNameLabel.setObjectName("testNameLabel")
        self.verticalLayout.addWidget(self.testNameLabel)
        self.startButton = QtWidgets.QPushButton(self.leftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(100, 0))
        self.startButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.addToLibraryButton = QtWidgets.QPushButton(self.leftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addToLibraryButton.sizePolicy().hasHeightForWidth())
        self.addToLibraryButton.setSizePolicy(sizePolicy)
        self.addToLibraryButton.setMinimumSize(QtCore.QSize(200, 0))
        self.addToLibraryButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.addToLibraryButton.setObjectName("addToLibraryButton")
        self.verticalLayout.addWidget(self.addToLibraryButton)
        self.textBrowser = QtWidgets.QTextBrowser(self.leftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(200, 400))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        spacerItem3 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addWidget(self.leftFrame, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 6, 1, 1)

        self.retranslateUi(testPreviewFrame)
        QtCore.QMetaObject.connectSlotsByName(testPreviewFrame)

    def retranslateUi(self, testPreviewFrame):
        _translate = QtCore.QCoreApplication.translate
        testPreviewFrame.setWindowTitle(_translate("testPreviewFrame", "Frame"))
        self.testNameLabel.setText(_translate("testPreviewFrame", "Test Name"))
        self.startButton.setText(_translate("testPreviewFrame", "Start"))
        self.addToLibraryButton.setText(_translate("testPreviewFrame", "Add to my library"))
        self.textBrowser.setHtml(_translate("testPreviewFrame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Fira Sans Semi-Light\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Some sample description.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    testPreviewFrame = QtWidgets.QFrame()
    ui = Ui_testPreviewFrame()
    ui.setupUi(testPreviewFrame)
    testPreviewFrame.show()
    sys.exit(app.exec_())
