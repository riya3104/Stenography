## Secure Data Hiding in Images Using Steganography  
This project implements image steganography using Python and OpenCV, where a secret message is hidden inside an image using the Least Significant Bit (LSB) technique.

---

### Features  
- Encode a secret message into an image  
- Decode the hidden message from an image  
- Simple GUI interface using Tkinter  

---

### Technologies Used  
- Python  
- OpenCV  
- NumPy  
- Tkinter  

---

### Installation  
Run the following command to install dependencies:  
```sh
pip install opencv-python numpy

# Usage
1.Run the script:
2.Encoding:
Select an image
Enter a secret message
Save the encoded image
3.Decoding:
Load the encoded image
Extract and display the hidden message

# Project Structure
steganography_project  
│── steno_code.py          # Main script  
│── sample_image.png       # Test image  
