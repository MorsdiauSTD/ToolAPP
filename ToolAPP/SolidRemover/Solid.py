import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

def remove_bg():
    image_path = filedialog.askopenfilename(title="Select an image to remove background")
    if image_path:
        lower_color = np.array([35, 100, 100])
        upper_color = np.array([85, 255, 255])

        foreground = remove_bg(image_path, lower_color, upper_color)

        cv2.imwrite("foreground_image.png", foreground)
        result_label.config(text="Background removed and saved as 'foreground_image.png'.")

root = tk.Tk()
root.title("BG Remover")

remove_button = tk.Button(root, text="Remove Background", command=remove_bg)
remove_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()