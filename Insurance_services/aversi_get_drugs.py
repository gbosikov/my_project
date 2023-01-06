import xml.dom.minidom
from xml.dom import pulldom
import requests
from requests.structures import CaseInsensitiveDict
from xml.dom import minidom
import xml.etree.ElementTree as ET
import pandas as pd


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
    headers["Content-Length"] = "length"
    body = """<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <GetAllMedFromAllDrugForInsurances xmlns="http://tempuri.org/" />
      </soap12:Body>
    </soap12:Envelope>"""
    response = requests.post(AVERSI_URL, headers=headers, data=body)
    resp_xml = response.content
    with open("response.xml", "wb", encoding='utf-8') as f:
        f.write(resp_xml)
        f.close()
        return response.status_code

# print(aversi_drugs(AVERSI_URL))


def read_xml(file_opts):
    """Return the sample XML file as a string."""
    with open('response.xml', file_opts, encoding='utf-8') as xml:
        return xml.read()


# print(read_xml('r'))
from bs4 import BeautifulSoup as bs


soup = bs(read_xml('r'), 'xml')
ns2 = soup.find_all('NewDataSet')


for x in ns2[0].find_all('Medicaments'):
    med_name_node = x.find('MedName')
    if med_name_node is not None:
        med_name = med_name_node.text
    else:
        med_name = None

    fact_name_node = x.find('FactName')
    if fact_name_node is not None:
        fact_name = fact_name_node.text
    else:
        fact_name = None

    con_name_node = x.find('ConName')
    if con_name_node is not None:
        con_name = con_name_node.text
    else:
        con_name = None

    gen_name_node = x.find('GenName')
    if gen_name_node is not None:
        gen_name = gen_name_node.text
    else:
        gen_name = None

    cod_mat_node = x.find('COD_MAT')
    if cod_mat_node is not None:
        cod_mat = cod_mat_node.text
    else:
        cod_mat = None

    cod_qvek_node = x.find('COD_QVEK')
    if cod_qvek_node is not None:
        cod_qvek = cod_qvek_node.text
    else:
        cod_qvek = None

    cod_gac_node = x.find('COD_GAC')
    if cod_gac_node is not None:
        cod_gac = cod_gac_node.text
    else:
        cod_gac = None

    cod_vat_node = x.find('COD_VAT')
    if cod_vat_node is not None:
        cod_vat = cod_vat_node.text
    else:
        cod_vat = None

    price_gel_vat_node = x.find('PriceGEL_VAT')
    if price_gel_vat_node is not None:
        price_gel_vat = price_gel_vat_node.text
    else:
        price_gel_vat = None

    unit_price_gel_vat_node = x.find('UnitPriceGEL_VAT')
    if unit_price_gel_vat_node is not None:
        unit_price_gel_vat = unit_price_gel_vat_node.text
    else:
        unit_price_gel_vat = None

    price_gel_node = x.find('PriceGEL')
    if price_gel_node is not None:
        price_gel = price_gel_node.text
    else:
        price_gel = None

    unit_price_gel_node = x.find('UnitPriceGEL')
    if unit_price_gel_node is not None:
        unit_price_gel = unit_price_gel_node.text
    else:
        unit_price_gel = None

    med_namep_node = x.find('MedNameP')
    if med_namep_node is not None:
        med_namep = med_namep_node.text
    else:
        med_namep = None

    dosage_node = x.find('Dosage')
    if dosage_node is not None:
        dosage = dosage_node.text
    else:
        dosage = None

    numerus_node = x.find('Numerus')
    if numerus_node is not None:
        numerus = numerus_node.text
    else:
        numerus = None

    calc_numerus_node = x.find('CalcNumerus')
    if calc_numerus_node is not None:
        calc_numerus = calc_numerus_node.text
    else:
        calc_numerus = None

    distributor_node = x.find('Distributor')
    if distributor_node is not None:
        distributor = distributor_node.text
    else:
        distributor = None

    geo_gen_name_node = x.find('GeoGenName')
    if geo_gen_name_node is not None:
        geo_gen_name = geo_gen_name_node.text
    else:
        geo_gen_name = None

    cod_med_node = x.find('COD_MED')
    if cod_med_node is not None:
        cod_med = cod_med_node.text
    else:
        cod_med = None

    fact_id_node = x.find('FactID')
    if fact_id_node is not None:
        fact_id = fact_id_node.text
    else:
        fact_id = None

    med_name_eng_node = x.find('MedNameEng')
    if med_name_eng_node is not None:
        med_name_eng = med_name_eng_node.text
    else:
        med_name_eng = None




    print(f'{med_name} | {fact_name} | {con_name} | {gen_name} | {cod_mat} | {cod_qvek} | {cod_gac} | {cod_vat}'
          f'| {price_gel_vat} | {unit_price_gel_vat} | {price_gel} | {unit_price_gel} | {med_namep} | {dosage} '
          f'| {numerus} | {calc_numerus} | {distributor} | {geo_gen_name} | {cod_med} | {fact_id} | {med_name_eng}')

