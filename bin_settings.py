# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bin_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(435, 197)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 150, 231, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 50, 30))
        self.label.setObjectName("label")
        self.width_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.width_lineEdit.setGeometry(QtCore.QRect(90, 20, 120, 30))
        self.width_lineEdit.setObjectName("width_lineEdit")
        self.channels_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.channels_lineEdit.setGeometry(QtCore.QRect(90, 70, 120, 30))
        self.channels_lineEdit.setObjectName("channels_lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 50, 30))
        self.label_2.setObjectName("label_2")
        self.heigth_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.heigth_lineEdit.setGeometry(QtCore.QRect(290, 20, 120, 30))
        self.heigth_lineEdit.setObjectName("heigth_lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(230, 20, 50, 30))
        self.label_3.setObjectName("label_3")
        self.dtype_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.dtype_lineEdit.setGeometry(QtCore.QRect(290, 70, 120, 30))
        self.dtype_lineEdit.setObjectName("dtype_lineEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(230, 70, 50, 30))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 571, 30))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "宽度"))
        self.label_2.setText(_translate("Dialog", "通道数"))
        self.label_3.setText(_translate("Dialog", "高度"))
        self.label_4.setText(_translate("Dialog", "dtype"))
        self.label_5.setText(_translate("Dialog", "一般情况下：RGB：通道数=3,dtype=uint8；IR：通道数=1,dtype=uint16"))
