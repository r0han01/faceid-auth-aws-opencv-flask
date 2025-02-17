# **FaceID Web Authentication with OpenCV, AWS, Flask & MongoDB**

## **📌 Project Overview**
FaceID-Web-Auth is a real-time face authentication system built using **OpenCV**, **Face Recognition**, **AWS S3 & DynamoDB**, and **Flask**. It allows for **secure authentication** using facial recognition, eliminating the need for passwords.

---

## **🚀 How We Achieved It**

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

4. **Logging Authentication Attempts**:
   - **MongoDB** was used to log all authentication attempts with timestamps and status messages.
   
---

## **📂 Directory Structure**

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
git clone https://github.com/yourusername/FaceID-Web-Auth.git
cd FaceID-Web-Auth
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

## **📜 Useful Scripts**

- **Upload Image to S3**:  
  Upload a new image to AWS S3:
  ```bash
  python upload_image_to_s3.py
  ```
  
- **Generate Face Encoding**:  
  Extract and generate face encoding from an image:
  ```bash
  python generate_face_encoding.py
  ```
  
- **Retrieve Face Encoding**:  
  Retrieve face encoding from DynamoDB:
  ```bash
  python retrieve_face_encoding.py
  ```

- **Authenticate Face**:  
  Run authentication to verify a live face with the stored encoding:
  ```bash
  python src/authenticate.py
  ```

---

## **⚙️ Configuration**
Ensure the following AWS configurations are correctly set in the `.env` file:
- `AWS_ACCESS_KEY_ID`  
- `AWS_SECRET_ACCESS_KEY`  
- `AWS_REGION`

---

## **💡 Key Concepts**

- **Face Encoding**:  
  A numerical representation of a person's face features, used to compare faces in the system.

- **Authentication Process**:  
  The live face captured from the webcam is compared with a stored face encoding in DynamoDB, granting access if a match is found.

- **MongoDB Logging**:  
  All authentication attempts, whether successful or not, are logged into MongoDB for auditing and debugging purposes.

