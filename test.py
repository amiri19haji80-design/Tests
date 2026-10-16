import os 
import pytest


print([o.key for o in s3.Bucket(e['BUCKET_RATES']).objects.filter(Prefix='DataSources/').limit(5)])


print([o.key for o in s3.Bucket(e['BUCKET_RATES']).objects.filter(Prefix='CRM/').limit(5)])
