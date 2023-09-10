import cv2
import zmq
import imagezmq

# Initialize the ImageSender with the loopback address
sender = imagezmq.ImageSender(connect_to="tcp://127.0.0.1:5555")

# Read an image from file or capture it from a camera (replace with your image source)
image_path = "D:\imagezmq-master\img.jpg"
frame = cv2.imread(image_path)

# Send the image to the receiver
sender.send_image("Image from Sender", frame)
