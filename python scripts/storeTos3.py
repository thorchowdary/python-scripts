import boto3
import os
from botocore.exceptions import ClientError
session = boto3.Session(
    aws_access_key_id="AKIARPN7B4NBXMGYACO2",
    aws_secret_access_key="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",
)

def upload_file_to_s3(file_name, bucket, object_name=None, folder_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name.split('/')[-1]
        # If folder_name was specified, upload in the folder
        if folder_name is not None:
            object_name = f'{folder_name}/{object_name}'

    # Upload the file
    try:
        s3_client = boto3.client(
            service_name='s3'
        )
        response = s3_client.upload_file(file_name, bucket, object_name)
        print(response)
    except ClientError as e:
        print(e)
        
file = os.__file__
upload_file_to_s3("aws documentation/vpc/vpc-workflow.png","dev-thors3bucket","","python")