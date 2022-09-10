"""
Template used to initialize boto3 client
"""
from dotenv import load_dotenv
import boto3
import os


# Interaction with IAM
# 1. At IAM screen click 'Users'
# 2. Click 'Add User'
# 3. Click 'Programmatic Access'
# 4. 'Attach existing policies directly'
# 5. Give User the managed services for us:
#       AmazonS3FullAccess

s3 = boto3.client('s3',
                  region_name= 'eu-west-2'
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)