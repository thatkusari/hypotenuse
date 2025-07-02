# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'hippo.ui'
##
# Created by: Qt User Interface Compiler version 6.9.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 200)
        icon = QIcon()
        icon.addFile(u"hippo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.widthLabel = QLabel(Form)
        self.widthLabel.setObjectName(u"widthLabel")

        self.formLayout.setWidget(
            0, QFormLayout.ItemRole.LabelRole, self.widthLabel)

        self.widthLineEdit = QLineEdit(Form)
        self.widthLineEdit.setObjectName(u"widthLineEdit")

        self.formLayout.setWidget(
            0, QFormLayout.ItemRole.FieldRole, self.widthLineEdit)

        self.heightLabel = QLabel(Form)
        self.heightLabel.setObjectName(u"heightLabel")

        self.formLayout.setWidget(
            1, QFormLayout.ItemRole.LabelRole, self.heightLabel)

        self.heightLineEdit = QLineEdit(Form)
        self.heightLineEdit.setObjectName(u"heightLineEdit")

        self.formLayout.setWidget(
            1, QFormLayout.ItemRole.FieldRole, self.heightLineEdit)

        self.verticalLayout_2.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.calculateButton = QPushButton(Form)
        self.calculateButton.setObjectName(u"calculateButton")

        self.horizontalLayout_2.addWidget(self.calculateButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.resultLabel = QLabel(Form)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.resultLabel.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse | Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.resultLabel)

        self.resultLineEdit = QLineEdit(Form)
        self.resultLineEdit.setObjectName(u"resultLineEdit")

        self.horizontalLayout.addWidget(self.resultLineEdit)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate(
            "Form", u"Calculate the hypotenuse", None))
        self.widthLabel.setText(QCoreApplication.translate(
            "Form", u"What is the width?", None))
        self.widthLineEdit.setText("")
        self.heightLabel.setText(QCoreApplication.translate(
            "Form", u"What is the height?", None))
        self.calculateButton.setText(
            QCoreApplication.translate("Form", u"Calculate!", None))
        self.resultLabel.setText(QCoreApplication.translate(
            "Form", u"The result is:", None))
    # retranslateUi
