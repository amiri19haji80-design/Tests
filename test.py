import os 
import pytest

python -c "import boto3,os; ecs=boto3.resource('s3', endpoint_url='https://'+os.environ['ENDPOINT_RATES'], aws_access_key_id=os.environ['ACCESS_KEY_RATES'], aws_secret_access_key=os.environ['SECRET_KEY'], verify='/mnt/nfs/ssl/CA_Bundle.pem'); print('ECS OK:', [o.key for o in ecs.Bucket(os.environ['BUCKET_RATES']).objects.limit(3)])"
