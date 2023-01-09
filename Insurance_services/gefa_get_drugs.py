import requests
from requests.structures import CaseInsensitiveDict
import xml.dom.minidom
import mysql.connector


GEPA_URL = "http://10.188.55.10/alpha.asmx/saqonelis_reestri"


def gepa_drugs(url: str):
    """
    send request to url and creates xml file with response data
    :param url:
    :return:
    """
    headers = CaseInsensitiveDict()
    headers["Host"] = "192.168.0.237"
    headers["Content-Type"] = "application/soap+xml; charset=utf-8"
    headers["Content-Length"] = "length"
    headers["user"] = 'alpha241'
    headers["password"] = '4522558'
    # body = """<?xml version="1.0" encoding="utf-8"?>
    # <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
    #   <soap12:Body>
    #     <GetAllMedFromAllDrugForInsurances xmlns="http://tempuri.org/" />
    #   </soap12:Body>
    # </soap12:Envelope>"""
    # response = requests.post(GEPA_URL, headers=headers, data=body)
    # resp_xml = response.content
    # with open("gepa_response.xml", "wb") as f:
    #     f.write(resp_xml)
    #     f.close()
    return print(headers)

print(gepa_drugs(GEPA_URL))