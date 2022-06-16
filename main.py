import sys

import cv2
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

import Tools
from API_Get import getApi
from UI import *


# noinspection PyTypeChecker
class MainForm(QMainWindow, Ui_Form, Tools.tools):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setMaximumSize(986, 545)
        self.setMinimumSize(986, 545)
        self.PicLabel.setPixmap(QPixmap(r"./oldImg.png"))
        self.PicLabel_2.setPixmap(QPixmap(r"./newImg.png"))
        self.setImg.clicked.connect(self.open_image)
        self.Start.clicked.connect(self.SendImg_And_Infos)
        self.Save.clicked.connect(self.SaveImg)
        self.Exit.clicked.connect(self.exit)
        self.comboBox.activated.connect(self.ChangeFace)

    def open_image(self):
        img_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "*.jpg;;*.png;;*.jpeg")
        self.PicLabel.setPixmap(QPixmap(img_name))
        self.PicLabel_2.setPixmap(QPixmap(r"./newImg.png"))
        self.FilePath.setText(img_name)

    def SendImg_And_Infos(self):
        filePath = self.FilePath.text()
        # 清除下拉列表中所有选项
        self.comboBox.clear()
        if filePath.isspace() or len(filePath) == 0 or filePath == '':
            QMessageBox.critical(self, "错误", "请选择图片！")
        else:
            # 读取信息
            global Axis, faceNums, Gender, Age, Mask, Glass, Hat, Beauty
            Axis = []
            Gender = []
            Age = []
            Mask = []
            Glass = []
            Hat = []
            Beauty = []
            json = getApi(filePath)
            faceInfos = json['FaceInfos']
            faceNums = len(faceInfos)
            for i in range(faceNums):
                Axis.append([])
                Axis[i].append(faceInfos[i]['X'])
                Axis[i].append(faceInfos[i]['Y'])
                Axis[i].append(faceInfos[i]['Width'])
                Axis[i].append(faceInfos[i]['Height'])
                FaceAttributesInfo = faceInfos[i]['FaceAttributesInfo']
                self.comboBox.addItem(str(i))
                if FaceAttributesInfo['Gender'] == 0:
                    Gender.append('女')
                else:
                    Gender.append('男')
                Age.append(FaceAttributesInfo['Age'])
                Beauty.append(FaceAttributesInfo['Beauty'])
                if FaceAttributesInfo['Hat']:
                    Hat.append('有')
                else:
                    Hat.append('无')
                if FaceAttributesInfo['Mask']:
                    Mask.append('有')
                else:
                    Mask.append('无')
                if FaceAttributesInfo['Glass']:
                    Glass.append('有')
                else:
                    Glass.append('无')

            self.face_num.setText(str(faceNums))
            # 人脸信息属性框默认设置为第一个
            self.Mask_Text.setText(str(Mask[0]))
            self.Age_Text.setText(str(Age[0]))
            self.Beauty_Text.setText(str(Beauty[0]))
            self.Hat_Text.setText(str(Hat[0]))
            self.Glass_Text.setText(str(Glass[0]))
            self.Gender_Text.setText(str(Gender[0]))
            # 绘制矩形并载入图片
            ImgCachePath = Tools.tools.draw_rectangle(filePath, Axis)
            self.PicLabel_2.setPixmap(QPixmap(ImgCachePath))

    def SaveImg(self):
        # 重写draw_rectangle方法
        def draw_rectangle(filePath: str):
            img = cv2.imread(filePath)
            for i in range(faceNums):
                pt1 = (Axis[i][0], Axis[i][1])
                pt2 = (Axis[i][0] + Axis[i][2], Axis[i][1] + Axis[i][3])
                cv2.rectangle(img, pt1, pt2, (0, 255, 255), 2)
                cv2.putText(img, str(i), pt1, 1, 2, (0, 255, 255), 3)
            ImgSaved_Path = './ImgSaved/' + 'out-' + filePath.split('/')[-1]
            cv2.imwrite(ImgSaved_Path, img)

        fileName = self.FilePath.text().split('/')[-1]
        new_filePath = './ImgCache/' + fileName
        draw_rectangle(new_filePath)

    def ChangeFace(self):
        currentText = int(self.comboBox.currentText())
        self.Mask_Text.setText(str(Mask[currentText]))
        self.Age_Text.setText(str(Age[currentText]))
        self.Beauty_Text.setText(str(Beauty[currentText]))
        self.Hat_Text.setText(str(Hat[currentText]))
        self.Glass_Text.setText(str(Glass[currentText]))
        self.Gender_Text.setText(str(Gender[currentText]))

    @staticmethod
    def exit():
        Tools.tools.del_files('./ImgCache')
        quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainForm()
    myWin.show()
    sys.exit(app.exec())
