import requests
from requests.structures import CaseInsensitiveDict
import xml.dom.minidom
import mysql.connector


AVERSI_URL = "http://185.69.172.34/ForInsuranceCompanies/ForInsuranceCompanies.asmx?op=GetAllMedFromAllDrugForInsurances"


def aversi_drugs(url: str):
    """
    send request to url and creates xml file with response data
    :param url:
    :return:
    """
    headers = CaseInsensitiveDict()
    headers["Host"] = "185.69.172.34"
    headers["Content-Type"] = "application/soap+xml; charset=utf-8"
    headers["Content-Length"] = "10000"
    body = """<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <GetAllMedFromAllDrugForInsurances xmlns="http://tempuri.org/" />
      </soap12:Body>
    </soap12:Envelope>"""
    response = requests.post(AVERSI_URL, headers=headers, data=body)
    resp_xml = response.content
    with open("aversi_response.xml", "wb") as f:
        f.write(resp_xml)
        f.close()
        return response.status_code

print(aversi_drugs(AVERSI_URL))


def db_create(db_name: str):
    mydb = mysql.connector.connect(
        host='localhost',
        user='admin',
        password='4dmirq3J',
        charset='utf-8'
    )

    mycursor = mydb.cursor()
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")


print(db_create('serv_db'))


def table_create(database: str, t_name: str):
    mydb = mysql.connector.connect(
        host='localhost',
        user='admin',
        password='4dmirq3J',
        database=database
    )
    mycursor = mydb.cursor()
    mycursor.execute(f'CREATE TABLE IF NOT EXISTS {t_name} '
                     f'(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                     f'med_name VARCHAR(255),'
                     f'fact_name VARCHAR(255),'
                     f'con_name VARCHAR(255),'
                     f'gen_name VARCHAR(255),'
                     f'cod_mat INT,'
                     f'cod_qvek FLOAT,'
                     f'cod_gac INT,'
                     f'cod_vat VARCHAR(255),'
                     f'price_gel_vat FLOAT,'
                     f'unit_price_vat FLOAT,'
                     f'price_gel FLOAT,'
                     f'unit_price_gel FLOAT,'
                     f'med_namep VARCHAR(255),'
                     f'dosage VARCHAR(255),'
                     f'numerus FLOAT,'
                     f'calc_numerus INT,'
                     f'form VARCHAR(255),'
                     f'geo_gen_name VARCHAR(255),'
                     f'cod_med VARCHAR(255),'
                     f'fact_id INT,'
                     f'med_name_eng VARCHAR(255))')


print(table_create('serv_db', 'aversi_drugs'))


def aversi_drugs_ins():
    mydb = mysql.connector.connect(
        host='localhost',
        user='admin',
        password='4dmirq3J',
        database='serv_db'
    )
    mycursor = mydb.cursor()

    domtree = xml.dom.minidom.parse('aversi_response.xml')
    group = domtree.documentElement
    medicaments = group.getElementsByTagName('Medicaments')

    for medicament in medicaments:
        med_id = medicament.getAttribute("diffgr:id")
        try:
            med_name = medicament.getElementsByTagName('MedName')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            med_name = 'NULL'
        try:
            fact_name = medicament.getElementsByTagName('FactName')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            fact_name = 'NULL'
        try:
            con_name = medicament.getElementsByTagName('ConName')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            con_name = 'NULL'
        try:
            gen_name = medicament.getElementsByTagName('GenName')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            gen_name = 'NULL'
        try:
            cod_mat = medicament.getElementsByTagName('COD_MAT')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            cod_mat = 'NULL'
        try:
            cod_qvek = medicament.getElementsByTagName('COD_QVEK')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            cod_qvek = 'NULL'
        try:
            cod_gac = medicament.getElementsByTagName('COD_GAC')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            cod_gac = 'NULL'
        try:
            cod_vat = medicament.getElementsByTagName('COD_VAT')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            cod_vat = 'NULL'
        try:
            price_gel_vat = medicament.getElementsByTagName('PriceGEL_VAT')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            price_gel_vat = 'NULL'
        try:
            unit_price_vat = medicament.getElementsByTagName('UnitPriceGEL_VAT')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            unit_price_vat = 'NULL'
        try:
            price_gel = medicament.getElementsByTagName('PriceGEL')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            price_gel = 'NULL'
        try:
            unit_price_gel = medicament.getElementsByTagName('UnitPriceGEL')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            unit_price_gel = 'NULL'
        try:
            med_namep = medicament.getElementsByTagName('MedNameP')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            med_namep = 'NULL'
        try:
            dosage = medicament.getElementsByTagName('Dosage')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            dosage = 'NULL'
        try:
            numerus = medicament.getElementsByTagName('Numerus')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            numerus = 'NULL'
        try:
            calc_numerus = medicament.getElementsByTagName('CalcNumerus')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            calc_numerus = 'NULL'
        try:
            form = medicament.getElementsByTagName('Form')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            form = 'NULL'
        try:
            geo_gen_name = medicament.getElementsByTagName('GeoGenName')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            geo_gen_name = 'NULL'
        try:
            cod_med = medicament.getElementsByTagName('COD_MED')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            cod_med = 'NULL'
        try:
            fact_id = medicament.getElementsByTagName('FactID')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            fact_id = 'NULL'
        try:
            med_name_eng = medicament.getElementsByTagName('MedNameEng')[0].childNodes[0].nodeValue.replace('"', '')
        except IndexError:
            med_name_eng = 'NULL'

        mycursor.execute('INSERT INTO aversi_drugs  VALUES ('
                         f'{int(med_id[11:])},'
                         f'"{med_name}",'
                         f'"{fact_name}",'
                         f'"{con_name}",'
                         f'"{gen_name}",'
                         f'{cod_mat},'
                         f'{cod_qvek},'
                         f'{cod_gac},'
                         f'"{cod_vat}",'
                         f'{price_gel_vat},'
                         f'{unit_price_vat},'
                         f'{price_gel},'
                         f'{unit_price_gel},'
                         f'"{med_namep}",'
                         f'"{dosage}",'
                         f'{numerus},'
                         f'{calc_numerus},'
                         f'"{form}",'
                         f'"{geo_gen_name}",'
                         f'"{cod_med}",'
                         f'{fact_id},'
                         f'"{med_name_eng}")')
        mydb.commit()

print(aversi_drugs_ins())
