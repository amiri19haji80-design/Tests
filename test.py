import os 
import env 
import test 


B='UK_PRD_S3_uk-prod-s3-v2-gca-rates-d' A='user_uk-prod-s3-v2-gca-rates-d_rw' python3 -c "import os,glob,boto3,urllib3;urllib3.disable_warnings();e=os.environ;ca=(glob.glob('/mnt/nfs/ssl/CA_Bundle.pem')+glob.glob('/nfs/ssl/CA_Bundle.pem')+[False])[0];b=boto3.resource('s3',endpoint_url='https://'+e['ENDPOINT_RATES'],aws_access_key_id=e['A'],aws_secret_access_key=e['SECRET_KEY'],verify=ca).Bucket(e['B']);[print(p,[o.key for o in b.objects.filter(Prefix=p).limit(5)]) for p in ('DataSources/','CRM/')]"
