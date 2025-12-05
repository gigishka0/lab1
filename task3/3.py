import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

today = datetime(2025, 12, 3)
dates = [(today - timedelta(days=i)).strftime("%Y%m%d") for i in range(1, 8)]
dates.reverse()

x = []
y = []

for d in dates:
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={d}&json"
    data = requests.get(url).json()
    zar = next((item for item in data if item["cc"] == "ZAR"), None)
    if zar:
        x.append(zar["exchangedate"])
        y.append(zar["rate"])

plt.plot(x, y)
plt.xlabel("Дата")
plt.ylabel("Курс ZAR (UAH)")
plt.title("Курс південноафриканського ранду")

plt.xticks(x, fontsize=8)

plt.show()
