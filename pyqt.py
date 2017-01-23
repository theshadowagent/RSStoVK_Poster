# Form implementation generated from reading ui file 'G:\PyCharm\project\rss.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class UIDialog(object):
    def setup_UI(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(508, 313)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 181, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.LineEdit = QtGui.QLineEdit(Dialog)
        self.LineEdit.setGeometry(QtCore.QRect(260, 60, 151, 21))
        self.LineEdit.setObjectName(_fromUtf8("textEdit"))
        self.label2 = QtGui.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(40, 130, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(12)
        font.setItalic(True)
        self.label2.setFont(font)
        self.label2.setObjectName(_fromUtf8("label_2"))
        self.LineEdit_2 = QtGui.QLineEdit(Dialog)
        self.LineEdit_2.setGeometry(QtCore.QRect(260, 140, 151, 21))
        self.LineEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(10)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslate_ui(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(_translate("Dialog", "RSS to VK Poster", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Количество новостей:</p></body></html>", None))
        self.label2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\"font-size:12pt;\">Интервал вывода:</span></p></body></html>",
                                       None))
        self.pushButton.setText(_translate("Dialog", "Применить", None))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dialog = QtGui.QDialog()
    ui = UIDialog()
    ui.setup_UI(dialog)
    dialog.show()
    sys.exit(app.exec_())

