# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/notFound.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_notFoundFrame(object):
    def setupUi(self, notFoundFrame):
        notFoundFrame.setObjectName("notFoundFrame")
        notFoundFrame.resize(547, 459)
        self.horizontalLayout = QtWidgets.QHBoxLayout(notFoundFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.apologyLabel = QtWidgets.QLabel(notFoundFrame)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.apologyLabel.setFont(font)
        self.apologyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.apologyLabel.setWordWrap(True)
        self.apologyLabel.setObjectName("apologyLabel")
        self.horizontalLayout.addWidget(self.apologyLabel)

        self.retranslateUi(notFoundFrame)
        QtCore.QMetaObject.connectSlotsByName(notFoundFrame)

    def retranslateUi(self, notFoundFrame):
        _translate = QtCore.QCoreApplication.translate
        notFoundFrame.setWindowTitle(_translate("notFoundFrame", "Frame"))
        self.apologyLabel.setText(_translate("notFoundFrame", "Sorry, we didn\'t have enough time to finish that feature."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    notFoundFrame = QtWidgets.QFrame()
    ui = Ui_notFoundFrame()
    ui.setupUi(notFoundFrame)
    notFoundFrame.show()
    sys.exit(app.exec_())
