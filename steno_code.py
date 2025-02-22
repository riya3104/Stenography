import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

# Function to encode message into image
def encode_image(image_path, secret_message, output_path):
    image = cv2.imread(image_path)
    
    # Convert message to binary + add delimiter
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message) + '1111111111111110'
    
    data_index = 0
    message_length = len(binary_message)
    height, width, _ = image.shape  

    for row in range(height):
        for col in range(width):
            pixel = image[row, col]
            for i in range(3):  
                if data_index < message_length:
                    pixel[i] = (pixel[i] & 254) | int(binary_message[data_index])  
                    data_index += 1
                else:
                    break
    cv2.imwrite(output_path, image)
    print("Message encoded successfully.")


# Function to decode message from image
import cv2
import numpy as np
from tkinter import messagebox

def decode_image(image_path):
    image = cv2.imread(image_path)
    binary_message = ""

    height, width, _ = image.shape  

    for row in range(height):
        for col in range(width):
            pixel = image[row, col]
            for i in range(3):  
                binary_message += str(pixel[i] & 1)

    # Find the delimiter index (to stop decoding correctly)
    delimiter = '1111111111111110'
    end_index = binary_message.find(delimiter)
    if end_index == -1:
        print("No valid message found!")
        messagebox.showerror("Error", "No hidden message found.")
        return

    # Extract only the actual message
    binary_message = binary_message[:end_index]

    # Convert binary back to text
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))

    print("Decoded message:", message)
    messagebox.showinfo("Decoded Message", f"Hidden message:\n{message}")


# GUI Functions
def encode_interface():
    image_path = filedialog.askopenfilename(title="Select Image for Encoding", filetypes=[("PNG Images", "*.png"), ("JPEG Images", "*.jpg"), ("All Files", "*.*")])
    if not image_path:
        return

    secret_message = simpledialog.askstring("Input", "Enter the message to hide:")
    if not secret_message:
        messagebox.showwarning("Warning", "No message entered!")
        return

    output_path = filedialog.asksaveasfilename(title="Save Encoded Image", defaultextension=".png", filetypes=[("PNG Images", "*.png")])
    if not output_path:
        return

    encode_image(image_path, secret_message, output_path)

def decode_interface():
    image_path = filedialog.askopenfilename(title="Select Image for Decoding", filetypes=[("PNG Images", "*.png"), ("JPEG Images", "*.jpg"), ("All Files", "*.*")])
    if not image_path:
        return

    decode_image(image_path)

# GUI Setup
root = tk.Tk()
root.title("Image Steganography Tool")
root.geometry("300x200")

tk.Button(root, text="Encode Message", command=encode_interface, padx=10, pady=5).pack(pady=10)
tk.Button(root, text="Decode Message", command=decode_interface, padx=10, pady=5).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit, padx=10, pady=5, bg="red", fg="white").pack(pady=10)

root.mainloop()
