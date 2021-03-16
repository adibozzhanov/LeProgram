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
        mainFrame.resize(777, 664)
        self.gridLayout = QtWidgets.QGridLayout(mainFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.testsAndScrollbarFrame = QtWidgets.QFrame(mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testsAndScrollbarFrame.sizePolicy().hasHeightForWidth())
        self.testsAndScrollbarFrame.setSizePolicy(sizePolicy)
        self.testsAndScrollbarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.testsAndScrollbarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testsAndScrollbarFrame.setObjectName("testsAndScrollbarFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.testsAndScrollbarFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.testScrollArea = QtWidgets.QScrollArea(self.testsAndScrollbarFrame)
        self.testScrollArea.setWidgetResizable(True)
        self.testScrollArea.setObjectName("testScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 463, 585))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.testsAreaContents = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.testsAreaContents.setObjectName("testsAreaContents")
        self.testScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.testScrollArea)
        self.gridLayout.addWidget(self.testsAndScrollbarFrame, 1, 1, 1, 1)
        self.myLibraryLabel = QtWidgets.QLabel(mainFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.myLibraryLabel.setFont(font)
        self.myLibraryLabel.setObjectName("myLibraryLabel")
        self.gridLayout.addWidget(self.myLibraryLabel, 0, 0, 1, 1)
        self.searchAndTagsFrame = QtWidgets.QFrame(mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchAndTagsFrame.sizePolicy().hasHeightForWidth())
        self.searchAndTagsFrame.setSizePolicy(sizePolicy)
        self.searchAndTagsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchAndTagsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchAndTagsFrame.setObjectName("searchAndTagsFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.searchAndTagsFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.searchFrame = QtWidgets.QFrame(self.searchAndTagsFrame)
        self.searchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchFrame.setObjectName("searchFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.searchFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchButton = QtWidgets.QPushButton(self.searchFrame)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.searchLineEdit = QtWidgets.QLineEdit(self.searchFrame)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout_2.addWidget(self.searchLineEdit)
        self.verticalLayout_2.addWidget(self.searchFrame)
        self.tagsAndScrollbarFrame = QtWidgets.QFrame(self.searchAndTagsFrame)
        self.tagsAndScrollbarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tagsAndScrollbarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tagsAndScrollbarFrame.setObjectName("tagsAndScrollbarFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tagsAndScrollbarFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tagsFrame = QtWidgets.QFrame(self.tagsAndScrollbarFrame)
        self.tagsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tagsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tagsFrame.setObjectName("tagsFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tagsFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3.addWidget(self.tagsFrame)
        self.tagsScrollbar = QtWidgets.QScrollBar(self.tagsAndScrollbarFrame)
        self.tagsScrollbar.setOrientation(QtCore.Qt.Vertical)
        self.tagsScrollbar.setObjectName("tagsScrollbar")
        self.horizontalLayout_3.addWidget(self.tagsScrollbar)
        self.verticalLayout_2.addWidget(self.tagsAndScrollbarFrame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.searchAndTagsFrame, 1, 0, 1, 1)

        self.retranslateUi(mainFrame)
        QtCore.QMetaObject.connectSlotsByName(mainFrame)

    def retranslateUi(self, mainFrame):
        _translate = QtCore.QCoreApplication.translate
        mainFrame.setWindowTitle(_translate("mainFrame", "Frame"))
        self.myLibraryLabel.setText(_translate("mainFrame", "My Library"))
        self.searchButton.setText(_translate("mainFrame", "go!"))
        self.searchLineEdit.setPlaceholderText(_translate("mainFrame", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = QtWidgets.QFrame()
    ui = Ui_mainFrame()
    ui.setupUi(mainFrame)
    mainFrame.show()
    sys.exit(app.exec_())
