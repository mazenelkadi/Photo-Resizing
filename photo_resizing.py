import tkinter as tk  # Tkinter for creating GUI elements
from tkinter import filedialog, simpledialog  # Dialogs for file and input
from PIL import Image  # Python Imaging Library for image processing
from pathlib import Path  # For handling filesystem paths


def select_images():
    """Open a dialog to select image files."""
    root = tk.Tk()
    root.withdraw()  # Hide the tkinter root window
    file_paths = filedialog.askopenfilenames(
        title="Select Image Files",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    return list(file_paths)


def select_save_directory():
    """Open a dialog to select the save directory for resized images."""
    root = tk.Tk()
    root.withdraw()  # Hide the tkinter root window
    directory = filedialog.askdirectory(
        title="Select Directory to Save Resized Images")
    return directory


def get_resize_dimensions():
    """Prompt the user to enter the new width and height for resizing."""
    root = tk.Tk()
    root.withdraw()  # Hide the tkinter root window
    width = simpledialog.askinteger(
        "Input", "Enter the width:", parent=root, minvalue=1, maxvalue=10000)
    height = simpledialog.askinteger(
        "Input", "Enter the height:", parent=root, minvalue=1, maxvalue=10000)
    return width, height


def resize_images(image_paths, save_directory, new_size):
    """Resize the selected images to the specified dimensions and save them."""
    for image_path in image_paths:
        with Image.open(image_path) as img:
            img_resized = img.resize(new_size)
            save_path = Path(save_directory) / Path(image_path).name
            img_resized.save(save_path)
            print(f"Resized and saved: {save_path}")


if __name__ == '__main__':
    selected_images = select_images()
    if selected_images:
        save_directory = select_save_directory()
        if save_directory:
            new_size = get_resize_dimensions()
            if new_size:
                resize_images(selected_images, save_directory, new_size)
                print(f"Images resized and saved in {save_directory}")
            else:
                print("Resize dimensions not provided.")
        else:
            print("No save directory selected.")
    else:
        print("No images selected.")
