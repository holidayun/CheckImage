# -*- coding: utf-8 -*-
import os
import shutil
from PIL import Image
import imghdr

class CheckBrockImage(object):
    def __init__(self, train_dir):
        self.train_dir = train_dir
        self.completeFile = 0
        self.incompleteFile = 0

    def get_imgs(self):
        """遍历某个文件夹下的所有图片 어떤 폴더에 있는 모든 그림 """
        for file in os.listdir(self.train_dir):
            if os.path.exists("./error_img/" ) == False:
                os.makedirs("./images_detection/"  + item)
            imgType = imghdr.what(self.train_dir + file)
            # if imgType.lower() == 'jpg' or imgType.lower() == "jpeg":
            if imgType == None or imgType == "jpeg":
                if os.path.splitext(file)[1].lower() == '.jpg' or os.path.splitext(file)[1].lower() == ".jpeg":
                    ret = self.check_img_jpg(file)
                    if ret:
                        self.completeFile += 1
                    else:
                        shutil.copy(self.train_dir + file, "./error_img/" + file)
                        self.incompleteFile = self.incompleteFile + 1
                        self.img_remove(file)  # 删除不完整图片 삭제하고 옮긴다. 그대로 두고 싶으면 # 할것  
            elif imgType.lower() == 'png':
                ret = self.check_img_png(file)
                if ret:
                    self.completeFile += 1
                else:
                    shutil.copy(self.train_dir + file, "./error_img/" + file)
                    self.incompleteFile = self.incompleteFile + 1
                    self.img_remove(file)  # 删除不完整图片 삭제하고 옮긴다. 그대로 두고 싶으면 # 할것
            else :
                print(self.train_dir + file, ": error", "images type is : ", imgType.lower())

    def img_remove(self, file):
        """删除图片 그림 삭제 """ 
        os.remove(self.train_dir + file)

    def check_img_jpg(self, img_file):
        """检测图片完整性，图片完整返回True,图片不完整返回False"""
        """그림 검사 완정성, 그림 완료 완료 True, 그림 완료가 False """
        return CheckImage(self.train_dir + img_file).check_jpg_jpeg()
    def check_img_png(self, img_file):
        return CheckImage(self.train_dir + img_file).check_png()

    def run(self):
        """执行文件 실행 파일 """
        self.get_imgs()
        print('incomplete images : %d个' % self.incompleteFile)
        print('complete images : %d个' % self.completeFile)

class CheckImage(object):

    def __init__(self, img):
        with open(img, "rb") as f:
            f.seek(-2, 2)
            self.img_text = f.read()
            f.close()

    def check_jpg_jpeg(self):
        """检测jpg图片完整性，完整返回True，不完整返回False"""
        """jpg 이미지 완정성 체크, 완료 True, 완전하게 False"""
    
        buf = self.img_text
        return buf.endswith(b'\xff\xd9')

    def check_png(self):
        """检测png图片完整性，完整返回True，不完整返回False"""

        buf = self.img_text
        return buf.endswith(b'\x60\x82')


if __name__ == '__main__':
    if os.path.exists("./error_img"):
        shutil.rmtree('./error_img')
    os.mkdir('./error_img')
    img_dir = input('input image path:')
    # train_dir = './eoo/'  # 检测文件夹 폴더 검ㅅ 
    imgs = CheckBrockImage(img_dir)
    imgs.run()
