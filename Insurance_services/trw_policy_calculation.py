import requests
from requests.structures import CaseInsensitiveDict

url = "http://172.22.31.76:6060/api/values/trwcalculation"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Basic 5B98EBA5-83BD-402C-BE67-ED7E617A3DFB"
headers["Content-Type"] = "application/json; charset=utf-8"


data = """
{
  "Policy": {
    "user": "Alpha_Web",
    "pass": "0063B9111ED7C97F4D7CF74CC4556241",
    "type": "TRW",
    "PackageID": "105317",
    "SourceCountry": "GEO",
    "departure": "07-11-2022",
    "return": "14-11-2022",
    "days": 8,
    "dateofbirth": "10-08-1990",
    "LuggageDelay": 0,
    "LossOfLuggage": 1,
    "FlightDelay": 0,
    "Program1": 1,
    "Program2": 0,
    "Program3": 0,
    "Program4": 0
  }
}
"""

resp = requests.post(url, headers=headers, data=data.encode('utf-8'))

print(resp.text)

