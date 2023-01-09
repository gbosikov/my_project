import requests
from requests.structures import CaseInsensitiveDict
import xmltodict


PSP_URL = "http://services.psp.ge/webservice/price.webservice.php"


def aversi_drugs(url: str):
    """
    send request to url and creates xml file with response data
    :param url:
    :return:
    """
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "text/xml; charset='utf-8'"
    headers["Content-Length"] = "10000"
    headers["SOAPAction"] = "http://tempuri.org/get_products"
    body = """<?xml version="1.0" encoding="UTF-8"?>
                <Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
                   <Body>
                      <get_products xmlns="http://tempuri.org/">
                         <productCode />
                         <manufacturerCode />
                         <category />
                      </get_products>
                   </Body>
                </Envelope>"""
    response = requests.post(PSP_URL, headers=headers, data=body)
    resp_xml = response.content
    with open("psp_response.xml", "wb") as f:
        f.write(resp_xml)
        f.close()
        return response.status_code


print(aversi_drugs(PSP_URL))
