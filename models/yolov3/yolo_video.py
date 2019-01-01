from models.yolov3.yolo import YOLO
from PIL import Image

yolo = YOLO()


def detect_img(image):
    return yolo.detect_image(image)
    # r_image.show()
