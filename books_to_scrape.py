import requests 
from bs4 import BeautifulSoup 

response = requests.get("https://books.toscrape.com/") 

soup =BeautifulSoup( response.content , "html.parser")

books = soup.find_all("article")

for book in books :
    name = book.h3.a["title"]
    rating = book.p["class"][1]
    price = book.select_one(".price_color").text
    
    print("The book title is : " + name + " has a raiting : " + rating + " star " + "and price is : " + price ) 