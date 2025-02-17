from flask import Flask, render_template, jsonify, request
import cv2
import face_recognition
import numpy as np
import json
from pymongo import MongoClient
from datetime import datetime
from src.utils.aws_helper import get_dynamodb_table

app = Flask(__name__)

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")  # Change if using a remote MongoDB instance
db = mongo_client["FaceAuthDB"]
auth_logs = db["AuthLogs"]

# Get the DynamoDB table
table = get_dynamodb_table("FaceEncodings")

def get_face_encoding(name):
    """Retrieve face encoding from DynamoDB"""
    response = table.get_item(Key={"name": name})
    if "Item" in response:
        return np.array(json.loads(response["Item"]["encoding"]))  # Convert back to NumPy array
    return None

known_encoding = get_face_encoding("Rohan")
if known_encoding is None:
    raise Exception("No encoding found in database!")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    """Handles face authentication and logs the attempt."""
    # Open webcam
    video_capture = cv2.VideoCapture(0)

    ret, frame = video_capture.read()
    if not ret:
        log_authentication("❌ Could not access webcam!")
        return jsonify({"message": "❌ Could not access webcam!"})

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    message = "❌ Face not matched!"
    
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([known_encoding], face_encoding)
        face_distance = face_recognition.face_distance([known_encoding], face_encoding)

        if matches[0] and face_distance[0] < 0.5:  # Confidence threshold
            message = "✅ Face Matched! Access Granted."
            break

    # Release camera resources
    video_capture.release()
    cv2.destroyAllWindows()

    # Log authentication attempt
    log_authentication(message)

    return jsonify({"message": message})

def log_authentication(message):
    """Logs the authentication attempt into MongoDB."""
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message": message
    }
    inserted_log = auth_logs.insert_one(log_entry)
    log_entry["_id"] = str(inserted_log.inserted_id)  # Convert ObjectID to string

    print(f"Logged Authentication Attempt: {log_entry}")

if __name__ == '__main__':
    app.run(debug=True)
