import cv2
import os
import numpy

def video_from_webcam():
    capture = cv2.VideoCapture(0)

    if not capture.isOpened():
        exit()

    while True:
        ret, frame = capture.read()

        if ret:
            cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) == ord("q"):
            break
    
    capture.release()
    cv2.destroyAllWindows()

def video_from_file():
    root = os.getcwd()
    video_path = os.path.join(root, "class2/video/video.mp4")
    capture = cv2.VideoCapture(video_path)
    
    while capture.isOpened():
        ret, frame = capture.read()
        delay = int(1000/60)

        if ret:
            cv2.imshow("video", frame)

        if cv2.waitKey(delay) == ord("q"):
            break

def video_to_file():
    capture = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    root = os.getcwd()
    output_path = os.path.join(root, "class2/video/output.mp4")
    output = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

    while capture.isOpened():
        ret, frame = capture.read()

        if ret:
            output.write(frame)
            cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) == ord("q"):
            break
    
    capture.release()
    output.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_from_webcam()
    video_from_file()
    video_to_file()