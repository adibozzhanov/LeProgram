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
        mainFrame.resize(1345, 796)
        self.gridLayout = QtWidgets.QGridLayout(mainFrame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.testScrollArea = QtWidgets.QScrollArea(mainFrame)
        self.testScrollArea.setMinimumSize(QtCore.QSize(500, 500))
        self.testScrollArea.setMaximumSize(QtCore.QSize(1500, 16777215))
        self.testScrollArea.setWidgetResizable(True)
        self.testScrollArea.setObjectName("testScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 498, 620))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.testsAreaContents = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.testsAreaContents.setObjectName("testsAreaContents")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.testsAreaContents.addItem(spacerItem2)
        self.testScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.testScrollArea, 1, 4, 1, 1)
        self.searchAndTagsFrame = QtWidgets.QFrame(mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchAndTagsFrame.sizePolicy().hasHeightForWidth())
        self.searchAndTagsFrame.setSizePolicy(sizePolicy)
        self.searchAndTagsFrame.setMinimumSize(QtCore.QSize(300, 0))
        self.searchAndTagsFrame.setMaximumSize(QtCore.QSize(700, 16777215))
        self.searchAndTagsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchAndTagsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchAndTagsFrame.setObjectName("searchAndTagsFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.searchAndTagsFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(60, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem3)
        self.searchFrame = QtWidgets.QFrame(self.searchAndTagsFrame)
        self.searchFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.searchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchFrame.setObjectName("searchFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.searchFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchButton = QtWidgets.QPushButton(self.searchFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMinimumSize(QtCore.QSize(50, 50))
        self.searchButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.searchLineEdit = QtWidgets.QLineEdit(self.searchFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLineEdit.sizePolicy().hasHeightForWidth())
        self.searchLineEdit.setSizePolicy(sizePolicy)
        self.searchLineEdit.setMaximumSize(QtCore.QSize(16777215, 80))
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
        self.tagsFrame.setMinimumSize(QtCore.QSize(0, 300))
        self.tagsFrame.setBaseSize(QtCore.QSize(0, -31072))
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
        spacerItem4 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem4)
        self.gridLayout.addWidget(self.searchAndTagsFrame, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 6, 1, 1)
        self.myLibraryLabel = QtWidgets.QLabel(mainFrame)
        self.myLibraryLabel.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.myLibraryLabel.setFont(font)
        self.myLibraryLabel.setObjectName("myLibraryLabel")
        self.gridLayout.addWidget(self.myLibraryLabel, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 3, 1, 1)

        self.retranslateUi(mainFrame)
        QtCore.QMetaObject.connectSlotsByName(mainFrame)

    def retranslateUi(self, mainFrame):
        _translate = QtCore.QCoreApplication.translate
        mainFrame.setWindowTitle(_translate("mainFrame", "Frame"))
        self.searchButton.setText(_translate("mainFrame", "go!"))
        self.searchLineEdit.setPlaceholderText(_translate("mainFrame", "Search"))
        self.myLibraryLabel.setText(_translate("mainFrame", "My Library"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = QtWidgets.QFrame()
    ui = Ui_mainFrame()
    ui.setupUi(mainFrame)
    mainFrame.show()
    sys.exit(app.exec_())
