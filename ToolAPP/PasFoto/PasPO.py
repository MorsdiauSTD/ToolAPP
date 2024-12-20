import tkinter as tk
from tkinter import filedialog, messagebox, Canvas, PhotoImage
import cv2
import numpy as np
from PIL import Image, ImageTk

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor Application")
        
        self.image_path = None
        self.original_image = None
        self.cropped_image = None
        self.bg_removed_image = None
        
        self.create_widgets()
        
    def create_widgets(self):
        self.add_image_button = tk.Button(self.root, text="Add Image", command=self.add_image)
        self.add_image_button.pack()
        
        self.canvas = Canvas(self.root, width=600, height=400)
        self.canvas.pack()
        
        self.crop_button = tk.Button(self.root, text="Crop Image", command=self.crop_image)
        self.crop_button.pack()
        
        self.remove_bg_button = tk.Button(self.root, text="Remove Background", command=self.remove_background)
        self.remove_bg_button.pack()
        
        self.color_button = tk.Button(self.root, text="Change Background Color", command=self.change_bg_color)
        self.color_button.pack()
        
        self.save_button = tk.Button(self.root, text="Save Image", command=self.save_image)
        self.save_button.pack()
        
        self.undo_button = tk.Button(self.root, text="Undo", command=self.undo)
        self.undo_button.pack()
        
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
        
    def add_image(self):
        self.image_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.original_image = cv2.imread(self.image_path)
            self.display_image(self.original_image)
    
    def display_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=image)
        self.canvas.image = image  # Keep a reference to avoid garbage collection
    
    def crop_image(self):
        # Placeholder for cropping functionality
        # You would implement a movable crop tool here
        if self.original_image is not None:
            # Example crop (you would replace this with actual cropping logic)
            self.cropped_image = self.original_image[50:350, 50:350]  # Dummy crop
            self.display_image(self.cropped_image)
    
    def remove_background(self):
        if self.cropped_image is not None:
            # Simple background removal using color range (this is a placeholder)
            lower_color = np.array([35, 100, 100])
            upper_color = np.array([85, 255, 255])
            mask = cv2.inRange(self.cropped_image, lower_color, upper_color)
            self.bg_removed_image = cv2.bitwise_and(self.cropped_image, self.cropped_image, mask=mask)
            self.display_image(self.bg_removed_image)
    
    def change_bg_color(self):
        if self.bg_removed_image is not None:
            # Change background color (this is a placeholder)
            bg_color = (255, 0, 0)  # Red background
            self.bg_removed_image[np.where((self.bg_removed_image == [0, 0, 0]).all(axis=2))] = bg_color
            self.display_image(self.bg_removed_image)
    
    def save_image(self):
        if self.bg_removed_image is not None:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                cv2.imwrite(save_path, self.bg_removed_image)
                messagebox.showinfo("Image Saved", "Image saved successfully!")
    
    def undo(self):
        # Placeholder for undo functionality
        messagebox.showinfo("Undo", "Undo functionality not implemented yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()