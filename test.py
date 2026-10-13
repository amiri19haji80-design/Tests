import os 
import pytest


curl.exe -s -o rates_test.zip -w "HTTP %{http_code}  size %{size_download}`n" -H "Authorization: Bearer HIS_TOKEN" "https://api.qdi.cib.echonet/rates/new/?cols=request_date,is_eScope,booking_system_name,response_type&sdate=20260201&edate=20260227"
