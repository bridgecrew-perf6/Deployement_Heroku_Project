import requests

ENDPOINT = "http://127.0.0.1:5000/predict"

test_ok = requests.post(ENDPOINT, json={"year": 5})
print(test_ok, test_ok.json())

test_ok_rounded = requests.post(ENDPOINT, json={"year": 5, "rounded": "True"})
print(test_ok_rounded, test_ok_rounded.json())

test_ko_no_json = requests.post(ENDPOINT, data={"year": 5, "rounded": "True"})
print(test_ko_no_json, test_ko_no_json.json())

test_ko_missing_year = requests.post(ENDPOINT, json={"rounded": "True"})
print(test_ko_missing_year, test_ko_missing_year.json())
