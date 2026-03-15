import cv2
import os
import matplotlib.pyplot
import numpy

def read_image():
    root = os.getcwd()
    image_path = os.path.join(root, "img/picture.jpg")
    image = cv2.imread(image_path)
    cv2.imshow("img", image)
    cv2.waitKey(0)

def write_image():
    root = os.getcwd()
    image_path = os.path.join(root, "img/picture.jpg")
    image = cv2.imread(image_path)
    output_path = os.path.join(root, "img/output.jpg")
    cv2.imwrite(output_path, image)

if __name__ == "__main__":
    read_image()
    write_image()