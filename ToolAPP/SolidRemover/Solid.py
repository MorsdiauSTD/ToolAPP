import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

def remove_bg():
    image_path = filedialog.askopenfilename(title="Select an image to remove background")
    if image_path:
        img = cv2.imread(image_path)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur_img = cv2.GaussianBlur(gray_img, (7, 7), 0)