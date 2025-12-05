import requests
from datetime import datetime, timedelta

today = datetime(2025, 12, 3)
dates = [(today - timedelta(days=i)).strftime("%Y%m%d") for i in range(1, 8)]
dates.reverse()

for d in dates:
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={d}&json"
    response = requests.get(url).json()
    zar = next((item for item in response if item["cc"] == "ZAR"), None)
    if zar:
        print(f"{zar['exchangedate']}: {zar['rate']} UAH")

