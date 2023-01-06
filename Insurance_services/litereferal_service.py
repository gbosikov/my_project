# -*- encoding: utf-8 -*-
import time
from time import sleep
import requests as rq
import xmltodict
import sys
import os


argv = input(f'Please enter direction number and pharmacy name\n'
             f'Example: 4321371, aversi\n')


def send_reqvest(argv):
    url = 'http://172.22.31.76:5050/litereferralget.asmx/GetLiteReferral'
    pharm_list = {
        'aversi': '0000037',
        'gepa': '0192863',
        'psp': '0192092'
    }

    send_dict_params = {}
    clear_input_list = argv.split(',')
    if len(clear_input_list) == 2:
        innum = clear_input_list[0].replace(' ', '')
        bkextid = clear_input_list[1].replace(' ', '')
        send_dict_params.setdefault('RSID', innum)
        send_dict_params.setdefault('PERSONALID', '')
        send_dict_params.setdefault('BKEXTID', pharm_list.get(bkextid))

    resp_obj = rq.get(url, params=send_dict_params)
    resp_xml = resp_obj.text
    resp_json = xmltodict.parse(resp_xml)
    return resp_json


def parser(some_dict: dict):
    in_dict_keys = some_dict.get('LiteInsurance')
    clean_dict_innum = in_dict_keys.get('Referral')
    error = clean_dict_innum.get('ErrorCode')
    innum = clean_dict_innum.get('Refnum')
    card = clean_dict_innum.get('Polnum')
    period = clean_dict_innum.get('Period')
    name = clean_dict_innum.get('Name')
    sur_name = clean_dict_innum.get('SurName')
    personal_id = clean_dict_innum.get('PersonalID')
    servid = clean_dict_innum.get('Servid')
    serv_name = clean_dict_innum.get('ServName')
    serv_count = clean_dict_innum.get('ServCount')
    if int(error) != 0:
        out = f'Nothing found {error}'
    else:
        out = f'Error code: {error}\n' \
           f'Direction: {innum}\n' \
           f'Card number: {card}\n' \
           f'Period: {period}\n' \
           f'Insured Name and Surname: {name} {sur_name}\n' \
           f'Insured ID card: {personal_id}\n' \
           f'Drug code: {servid}\n' \
           f'Drug name: {serv_name}\n' \
           f'Drag count: {serv_count}'
    return out


print(parser(send_reqvest(argv)))
input('Press ENTER to exit')
