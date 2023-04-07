import cv2
import hashlib

# Open the video file
cap = cv2.VideoCapture('completely different video.mp4')

# Initialize the hash object
hash_obj = hashlib.sha256()

# Loop through the frames of the video
while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()

    # If we have reached the end of the video, exit the loop
    if not ret:
        break

    # Convert the frame to a string and update the hash object
    frame_str = str(frame)
    hash_obj.update(frame_str.encode())

# Release the video capture object
cap.release()

# Get the hexadecimal representation of the hash value
hash_hex = hash_obj.hexdigest()

# Write the hash value to a file
with open('output_hash.txt', 'w') as f:
    f.write(hash_hex)
