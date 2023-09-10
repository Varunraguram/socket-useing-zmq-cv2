import cv2
import zmq
import imagezmq

# Initialize the ImageHub on the receiver with the loopback address and port
receiver = imagezmq.ImageHub(open_port="tcp://127.0.0.1:5555")

while True:
    # Receive the image and the sender's message
    sender_name, frame = receiver.recv_image()

    # Display the received image (you can replace 'sender_name' with your own label)
    cv2.imshow(sender_name, frame)

    # Optional: Respond to the sender to acknowledge receipt (if needed)
    receiver.send_reply(b"OK")
    print('ok')

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
