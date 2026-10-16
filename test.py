import os 
import pytest


verify='/nfs/ssl/CA_Bundle.pem'
s3 = boto3.resource('s3', endpoint_url='https://'+e['ENDPOINT_RATES'], aws_access_key_id=e['ACCESS_KEY_RATES'], aws_secret_access_key=e['SECRET_KEY_S3'], verify='/nfs/ssl/CA_Bundle.pem')


print([o.key for o in s3.Bucket(e['BUCKET_RATES']).objects.filter(Prefix='DataSources/').limit(5)])

print([o.key for o in s3.Bucket(e['BUCKET_RATES']).objects.filter(Prefix='CRM/').limit(5)])
