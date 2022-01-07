from bs4 import BeautifulSoup
import requests
import csv

pages = []

for i in range(1,51):
    url = f"http://books.toscrape.com/catalogue/page-{i}index.html"
    
    response = requests.get(url).text

    soup = BeautifulSoup(response,'html.parser')

    books = soup.find('ol', attrs = {'class': 'row'})

    for row in books.find_all("li"):
        
        for line in row.find_all("div", attrs = {"class":"product_price"}):
            priceFind = line.find_all("p")
            priceCheck = priceFind[1].text
            
        if priceCheck.strip() != "In Stock":
            continue
        else:
            book = {}
            
            book['title'] = row.find("h3").find("a").attrs["title"]
            book['price'] = priceFind[0].string
            book['rating'] = row.find('p').attrs['class'][1]
            book.append(pages)
        
print(pages)


keys = books[0].keys()
with open("books.csv","w",newline="",encoding="utf-8") as csvFile:
    writer = csv.DictWriter(csvFile. keys)
    writer.writeheader()
    writer.writetows(pages)
    
