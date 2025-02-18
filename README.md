# **FaceID Web Authentication with OpenCV, AWS, Flask & MongoDB**

## **Project Overview**
FaceID-Web-Auth is a real-time face authentication system built using **OpenCV**, **Face Recognition**, **AWS S3 & DynamoDB**, and **Flask**. It allows for **secure authentication** using facial recognition, eliminating the need for passwords.

###
![ScreenShot Tool -20250217175445](https://github.com/user-attachments/assets/dea5f598-da37-4200-b806-a3a15a0094fc)
###

---

## **How We Achieved It**

1. **Face Encoding Extraction**:
   - **OpenCV** was used to capture images from the webcam.
   - **Face Recognition** library helped to extract the face encodings from captured images.
   
2. **Storing Face Data**:
   - We used **AWS S3** to store images.
   - The face encodings were stored in **AWS DynamoDB** for easy retrieval during authentication.

3. **Authentication**:
   - We implemented a Flask API (`app.py`) to handle requests.
   - When a face is detected via the webcam, we compare the live face encoding with the stored encoding using the **Face Recognition** library.
   - If a match is found, access is granted; otherwise, access is denied.
###
| ![resetImage](https://github.com/user-attachments/assets/99400396-f9be-427c-a438-ba81a07d87c7) | ![ScreenShot Tool -20250217184714](https://github.com/user-attachments/assets/ddf62647-eb41-4b3f-b108-a0ca374fa874) |
|---|---|

5. **Logging Authentication Attempts**:
   - **MongoDB** was used to log all authentication attempts with timestamps and status messages.
###
![ScreenShot Tool -20250217180129 (1)](https://github.com/user-attachments/assets/488ce325-afd2-4da5-8177-aabfa841e7b7)
###
![Screenshot from 2025-02-17 18-13-13](https://github.com/user-attachments/assets/d6c87dd7-f5d5-41be-b0d8-130f6825866e)
###
   
---

## **Directory Structure**

```bash
FaceID-Web-Auth/
├── app.py                        # Main Flask API for authentication
├── list_s3_objects.py            # List objects in the S3 bucket
├── config                        # AWS configuration files
├── requirements.txt              # Project dependencies
├── data                          # Folder to store image data
├── retrieve_face_encoding.py     # Retrieve face encodings from DynamoDB
├── env                           # Virtual environment
├── FaceIDUser_accessKeys.csv     # User access keys for S3
├── templates                     # Frontend files (HTML templates)
├── face_recognition              # Face recognition models
├── upload_image_to_s3.py         # Script to upload images to S3
├── generate_face_encoding.py    # Script to generate and store face encodings
├── src/
│   ├── authenticate.py           # Authentication logic
│   ├── store_face.py             # Store new face encodings to DynamoDB
│   ├── aws_helper.py             # AWS helper functions for DynamoDB/S3
│   └── utils/                    # Utility functions
```

---

## **🛠 Setup & Installation**

### **1. Clone the repository:**
```bash
git clone https://github.com/r0han01/faceid-auth-aws-opencv-flask.git
cd faceid-auth-aws-opencv-flask
```

### **2. Set up a virtual environment:**
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### **3. Install dependencies:**
```bash
pip install -r requirements.txt
```

### **4. Configure AWS credentials:**
- Set up AWS credentials in the **config/.env** file:
```env
AWS_REGION=your-region
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
```

### **5. Start the Flask app:**
```bash
python app.py
```

Now, visit `http://127.0.0.1:5000` in your browser to use the system.

---

## **Useful Scripts**

- **Upload Image to S3**:  
  Upload a new image to AWS S3:
  ```bash
  python upload_image_to_s3.py
  ```
###
![Screenshot from 2025-02-17 18-20-41](https://github.com/user-attachments/assets/2fb9406b-1349-4a9a-a19f-1bb6650ff5d8)
###
![ScreenShot Tool -20250217182258](https://github.com/user-attachments/assets/657cdc89-c079-4423-92aa-90be9b8b72bd)
###
  
- **Generate Face Encoding**:  
  Extract and generate face encoding from an image:
  ```bash
  python generate_face_encoding.py
  ```
###
![Screenshot from 2025-02-17 18-26-21](https://github.com/user-attachments/assets/4dcf7d92-e886-418d-9a49-31ad8d896119)
###
- **Retrieve Face Encoding**:  
  Retrieve face encoding from DynamoDB:
  ```bash
  python retrieve_face_encoding.py
  ```
###
![Screenshot from 2025-02-17 18-29-32](https://github.com/user-attachments/assets/6ac93a50-e079-4d6f-8ca4-5df3eac9f9af)
###
- **Authenticate Face**:  
  Run authentication to verify a live face with the stored encoding:
  ```bash
  python src/authenticate.py
  ```
###
![IMG_3652 jpeg (1)](https://github.com/user-attachments/assets/e0467536-10e0-40e5-947f-725d7039a1a6)
###
![Screenshot from 2025-02-17 18-40-33](https://github.com/user-attachments/assets/f8642d21-1066-48ee-a04d-4462e543ab00)
###
---

## **Configuration**
Ensure the following AWS configurations are correctly set in the `.env` file:
- `AWS_ACCESS_KEY_ID`  
- `AWS_SECRET_ACCESS_KEY`  
- `AWS_REGION`

---

## **Key Concepts**

- **Face Encoding**:  
  A numerical representation of a person's face features, used to compare faces in the system.

- **Authentication Process**:  
  The live face captured from the webcam is compared with a stored face encoding in DynamoDB, granting access if a match is found.

- **MongoDB Logging**:  
  All authentication attempts, whether successful or not, are logged into MongoDB for auditing and debugging purposes.

