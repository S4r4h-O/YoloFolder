# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QProgressBar,
    QSizePolicy, QSlider, QSpacerItem, QToolButton,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(270, 276)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"DejaVu Serif"])
        font.setPointSize(11)
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.dirButton2 = QToolButton(Dialog)
        self.dirButton2.setObjectName(u"dirButton2")

        self.gridLayout.addWidget(self.dirButton2, 3, 2, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 9, 2, 1, 1)

        self.imageInput = QLineEdit(Dialog)
        self.imageInput.setObjectName(u"imageInput")

        self.gridLayout.addWidget(self.imageInput, 1, 0, 1, 4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 10, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 8, 0, 1, 1)

        self.dirButton1 = QToolButton(Dialog)
        self.dirButton1.setObjectName(u"dirButton1")

        self.gridLayout.addWidget(self.dirButton1, 0, 2, 1, 1)

        self.outInput = QLineEdit(Dialog)
        self.outInput.setObjectName(u"outInput")

        self.gridLayout.addWidget(self.outInput, 7, 0, 1, 4)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 11, 2, 1, 2)

        self.dirButton3 = QToolButton(Dialog)
        self.dirButton3.setObjectName(u"dirButton3")

        self.gridLayout.addWidget(self.dirButton3, 6, 1, 1, 1)

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 12, 0, 1, 4)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)

        self.labelInput = QLineEdit(Dialog)
        self.labelInput.setObjectName(u"labelInput")

        self.gridLayout.addWidget(self.labelInput, 4, 0, 1, 4)

        self.horizontalSlider = QSlider(Dialog)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 9, 3, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"YOLOfolder", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Out dir.:", None))
        self.dirButton2.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u" %:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Images dir.:", None))
        self.dirButton1.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.dirButton3.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Labels dir.:", None))
    # retranslateUi

