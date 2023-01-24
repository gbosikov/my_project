import xml.dom.minidom
from aversi_get_drugs import *


PSP_URL = "http://services.psp.ge/webservice/price.webservice.php"
DB_NAME = 'serv_db'


def take_psp_drugs(url: str):
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


def create_psp_table():
    send_db_query(f'CREATE TABLE IF NOT EXISTS psp_drugs'
                     f'(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                     f'product_code INT,'
                     f'manufacturer_code INT,'
                     f'price FLOAT,'
                     f'discount FLOAT,'
                     f'product_name VARCHAR(255),'
                     f'manufacturer_name VARCHAR(255),'
                     f'category INT,'
                     f'updated DATETIME,'
                     f'special_name VARCHAR(255),'
                     f'p_ron INT,'
                     f'units INT,'
                     f'dosage VARCHAR(255),'
                     f'brandname VARCHAR(255),'
                     f'forma VARCHAR(255),'
                     f'catst INT)')


def psp_drugs_ins():
    domtree = xml.dom.minidom.parse('psp_response.xml')
    group = domtree.documentElement
    medicaments = group.getElementsByTagName('product')
    med_id = 0

    for medicament in medicaments:
        med_id += 1
        try:
            product_code = medicament.getElementsByTagName('productCode')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            product_code = 'NULL'
        try:
            manufacturer_code = medicament.getElementsByTagName('manufacturerCode')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            manufacturer_code = 'NULL'
        try:
            price = medicament.getElementsByTagName('price')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            price = 'NULL'
        try:
            discount = medicament.getElementsByTagName('discount')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            discount = 'NULL'
        try:
            product_name = medicament.getElementsByTagName('productName')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            product_name = 'NULL'
        try:
            manufacturer_name = medicament.getElementsByTagName('manufacturerName')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            manufacturer_name = 'NULL'
        try:
            category = medicament.getElementsByTagName('category')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            category = 'NULL'
        try:
            updated = medicament.getElementsByTagName('updated')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            updated = 'NULL'
        try:
            special_name = medicament.getElementsByTagName('specialName')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            special_name = 'NULL'
        try:
            p_ron = medicament.getElementsByTagName('p_ron')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            p_ron = 'NULL'
        try:
            units = medicament.getElementsByTagName('units')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            units = 'NULL'
        try:
            dosage = medicament.getElementsByTagName('dosage')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            dosage = 'NULL'
        try:
            brandname = medicament.getElementsByTagName('brandname')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            brandname = 'NULL'
        try:
            forma = medicament.getElementsByTagName('forma')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            forma = 'NULL'
        try:
            catst = medicament.getElementsByTagName('catst')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            catst = 'NULL'

        send_db_query(f'INSERT INTO psp_drugs ('
                      f'product_code,'
                      f'manufacturer_code,'
                      f'price,'
                      f'discount,'
                      f'product_name,'
                      f'manufacturer_name,'
                      f'category,'
                      f'updated,'
                      f'special_name,'
                      f'p_ron,'
                      f'units,'
                      f'dosage,'
                      f'brandname,'
                      f'forma,'
                      f'catst) VALUES ('
                      f'{product_code},'
                      f'{manufacturer_code},'
                      f'{price},'
                      f'{discount},'
                      f'"{product_name}",'
                      f'"{manufacturer_name}",'
                      f'{category},'
                      f'"{updated}",'
                      f'"{special_name}",'
                      f'{p_ron},'
                      f'{units},'
                      f'"{dosage}",'
                      f'"{brandname}",'
                      f'"{forma}",'
                      f'{catst})')


print(take_psp_drugs(PSP_URL))
print(create_psp_table())
print(psp_drugs_ins())

print(take_aversi_drugs(AVERSI_URL))
print(create_aversi_table())
print(aversi_drugs_ins())
