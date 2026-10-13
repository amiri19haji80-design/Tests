import os 
import pytest


sed -i 's/^\(\s*\)s3_connection = SuperS3Custom(/\1settings.s3creds("rates")\n\1s3_connection = SuperS3Custom(/' /app/src/api/routes/rates/rates.py
