import face_recognition
import numpy as np

# Load the image file into a numpy array
image = face_recognition.load_image_file("/home/r0han/CoursePractice/PythonFrameworks/OpenCV/FaceID-Web-Auth/data/rohan.jpg")  # replace with your image file path

# Get the face encoding(s) from the image
face_encodings = face_recognition.face_encodings(image)

# If there are any faces detected, get the first one (assuming one face per image for simplicity)
if face_encodings:
    encoding = face_encodings[0]
    print("Face encoding:", encoding)
else:
    print("No faces found in the image.")
