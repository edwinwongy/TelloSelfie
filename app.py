from djitellopy.tello import Tello
import cv2
from models.yolov3 import yolo_video as model
from PIL import Image
import numpy as np


def run():
    tello = Tello()
    tello.connect()
    if not tello.streamoff():
        print("Could not stop video stream")

    if not tello.streamon():
        print("Could not start video stream")

    frame_read = tello.get_frame_read()
    while True:
        if frame_read.stopped:
            frame_read.stop()
            break

        # Display the resulting frame
        img = Image.fromarray(frame_read.frame)
        frame = model.detect_img(img)
        cv2.imshow('frame', np.array(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            tello.end()
            break


run()
#

#
# def testtakeoff():
#     tello.takeoff()
#     time.sleep(5)
#
#     tello.move_left(100)
#     time.sleep(5)
#
#     tello.rotate_counter_clockwise(45)
#     time.sleep(5)
#
#     tello.land()
#     time.sleep(5)
#
#     tello.end()
