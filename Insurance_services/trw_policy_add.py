import requests
from requests.structures import CaseInsensitiveDict

url = "http://172.22.31.76:7575/api/values/SendJson"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Basic 5B98EBA5-83BD-402C-BE67-ED7E617A3DFB"
headers["Content-Type"] = "application/json; charset=utf-8"



data = """
{
   "user_fields":{
      "user":"Alpha_Web",
      "pass":"0063B9111ED7C97F4D7CF74CC4556241"
   },
   "polcont_fields":{
      "contnum":"",
      "departure":"07-11-2022",
      "return":"14-11-2022",
      "policy_type":"105317",
      "type":"TRW",
      "custisben":1,
      "person_fields":{
         "country":"GEO",
         "national_id":"01001062395",
         "First_name_Ge":"TEXT",
         "Last_name_Ge":" TEXT",
         "First_name_En":" TEXT",
         "Last_name_En":" TEXT",
         "birth_date":"24-04-1991",
         "sex":"flmale",
         "address":"TEXT 73",
         "email":"test@mail.com",
         "phone":"595555666",
         "passport_id":"AB123457"
      }
   },
   "policy_fields":[
      {
         "departure":"07-11-2022",
         "return":"14-11-2022",
         "limit": 8,
         "country":"GEO",
         "policy_Cusrency":"EUR",
         "price_Curency":"GEL",
         "policy_type":"105317",
         "CountryOfTravel1":"AL",
         "CountryOfTravel2":"DZ",
         "CountryOfTravel3":"AD",
         "MultiPolicy":"YES",
         "AdditionalBbenefits":1,
         "LuggageDelay":0,
         "LossOfLuggage":1,
         "FlightDelay":1,
         "SourceCountry":"AU",
         "Program1":1,
         "Program2":0,
         "Program3":1,
         "Program4":0,
		 "PoliticallyExposedPerson": "კი",
		 "Question1": "კი",
		 "Question1_text": "test1",
		 "Question2": "კი",
		 "Question2_text": "test2",
		 "Question3": "კი",
		 "Question3_text": "test3",
		 "Question4": "კი",
		 "Question4_text": "test4",
		 "Question5": "კი",
		 "Question5_text": "test5",
		 "Question6": "კი",
		 "Question6_text": "test6",
		 "Question7": "კი",
		 "Question7_text": "test7",
		 "Question8": "კი",
		 "Question8_text": "test8",
		 "Question9": "კი",
		 "Question9_text": "test9",
		 "Question10": "კი",
		 "Question10_text": "test10",
		 "Question11": "კი",
		 "Question11_text": "test11",
		 "Question12": "კი",
		 "Question12_text": "test12",
		 "Question13": "კი",
		 "Question13_text": "test13",
         "owner_fields":{
            "country":"GEO",
            "national_id":"01001062395",
            "First_name_Ge":" TEXT",
            "Last_name_Ge":" TEXT",
            "First_name_En":" TEXT",
            "Last_name_En":" TEXT",
            "birth_date":"09-04-1972",
            "sex":"flmale",
            "address":"TEST 25",
            "email":"test5522@example.com",
            "phone":"555777300",
            "passport_id":"AB123457"
         }
      }],
   "img_fields":{
      "img_name":"",
      "img_data":""
   }
}
"""

resp = requests.post(url, headers=headers, data=data.encode('utf-8'))

print(resp.text)

