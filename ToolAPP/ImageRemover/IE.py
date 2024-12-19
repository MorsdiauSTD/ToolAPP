import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def remove_image():
    image_path = filedialog.askopenfilename(title="Select an image to remove")
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Image '{image_path}' removed successfully.")
    else:
        print(f"Image '{image_path}' does not exist.")

root = tk.Tk()
root.title("Image Remover Application")

remove_button = tk.Button(root, text="Remove Image", command= remove_image)
remove_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

# Example usage
# image_to-remove = ""
# remove_image(image_to_remove)