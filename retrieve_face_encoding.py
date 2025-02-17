import boto3
import json
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Define the table name
table_name = 'FaceEncodings'
table = dynamodb.Table(table_name)

def get_face_encoding(name):
    """Retrieve face encoding data from DynamoDB."""
    try:
        # Get the item from DynamoDB
        response = table.get_item(Key={'name': name})

        if 'Item' in response:
            # Decode the JSON string back to a Python list
            encoding = json.loads(response['Item']['encoding'])
            return encoding
        else:
            print(f"❌ No encoding found for {name}")
            return None
    except NoCredentialsError:
        print("❌ No AWS credentials found!")
    except PartialCredentialsError:
        print("❌ Incomplete AWS credentials!")
    except Exception as e:
        print(f"❌ Error retrieving face encoding: {e}")
        return None

# Example usage: Retrieve face encoding for Rohan
encoding = get_face_encoding("Rohan")
if encoding:
    print(f"✅ Retrieved encoding: {encoding}")
