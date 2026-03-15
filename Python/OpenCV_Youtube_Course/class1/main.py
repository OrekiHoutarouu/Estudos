import cv2
import os

def read_image():
    root = os.getcwd()
    image_path = os.path.join(root, "class1/img/picture.jpg")
    image = cv2.imread(image_path)
    cv2.imshow("img", image)
    cv2.waitKey(0)

def write_image():
    root = os.getcwd()
    image_path = os.path.join(root, "class1/img/picture.jpg")
    image = cv2.imread(image_path)
    output_path = os.path.join(root, "class1/img/output.jpg")
    cv2.imwrite(output_path, image)

if __name__ == "__main__":
    print(cv2.__version__)
    read_image()
    write_image()