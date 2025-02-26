Steps for encryption
1.Prepare the Image : Load the image into which the secret message will be embedded.
Check that the image is valid and can be processed.
2.Prepare the Secret Message : Convert the secret message into a list of characters.
Convert each character into its corresponding integer value using a dictionary (similar to c[i] in decryption).
3.Convert the Message into Pixel Values : For each character in the secret message, convert it to its corresponding integer (ASCII value).
Embed this integer into the pixel values of the image. The pixel values will be modified in a way that the encrypted message is hidden in the image.
4.Embed the Message into the Image : For each pixel, modify one of its color channels (red, green, or blue) to store the integer value of the character from the message.
Store the message character by character, ensuring that the color channels (R, G, B) of each pixel store the necessary encrypted value.
5.Save the Image : Once the message has been embedded in the image, save the modified image as the encrypted image.

Steps for decryption
1.Load the Encrypted Image : Load the encrypted image that contains the hidden secret message.
2.Check for Correct Passcode : Request the user to enter the passcode and verify if it matches the original one used during encryption. This ensures that the person decrypting the image has the right authorization.
3.Extract the Secret Message : Traverse the pixels of the image and extract the embedded message by converting each pixel value back to its corresponding character.
4.Output the Decrypted Message : After extracting all the characters, combine them to form the original secret message.
