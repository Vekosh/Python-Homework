import requests
import json
y = input("Выберите валюту: ").strip(" / .")
x = input("Выберите в какую валюту хотите переводить: ").strip(" / .")
amount = int(input("Введите сумму: "))
url = f"https://api.apilayer.com/fixer/convert?to={x}&from={y}&amount={amount}"

payload = {}
headers= {
  "apikey": "eBvUBFsWXaNAtUx6Uhtsr985Z0baHWZi"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
val_sum = json.loads(result)
# print(val_sum)

print(val_sum["query"], sep='\n', end='\n')
print(f"result = ", (val_sum["result"]))
# vfj