'MedName'
'FactName'
'ConName'
'GenName'
'COD_MAT'
'COD_QVEK'
'COD_GAC'
'COD_VAT'
'PriceGEL_VAT'
'UnitPriceGEL_VAT'
'PriceGEL'
'UnitPriceGEL'
'MedNameP'
'Dosage'
'Numerus'
'CalcNumerus'
'Distributor'
'GeoGenName'
'COD_MED'
'FactID'
'MedNameEng'

def parse_etree_stdlib():
    import xml.etree.ElementTree as etree_stdlib
    xml_as_string = read_xml('r')
    tree = etree_stdlib.fromstring(xml_as_string)
    xml_etree_stdlib = tree.findall('./MedName', {})

    return xml_etree_stdlib

# print(parse_etree_stdlib())


def parse_etree_lxml():
    from lxml import etree as etree_lxml

    xml_as_bytes = read_xml('rb')
    tree = etree_lxml.fromstring(xml_as_bytes)
    xml_etree_lxml = tree.findall('MedName', {})
    return xml_etree_lxml

# print(parse_etree_stdlib())


# print(aversi_drugs(AVERSI_URL))
#
# f = open('response.xml', 'r', encoding='utf-8')



# tree = ET.parse(f)
# root = tree.getroot()


# for med_name in root.iter('MedName'):
#     print(med_name.text)

# for fact_name in root.iter('FactName'):
#     print(fact_name.text)







# dat = open('response.xml', encoding='utf-8')
# p2 = minidom.parse(dat)
# med_name = p2.getElementsByTagName('MedName')
# fact_name = p2.getElementsByTagName('FactName')
# con_name = p2.getElementsByTagName('ConName')
# gen_name = p2.getElementsByTagName('GenName')
# cod_mat = p2.getElementsByTagName('COD_MAT')
# cod_qvek = p2.getElementsByTagName('COD_QVEK')
# cod_gac = p2.getElementsByTagName('COD_GAC')
# dod_vat = p2.getElementsByTagName('COD_VAT')
# price_gel_vat = p2.getElementsByTagName('PriceGEL_VAT')
# unit_price_vat = p2.getElementsByTagName('UnitPriceGEL_VAT')
# price_gel = p2.getElementsByTagName('PriceGEL')
# unit_price_gel = p2.getElementsByTagName('UnitPriceGEL')
# med_namep = p2.getElementsByTagName('MedNameP')
# dosage = p2.getElementsByTagName('Dosage')
# numerus = p2.getElementsByTagName('Numerus')
# calc_numerus = p2.getElementsByTagName('CalcNumerus')
# distributor = p2.getElementsByTagName('Distributor')
# geo_gen_name = p2.getElementsByTagName('GeoGenName')
# cod_med = p2.getElementsByTagName('COD_MED')
# fact_id = p2.getElementsByTagName('FactID')
# med_name_eng = p2.getElementsByTagName('MedNameEng')
#
# print(med_name[0].firstChild.data)
# print(fact_name[0].firstChild.data)
# print(con_name[0].firstChild.data)
# print(gen_name[0].firstChild.data)
# print(cod_mat[0].firstChild.data)
# print(cod_qvek[0].firstChild.data)
# print(cod_gac[0].firstChild.data)
# print(dod_vat[0].firstChild.data)
# print(price_gel_vat[0].firstChild.data)
# print(unit_price_vat[0].firstChild.data)
# print(price_gel[0].firstChild.data)
# print(unit_price_gel[0].firstChild.data)
# print(med_namep[0].firstChild.data)
# print(dosage[0].firstChild.data)
# print(numerus[0].firstChild.data)
# print(calc_numerus[0].firstChild.data)
# print(distributor[0].firstChild.data)
# print(geo_gen_name[0].firstChild.data)
# print(cod_med[0].firstChild.data)
# print(fact_id[0].firstChild.data)
# print(med_name_eng[0].firstChild.data)
#
#


