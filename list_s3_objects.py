import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Create an S3 client
s3 = boto3.client('s3')

def list_s3_objects(bucket_name):
    """Lists all objects in an S3 bucket"""
    try:
        # List objects in the S3 bucket
        response = s3.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            print(f"Objects in S3 bucket '{bucket_name}':")
            for obj in response['Contents']:
                print(f"- {obj['Key']}")
        else:
            print(f"No objects found in bucket '{bucket_name}'.")
    
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
bucket_name = 'faceiduser'  # Replace with your S3 bucket name
list_s3_objects(bucket_name)
