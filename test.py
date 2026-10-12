import os 
import pytest


python -c "import jwt,os,time; print(jwt.encode({'uid':'test','exp':int(time.time())+3600}, os.environ['SECRET_KEY'], algorithm='HS256'))"


curl.exe -s -w "`nHTTP %{http_code}`n" -H "Authorization: Bearer PASTE_TOKEN_HERE" "https://api.qdi.cib.echonet/rates/new/?sdate=20260119&edate=20260119"
