import requests
response_non_spam = requests.post("https://wine-app75018.herokuapp.com/predict", json={"YearsExperience": 2})
response_non_spam.json()

response_non_spam = requests.post("https://wine-app75018.herokuapp.com/predict", json={"YearsExperience": 'a'})
response_non_spam.json()

response_non_spam = requests.post("https://wine-app75018.herokuapp.com/predict", json={"YearsExperience": [5,5]})
response_non_spam.json()