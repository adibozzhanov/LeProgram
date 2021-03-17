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
        testPreviewFrame.resize(807, 599)
        self.gridLayout = QtWidgets.QGridLayout(testPreviewFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.leftFrame = QtWidgets.QFrame(testPreviewFrame)
        self.leftFrame.setMinimumSize(QtCore.QSize(220, 0))
        self.leftFrame.setMaximumSize(QtCore.QSize(220, 16777215))
        self.leftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftFrame.setObjectName("leftFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.testNameLabel = QtWidgets.QLabel(self.leftFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.testNameLabel.setFont(font)
        self.testNameLabel.setObjectName("testNameLabel")
        self.verticalLayout.addWidget(self.testNameLabel)
        self.startButton = QtWidgets.QPushButton(self.leftFrame)
        self.startButton.setMinimumSize(QtCore.QSize(50, 0))
        self.startButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.addToLibraryButton = QtWidgets.QPushButton(self.leftFrame)
        self.addToLibraryButton.setMinimumSize(QtCore.QSize(150, 0))
        self.addToLibraryButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.addToLibraryButton.setObjectName("addToLibraryButton")
        self.verticalLayout.addWidget(self.addToLibraryButton)
        self.textBrowser = QtWidgets.QTextBrowser(self.leftFrame)
        self.textBrowser.setMinimumSize(QtCore.QSize(200, 400))
        self.textBrowser.setMaximumSize(QtCore.QSize(200, 400))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.leftFrame, 0, 0, 1, 1)
        self.taskArea = QtWidgets.QScrollArea(testPreviewFrame)
        self.taskArea.setMinimumSize(QtCore.QSize(500, 500))
        self.taskArea.setWidgetResizable(True)
        self.taskArea.setObjectName("taskArea")
        self.taskAreaContents = QtWidgets.QWidget()
        self.taskAreaContents.setGeometry(QtCore.QRect(0, 0, 561, 579))
        self.taskAreaContents.setObjectName("taskAreaContents")
        self.taskAreaLayout = QtWidgets.QVBoxLayout(self.taskAreaContents)
        self.taskAreaLayout.setObjectName("taskAreaLayout")
        self.taskArea.setWidget(self.taskAreaContents)
        self.gridLayout.addWidget(self.taskArea, 0, 1, 1, 1)

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
