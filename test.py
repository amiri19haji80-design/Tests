import os 
import env 
import test


sed -i 's/os.environ.get("BUCKET_RATES")/os.environ.get("BUCKET_STATIC")/' /app/src/api/routes/rates/data_cache.py


sed -i 's/os.environ.get("ACCESS_KEY_RATES")/os.environ.get("ACCESS_KEY_STATIC")/' /app/src/api/routes/rates/data_cache.py


sed -i 's/os.environ.get("SECRET_KEY_S3")/os.environ.get("SECRET_KEY_STATIC")/' /app/src/api/routes/rates/data_cache.py



grep -n "STATIC" /app/src/api/routes/rates/data_cache.py



