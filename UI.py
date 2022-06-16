from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QGroupBox, QLabel, QLineEdit,QComboBox,
                               QPushButton, QToolButton)


# noinspection PyTypeChecker
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(986, 545)
        # 选择图片按钮
        self.setImg = QToolButton(Form)
        self.setImg.setObjectName(u"setImg")
        self.setImg.setGeometry(QRect(540, 30, 41, 31))

        # 路径文本框
        self.FilePath = QLineEdit(Form)
        self.FilePath.setObjectName(u"FilePath")
        self.FilePath.setGeometry(QRect(70, 30, 471, 31))
        self.PicLabel = QLabel(Form)
        self.PicLabel.setObjectName(u"PicLabel")
        # 图片自适应大小
        self.PicLabel.setScaledContents(True)
        self.PicLabel.setGeometry(QRect(60, 110, 250, 320))
        self.PicLabel.setPixmap(QPixmap(r".\oldImg.png"))

        # 识别图片Label
        self.PicLabel_2 = QLabel(Form)
        self.PicLabel_2.setObjectName(u"PicLabel_2")
        self.PicLabel_2.setScaledContents(True)
        self.PicLabel_2.setGeometry(QRect(420, 110, 250, 320))
        self.PicLabel.setPixmap(QPixmap(r".\newImg.png"))

        # 开始识别按钮
        self.Start = QPushButton(Form)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(640, 30, 221, 31))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.Start.setFont(font)

        # 面部信息Layout
        self.FaceInfos = QGroupBox(Form)
        self.FaceInfos.setObjectName(u"FaceInfos")
        self.FaceInfos.setGeometry(QRect(680, 100, 251, 351))
        self.Gender = QLabel(self.FaceInfos)
        self.Gender.setObjectName(u"Gender")
        self.Gender.setGeometry(QRect(20, 40, 54, 16))
        self.Age = QLabel(self.FaceInfos)
        self.Age.setObjectName(u"Age")
        self.Age.setGeometry(QRect(20, 80, 81, 16))
        self.Hat = QLabel(self.FaceInfos)
        self.Hat.setObjectName(u"Hat")
        self.Hat.setGeometry(QRect(20, 120, 53, 16))
        self.Glass = QLabel(self.FaceInfos)
        self.Glass.setObjectName(u"Glass")
        self.Glass.setGeometry(QRect(20, 160, 53, 16))
        self.Mask = QLabel(self.FaceInfos)
        self.Mask.setObjectName(u"Mask")
        self.Mask.setGeometry(QRect(20, 200, 53, 16))
        self.Beauty = QLabel(self.FaceInfos)
        self.Beauty.setObjectName(u"Beauty")
        self.Beauty.setGeometry(QRect(20, 240, 53, 16))
        self.Beauty_Text = QLineEdit(self.FaceInfos)
        self.Beauty_Text.setObjectName(u"Beauty_Text")
        self.Beauty_Text.setGeometry(QRect(110, 230, 113, 30))
        font1 = QFont()
        font1.setPointSize(13)
        self.Gender.setFont(font1)
        self.Mask.setFont(font1)
        self.Hat.setFont(font1)
        self.Glass.setFont(font1)
        self.Age.setFont(font1)
        self.Beauty.setFont(font1)

        self.Gender_Text = QLineEdit(self.FaceInfos)
        self.Gender_Text.setObjectName(u"Gender_Text")
        self.Gender_Text.setGeometry(QRect(110, 30, 113, 30))
        self.Age_Text = QLineEdit(self.FaceInfos)
        self.Age_Text.setObjectName(u"Age_Text")
        self.Age_Text.setGeometry(QRect(110, 70, 113, 30))
        self.Hat_Text = QLineEdit(self.FaceInfos)
        self.Hat_Text.setObjectName(u"Hat_Text")
        self.Hat_Text.setGeometry(QRect(110, 110, 113, 30))
        self.Glass_Text = QLineEdit(self.FaceInfos)
        self.Glass_Text.setObjectName(u"Glass_Text")
        self.Glass_Text.setGeometry(QRect(110, 150, 113, 30))
        self.Mask_Text = QLineEdit(self.FaceInfos)
        self.Mask_Text.setObjectName(u"Mask_Text")
        self.Mask_Text.setGeometry(QRect(110, 190, 113, 30))
        # 下拉列表
        self.comboBox = QComboBox(self.FaceInfos)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 0, 69, 22))
        # 保存按钮
        self.Save = QPushButton(self.FaceInfos)
        self.Save.setObjectName(u"Save")
        self.Save.setGeometry(QRect(40, 280, 171, 61))
        self.Save.setFont(font)

        # 退出按钮
        self.Exit = QPushButton(Form)
        self.Exit.setObjectName(u"Exit")
        self.Exit.setGeometry(QRect(860, 480, 71, 41))
        font2 = QFont()
        font2.setBold(True)
        self.Exit.setFont(font2)

        # 脸数
        self.face_num = QLabel(Form)
        self.face_num.setObjectName(u"face_num")
        self.face_num.setGeometry(QRect(770, 70, 51, 21))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.face_num.setFont(font3)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 5, 71, 21))
        self.label.setFont(font)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 440, 71, 31))
        self.label_2.setFont(font)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(510, 440, 71, 31))
        self.label_3.setFont(font)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(640, 70, 121, 21))
        self.label_4.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4eba\u50cf\u4fe1\u606f\u8bc6\u522b", None))
        self.setImg.setText(QCoreApplication.translate("Form", u"...", None))
        self.PicLabel.setText(QCoreApplication.translate("Form", u"\u539f\u59cb\u56fe\u7247", None))
        self.PicLabel_2.setText(QCoreApplication.translate("Form", u"\u8bc6\u522b\u56fe\u7247", None))
        self.Start.setText(QCoreApplication.translate("Form", u"\u8bc6\u522b", None))
        self.FaceInfos.setTitle(QCoreApplication.translate("Form", u"FaceInfos", None))
        # noinspection PyTypeChecker
        self.Gender.setText(QCoreApplication.translate("Form", u"\u6027\u522b\uff1a", None))
        self.Age.setText(QCoreApplication.translate("Form", u"\u9884\u4f30\u5e74\u9f84\uff1a", None))
        self.Hat.setText(QCoreApplication.translate("Form", u"\u5e3d\u5b50\uff1a", None))
        self.Glass.setText(QCoreApplication.translate("Form", u"\u773c\u955c\uff1a", None))
        self.Mask.setText(QCoreApplication.translate("Form", u"\u53e3\u7f69\uff1a", None))
        self.Beauty.setText(QCoreApplication.translate("Form", u"\u9b45\u529b\u503c\uff1a", None))
        self.Save.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.Exit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u8def\u5f84", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u539f\u59cb\u56fe\u7247", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8bc6\u522b\u56fe\u7247", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8bc6\u522b\u5230\u7684\u4eba\u6570\uff1a", None))
        self.face_num.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi
