import os 
import pytest


cd /app && python -c "from src.api.routes.rates.settings import settings; settings.s3creds('rates'); print('BUCKET:', settings.bucket_name, '| ENDPOINT:', settings.endpoint)"
