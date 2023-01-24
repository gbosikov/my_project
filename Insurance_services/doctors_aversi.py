import requests
from requests.structures import CaseInsensitiveDict
import xml.dom.minidom
import mysql.connector



DOCTOR_URL = 'http://185.69.172.34/ClinicCallCenter/ClinicCallCenter.asmx'


def get_aversi_doctors(url: str):
    """
    send request to url and creates xml file with response data
    :param url:
    :return:
    """
    USERNAME = 'AlphaWebAndMobileApplication'
    PASSWORD = 'pdU3M7g6PxtVyhDnmUVpIdUEylnbLsxp'
    headers = CaseInsensitiveDict()

    headers["Content-Type"] = 'text/xml; charset="utf-8"'
    headers["Content-Length"] = "10000"
    headers["SOAPAction"] = 'http://intro.aversi.ge/GetDoctorsList'
    body = """<?xml version="1.0" encoding="UTF-8"?>
            <Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
               <Body>
                  <GetDoctorsList xmlns="http://intro.aversi.ge/">
                     <user>AlphaWebAndMobileApplication</user>
                     <passord>pdU3M7g6PxtVyhDnmUVpIdUEylnbLsxp</passord>
                  </GetDoctorsList>
               </Body>
            </Envelope>"""
    response = requests.post(url, headers=headers, data=body)
    resp_xml = response.content
    with open("doctor_response.xml", "wb") as f:
        f.write(resp_xml)
        f.close()
        return response.status_code

print(get_aversi_doctors(DOCTOR_URL))