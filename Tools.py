import os
import shutil

import cv2


# noinspection PyMethodParameters
class tools:
    # 获取路径中的文件名
    def get_image_name(Path: str) -> list['str']:
        fileName = Path.split('/')[-1].split('.')
        return fileName

    # 绘制矩形
    def draw_rectangle(filePath: str, Axis: list) -> str:
        fileName = tools.get_image_name(filePath)
        faceNums = len(Axis)
        shutil.copy(filePath, './ImgCache/' + fileName[0] + '.' + fileName[1])
        img = cv2.imread(filePath)
        for i in range(faceNums):
            pt1 = (Axis[i][0], Axis[i][1])
            pt2 = (Axis[i][0] + Axis[i][2], Axis[i][1] + Axis[i][3])
            cv2.rectangle(img, pt1, pt2, (0, 255, 255), 2)
            cv2.putText(img, str(i), pt1, 1, 2, (0, 255, 255),3)

        ImgCache_Path = './ImgCache/' + fileName[0] + '-ImgCache.' + fileName[1]
        cv2.imwrite(ImgCache_Path, img)
        return ImgCache_Path

    # 删除文件夹中所有文件
    def del_files(path_file: str):
        ls = os.listdir(path_file)
        for i in ls:
            f_path = os.path.join(path_file, i)
            if os.path.isdir(f_path):
                tools.del_files(f_path)
            else:
                os.remove(f_path)
