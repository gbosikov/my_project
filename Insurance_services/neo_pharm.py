import requests
from requests.structures import CaseInsensitiveDict
import xmltodict

url = "http://sale.neopharmi.ge/aisi/aisiservice.asmx?op=getPriceList"


headers = CaseInsensitiveDict()
headers["Host"] = "sale.neopharmi.ge"
headers["Content-Type"] = "text/xml; charset='utf-8'"
headers["SOAPAction"] = "http://tempuri.org/getPriceList"



body = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getPriceList xmlns="http://tempuri.org/" />
  </soap:Body>
</soap:Envelope>"""


response = requests.post(url, headers=headers, data=body)
resp_xml = response.text
# resp_json = xmltodict.parse(resp_xml)
print(response.text)
