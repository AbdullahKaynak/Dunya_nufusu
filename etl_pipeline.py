import requests
import pandas as pd
from database import get_connection

pd.set_option("display.max_columns", None)  # Tüm sütunları göster
pd.set_option("display.width", 1000)  # Genişliği artır ki satırlar kaymasın

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
user_agent = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
    }

response = requests.get(url, headers=user_agent)
df = pd.read_html(response.text)[0]
print(df)

df1 = df.copy()

df1 = df1.drop(0)
df1 = df1.drop(columns="Notes")
df1["% of world"] = df1["% of world"].str.replace("%", "").astype(float) / 100
df1["Date"] = pd.to_datetime(df["Date"], format= "%d %b %Y", errors="coerce")

print(df1)


## Bağlantı
engine = get_connection()

df1.to_sql("dunya_nufusu", con=engine, if_exists="replace", index=False)
print("Veriler MySQL veriitabanına başarıyla yüklendi.")

df1.to_csv("Guncel_nufus_verisi.csv", index=False, encoding="Utf-8-sig")
print("Güncel veriler 'Guncel_nufus_verisi.csv' olarak kaydedildi")


