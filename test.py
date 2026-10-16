import os 
import pytest


python3 -c "import os,glob,boto3,urllib3;urllib3.disable_warnings();e=os.environ;ca=(glob.glob('/nfs/ssl/CA_Bundle.pem')+glob.glob('/mnt/*/ssl/CA_Bundle.pem')+[False])[0];print('bucket:',e['BUCKET_RATES'],'ca:',ca);b=boto3.resource('s3',endpoint_url='https://'+e['ENDPOINT_RATES'],aws_access_key_id=e['ACCESS_KEY_RATES'],aws_secret_access_key=e['SECRET_KEY_S3'],verify=ca).Bucket(e['BUCKET_RATES']);[print(p,[o.key for o in b.objects.filter(Prefix=p).limit(5)]) for p in ('DataSources/','CRM/')]"
