import requests
from requests.structures import CaseInsensitiveDict
import xml.dom.minidom
import mysql.connector


GEPA_URL = " http://172.22.31.78:6061/LiteReferralGet.asmx/GetLiteReferral"



data = {
    'RSID': '4443371',
    'PERSONALID': '',
    'CID': '',
    'BKEXTID': '0000037'
}

r = requests.post(url=GEPA_URL, data=data)

responce = r.text
print(responce)
