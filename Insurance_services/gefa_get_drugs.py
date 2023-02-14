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

    response = requests.post(GEPA_URL, headers=headers)
    resp_xml = response.content
    # with open("gepa_response.xml", "wb") as f:
    #     f.write(resp_xml)
    #     f.close()
    return response.status_code


print(gepa_drugs(GEPA_URL))