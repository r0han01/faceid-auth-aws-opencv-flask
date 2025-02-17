import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import os

def upload_image_to_s3(image_path, bucket_name, s3_key):
    # Create S3 client
    s3 = boto3.client('s3')

    try:
        # Upload the image to S3 bucket
        s3.upload_file(image_path, bucket_name, s3_key)
        print(f"Successfully uploaded {image_path} to S3 as {s3_key}")
    except FileNotFoundError:
        print(f"File not found: {image_path}")
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Set your image path, S3 bucket name, and the desired S3 key (file name in S3)
    image_path = '/home/r0han/CoursePractice/PythonFrameworks/OpenCV/FaceID-Web-Auth/data/rohan.jpg'
    bucket_name = 'faceiduser'
    
    # Choose the S3 key (path) where you want to store the image
    s3_key = 'rohan.jpg'  # For example, store it in a folder named 'images'

    upload_image_to_s3(image_path, bucket_name, s3_key)
