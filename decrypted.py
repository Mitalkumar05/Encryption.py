import cv2

def decrypt_image(encrypted_image_path, password, secret_message_length):

    img = cv2.imread(encrypted_image_path)
    if img is None:
        raise ValueError(f"Image at {encrypted_image_path} could not be loaded.")

    d = {chr(i): i for i in range(255)}
    c = {i: chr(i) for i in range(255)}

    n = 0
    m = 0
    z = 0
    message = ""

    passcode_input = input("Enter passcode for Decryption: ")

    if password == passcode_input:

        for i in range(secret_message_length):
            message += c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3

        print("Decrypted message:", message)
    else:
        print("YOU ARE NOT authorized")

if __name__ == "__main__":
    encrypted_image_path = input("Enter the encrypted image path: ")
    password = input("Enter the passcode: ")

    secret_message_length = int(input("Enter the length of the secret message: "))
    
    decrypt_image(encrypted_image_path, password, secret_message_length)
