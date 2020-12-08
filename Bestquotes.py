import requests

url = "https://qvoca-bestquotes-v1.p.rapidapi.com/quote"

querystring = {"author":"太宰治"}

headers = {
    'x-rapidapi-key': "SIGN-UP-FOR-KEY",
    'x-rapidapi-host': "qvoca-bestquotes-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response)