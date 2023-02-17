import requests
from requests.structures import CaseInsensitiveDict
import xml.dom.minidom
import mysql.connector


URL = 'http://eprescription.moh.gov.ge:88/ws/ws.asmx'
DB_NAME = 'serv_db'

def send_db_query(query: str):
    mydb = mysql.connector.connect(
        host='localhost',
        user='admin',
        password='4dmirq3J',
        charset='utf-8',
        database=DB_NAME
    )

    mycursor = mydb.cursor()
    mycursor.execute(query)
    mydb.commit()

    return [x for x in mycursor]

def take_gov_drugs(url: str):
    """
    send request to url and creates xml file with response data
    :param url:
    :return:
    """
    headers = CaseInsensitiveDict()
    headers["Host"] = "185.69.172.34"
    headers["Content-Type"] = "text/xml; charset=utf-8"
    headers["Content-Length"] = "10000"
    headers["SOAPAction"] = "http://tempuri.org/GetProductList"
    body = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetProductListAsJson xmlns="http://tempuri.org/">
      <UserName></UserName>
      <UserPass></UserPass>
      <SearchString></SearchString>
    </GetProductListAsJson>
  </soap:Body>
</soap:Envelope>"""
    response = requests.post(url=url, headers=headers, data=body)
    resp_xml = response.text
    with open("gov_drugs_response.xml", "w", encoding="utf-8") as f:
        f.write(resp_xml)
        f.close()
        return response.status_code




def create_gov_drugs_table():
    send_db_query(f'CREATE TABLE IF NOT EXISTS gov_drugs '
                     f'(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                     f'product_id VARCHAR(255),'
                     f'product_guid VARCHAR(255),'
                     f'geo_ndc VARCHAR(255),'
                     f'geo_trade_name VARCHAR(255),'
                     f'eng_trade_name VARCHAR(255),'
                     f'atc_code VARCHAR(255),'
                     f'product_generic VARCHAR(255),'
                     f'pharma_therapy_group VARCHAR(255),'
                     f'issuance_mode VARCHAR(255),'
                     f'other_details_geo LONGTEXT,'
                     f'other_details_eng LONGTEXT,'
                     f'api LONGTEXT,'
                     f'registration_till VARCHAR(255),'
                     f'disable_reason LONGTEXT,'
                     f'manufacturer LONGTEXT,'
                     f'intermediate_product_manufacturer VARCHAR(255),'
                     f'manufacturer_country_name VARCHAR(255),'
                     f'intermediate_product_manufacturer_countryName VARCHAR(255),'
                     f'product_status INT)')


def gov_drugs_ins():
    domtree = xml.dom.minidom.parse('gov_drugs_response.xml')
    group = domtree.documentElement
    medicaments = group.getElementsByTagName('Products')

    for medicament in medicaments:

        try:
            product_id = medicament.getElementsByTagName('ProductID')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            product_id = 'NULL'
        try:
            product_guid = medicament.getElementsByTagName('ProductGuid')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            product_guid = 'NULL'
        try:
            geo_ndc = medicament.getElementsByTagName('GeoNDC')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            geo_ndc = 'NULL'
        try:
            geo_trade_name = medicament.getElementsByTagName('GeoTradeName')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            geo_trade_name = 'NULL'
        try:
            eng_trade_name = medicament.getElementsByTagName('EngTradeName')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            eng_trade_name = 'NULL'
        try:
            atc_code = medicament.getElementsByTagName('AtcCode')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            atc_code = 'NULL'
        try:
            product_generic = medicament.getElementsByTagName('ProductGeneric')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            product_generic = 'NULL'
        try:
            pharma_therapy_group = medicament.getElementsByTagName('PharmaTherapyGroup')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            pharma_therapy_group = 'NULL'
        try:
            issuance_mode = medicament.getElementsByTagName('IssuanceMode')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            issuance_mode = 'NULL'
        try:
            other_details_geo = medicament.getElementsByTagName('OtherDetailsGeo')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            other_details_geo = 'NULL'
        try:
            other_details_eng = medicament.getElementsByTagName('OtherDetailsEng')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            other_details_eng = 'NULL'
        try:
            api = medicament.getElementsByTagName('Api')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            api = 'NULL'
        try:
            registration_till = medicament.getElementsByTagName('RegistrationTill')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            registration_till = 'NULL'
        try:
            disable_reason = medicament.getElementsByTagName('DisableReason')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            disable_reason = 'NULL'
        try:
            manufacturer = medicament.getElementsByTagName('Manufacturer')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            manufacturer = 'NULL'
        try:
            intermediate_product_manufacturer = medicament.getElementsByTagName('IntermediateProductManufacturer')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            intermediate_product_manufacturer = 'NULL'
        try:
            manufacturer_country_name = medicament.getElementsByTagName('ManufacturerCountryName')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            manufacturer_country_name = 'NULL'
        try:
            intermediate_product_manufacturer_countryName = medicament.getElementsByTagName('IntermediateProductManufacturerCountryName')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            intermediate_product_manufacturer_countryName = 'NULL'
        try:
            product_status = medicament.getElementsByTagName('Product_Status')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            product_status = 'NULL'




        send_db_query(f'INSERT INTO gov_drugs (product_id,'
                      f'product_guid,'
                      f'geo_ndc,'
                      f'geo_trade_name,'
                      f'eng_trade_name,'
                      f'atc_code,'
                      f'product_generic,'
                      f'pharma_therapy_group,'
                      f'issuance_mode,'
                      f'other_details_geo,'
                      f'other_details_eng,'
                      f'api,'
                      f'registration_till,'
                      f'disable_reason,'
                      f'manufacturer,'
                      f'intermediate_product_manufacturer,'
                      f'manufacturer_country_name,'
                      f'intermediate_product_manufacturer_countryName,'
                      f'product_status) VALUES ('
                      f'"{product_id}",'
                      f'"{product_guid}",'
                      f'"{geo_ndc}",'
                      f'"{geo_trade_name}",'
                      f'"{eng_trade_name}",'
                      f'"{atc_code}",'
                      f'"{product_generic}",'
                      f'"{pharma_therapy_group}",'
                      f'"{issuance_mode}",'
                      f'"{other_details_geo}",'
                      f'"{other_details_eng}",'
                      f'"{api}",'
                      f'"{registration_till}",'
                      f'"{disable_reason}",'
                      f'"{manufacturer}",'
                      f'"{intermediate_product_manufacturer}",'
                      f'"{manufacturer_country_name}",'
                      f'"{intermediate_product_manufacturer_countryName}",'
                      f'{product_status})')


# print(take_gov_drugs(URL))
print(create_gov_drugs_table())
print(gov_drugs_ins())
