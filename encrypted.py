import cv2
import os

def encrypt_image(image_path, secret_message, password, encrypted_image_path="Myimage.jpg"):
    if not os.path.exists(image_path):
        raise ValueError(f"Image at {image_path} does not exist. Please check the file path.")
    
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image at {image_path} could not be loaded. Make sure the image is a valid format.")
    
    d = {chr(i): i for i in range(255)}
    c = {i: chr(i) for i in range(255)}

    m = 0
    n = 0
    z = 0

    for i in range(len(secret_message)):
        img[n, m, z] = d[secret_message[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite(encrypted_image_path, img)

    os.system(f"start {encrypted_image_path}")  

    print("Encryption complete!")

if __name__ == "__main__":
    image_path = input("Enter the image path (e.g., C:/path/to/Myinage.jpg): ")
    secret_message = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    encrypt_image(image_path, secret_message, password)
