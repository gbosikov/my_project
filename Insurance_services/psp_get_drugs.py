import requests
from requests.structures import CaseInsensitiveDict
import xmltodict

url = "http://services.psp.ge/webservice/price.webservice.php"


headers = CaseInsensitiveDict()
headers["Host"] = "185.69.172.34"
headers["Content-Type"] = "text/xml; charset='utf-8'"
headers["SOAPAction"] = "http://tempuri.org/get_products"



body = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <GetAllMedFromAllDrugForInsurances xmlns="http://tempuri.org/" />
  </soap12:Body>
</soap12:Envelope>"""


response = requests.post(url, headers=headers, data=body)
resp_xml = response.text
# resp_json = xmltodict.parse(resp_xml)
print(response.status_code)
