from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox


def generate_key(shape, seed=42):
    """Generate a pseudo-random key array of the same shape as the image."""
    np.random.seed(seed)  # Ensures reproducibility
    return np.random.randint(0, 256, size=shape, dtype=np.uint8)


def encrypt_image(input_path, output_path, key):
    """Encrypt an image using XOR encryption."""
    img = Image.open(input_path).convert("RGB")  # Ensure RGB mode
    img_array = np.array(img)

    # XOR encryption
    encrypted_array = img_array ^ key

    # Save encrypted image
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    messagebox.showinfo("Success", f"Image encrypted and saved as {output_path}")


def decrypt_image(input_path, output_path, key):
    """Decrypt an XOR-encrypted image."""
    encrypted_img = Image.open(input_path).convert("RGB")  # Ensure RGB mode
    encrypted_array = np.array(encrypted_img)

    # XOR decryption
    decrypted_array = encrypted_array ^ key

    # Convert back to image
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)
    messagebox.showinfo("Success", f"Image decrypted and saved as {output_path}")


def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    action = simpledialog.askstring("Input", "Do you want to encrypt or decrypt the image? (encrypt/decrypt)")
    if action not in ["encrypt", "decrypt"]:
        messagebox.showerror("Error", "Invalid option selected")
        return

    input_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if not input_path:
        messagebox.showerror("Error", "No file selected")
        return

    seed = simpledialog.askinteger("Input", "Enter a seed number for key generation:")
    if seed is None:
        messagebox.showerror("Error", "Invalid seed")
        return
