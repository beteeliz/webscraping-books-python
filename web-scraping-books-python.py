import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/catalogue/page-1.html"

response = requests.get(url)
response.raise_for_status()  # Ensure the request worked
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

book_list = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip()
    availability = book.find("p", class_="instock availability").text.strip()

    book_list.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

df = pd.DataFrame(book_list)
df.to_csv("books.csv", index=False)

print("Data saved successfully - books.csv")