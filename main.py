from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

headers = {
"Accept-Language": "es-419,es;q=0.9,en;q=0.8",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

my_email = "ale240307@gmail.com"
password = "ociexxtfsybphnux"

url = "https://www.amazon.com/-/es/DeWalt-DW1361-brocas-Titanio-unidades/dp/B004GIO0F8/ref=sr_1_7?qid=1674557524&s=hi&sr=1-7&th=1"
data = requests.get(url, headers= headers)

soup = BeautifulSoup(data.content, "lxml")
lista = soup.find("span", class_="a-offscreen").text
precio = lista.split("$")[1]
precio_float = float(precio)
print(precio_float)

PRECIO_JUSTO = 29

if precio_float < PRECIO_JUSTO:
    with smtplib.SMTP("smtp.gmail.com", port=587) as coneccion:
        coneccion.starttls()
        coneccion.login(user=my_email, password=password)
        coneccion.sendmail(from_addr=my_email,
                           to_addrs="ale240307@gmail.com",
                           msg=f"Subjet:precio de mechas\n\n el precio bajo mas que el objetivo es hora de comprar")






