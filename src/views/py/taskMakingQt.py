# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/taskMaking.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_taskMakingFrame(object):
    def setupUi(self, taskMakingFrame):
        taskMakingFrame.setObjectName("taskMakingFrame")
        taskMakingFrame.resize(803, 641)
        taskMakingFrame.setStyleSheet("background-color: rgb(255, 255, 242);\n"
"border-color: rgb(246, 247, 200);")
        self.gridLayout = QtWidgets.QGridLayout(taskMakingFrame)
        self.gridLayout.setContentsMargins(30, 10, 30, 50)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.answerButtonFrame = QtWidgets.QFrame(taskMakingFrame)
        self.answerButtonFrame.setStyleSheet("background-color: rgb(24, 35, 32);")
        self.answerButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.answerButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.answerButtonFrame.setObjectName("answerButtonFrame")
        self.answersLayout = QtWidgets.QHBoxLayout(self.answerButtonFrame)
        self.answersLayout.setObjectName("answersLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.answersLayout.addItem(spacerItem)
        self.addAnswerButton = QtWidgets.QPushButton(self.answerButtonFrame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(11)
        self.addAnswerButton.setFont(font)
        self.addAnswerButton.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);")
        self.addAnswerButton.setObjectName("addAnswerButton")
        self.answersLayout.addWidget(self.addAnswerButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.answersLayout.addItem(spacerItem1)
        self.removeAnswerButton = QtWidgets.QPushButton(self.answerButtonFrame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.removeAnswerButton.setFont(font)
        self.removeAnswerButton.setStyleSheet("background-color: rgb(246, 247, 200);\n"
"border-color: rgb(246, 247, 200);")
        self.removeAnswerButton.setObjectName("removeAnswerButton")
        self.answersLayout.addWidget(self.removeAnswerButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.answersLayout.addItem(spacerItem2)
        self.gridLayout.addWidget(self.answerButtonFrame, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(0, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem3, 4, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.answersScrollArea = QtWidgets.QScrollArea(taskMakingFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answersScrollArea.sizePolicy().hasHeightForWidth())
        self.answersScrollArea.setSizePolicy(sizePolicy)
        self.answersScrollArea.setMinimumSize(QtCore.QSize(500, 300))
        self.answersScrollArea.setStyleSheet("background-color: rgb(255, 255, 242);\n"
"border-color: rgb(255, 255, 242);")
        self.answersScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.answersScrollArea.setLineWidth(0)
        self.answersScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.answersScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.answersScrollArea.setWidgetResizable(True)
        self.answersScrollArea.setObjectName("answersScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 743, 393))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.answerScrollBarContents = QtWidgets.QVBoxLayout()
        self.answerScrollBarContents.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.answerScrollBarContents.setSpacing(0)
        self.answerScrollBarContents.setObjectName("answerScrollBarContents")
        self.verticalLayout_2.addLayout(self.answerScrollBarContents)
        self.answersScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.answersScrollArea, 4, 0, 1, 1)
        self.expressionFrame = QtWidgets.QFrame(taskMakingFrame)
        self.expressionFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.expressionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.expressionFrame.setObjectName("expressionFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.expressionFrame)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.deleteButton = QtWidgets.QPushButton(self.expressionFrame)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setItalic(False)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("background-color: rgb(24, 35, 32);\n"
"color: rgb(246, 247, 200);\n"
"")
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_3.addWidget(self.deleteButton)
        self.expressionInput = QtWidgets.QLineEdit(self.expressionFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expressionInput.sizePolicy().hasHeightForWidth())
        self.expressionInput.setSizePolicy(sizePolicy)
        self.expressionInput.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(11)
        self.expressionInput.setFont(font)
        self.expressionInput.setStyleSheet("background-color: rgb(255, 255, 242);\n"
"border-color: rgb(246, 247, 200);\n"
"alternate-background-color: rgb(246, 247, 200);\n"
"selection-background-color: rgb(246, 247, 200);")
        self.expressionInput.setText("")
        self.expressionInput.setObjectName("expressionInput")
        self.horizontalLayout_3.addWidget(self.expressionInput)
        self.ifValidLabel = QtWidgets.QLabel(self.expressionFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ifValidLabel.setFont(font)
        self.ifValidLabel.setStyleSheet("color: rgb(50, 168, 82);")
        self.ifValidLabel.setObjectName("ifValidLabel")
        self.horizontalLayout_3.addWidget(self.ifValidLabel)
        self.gridLayout.addWidget(self.expressionFrame, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(taskMakingFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 242);\n"
"border-color: rgb(246, 247, 200);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.taskDescriptionInput = QtWidgets.QPlainTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskDescriptionInput.sizePolicy().hasHeightForWidth())
        self.taskDescriptionInput.setSizePolicy(sizePolicy)
        self.taskDescriptionInput.setMinimumSize(QtCore.QSize(350, 0))
        self.taskDescriptionInput.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(11)
        self.taskDescriptionInput.setFont(font)
        self.taskDescriptionInput.setStyleSheet("background-color: rgb(255, 255, 242);\n"
"border-color: rgb(255, 255, 242);")
        self.taskDescriptionInput.setFrameShape(QtWidgets.QFrame.Panel)
        self.taskDescriptionInput.setFrameShadow(QtWidgets.QFrame.Raised)
        self.taskDescriptionInput.setObjectName("taskDescriptionInput")
        self.horizontalLayout.addWidget(self.taskDescriptionInput)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)

        self.retranslateUi(taskMakingFrame)
        QtCore.QMetaObject.connectSlotsByName(taskMakingFrame)

    def retranslateUi(self, taskMakingFrame):
        _translate = QtCore.QCoreApplication.translate
        taskMakingFrame.setWindowTitle(_translate("taskMakingFrame", "Frame"))
        self.addAnswerButton.setText(_translate("taskMakingFrame", "  Add answer  "))
        self.removeAnswerButton.setText(_translate("taskMakingFrame", "  Remove answer  "))
        self.deleteButton.setText(_translate("taskMakingFrame", "Delete"))
        self.expressionInput.setPlaceholderText(_translate("taskMakingFrame", "(Optional) Enter Expression"))
        self.ifValidLabel.setText(_translate("taskMakingFrame", "Valid"))
        self.taskDescriptionInput.setPlaceholderText(_translate("taskMakingFrame", "Enter task description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    taskMakingFrame = QtWidgets.QFrame()
    ui = Ui_taskMakingFrame()
    ui.setupUi(taskMakingFrame)
    taskMakingFrame.show()
    sys.exit(app.exec_())
