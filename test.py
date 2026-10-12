import os 
import pytest


python -c "import jwt,os; t='PASTE_TOKEN_HERE'; print(jwt.get_unverified_header(t)); print(jwt.decode(t, os.environ['SECRET_KEY'], algorithms=['HS256']))"
