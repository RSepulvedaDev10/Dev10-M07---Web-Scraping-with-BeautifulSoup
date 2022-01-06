from bs4 import BeautifulSoup
import requests
import csv

def getHTML(url):
    response = requests.get(url)
    return response.text

html = getHTML("http://books.toscrape.com/")

soup = BeautifulSoup(html,'lxml')

table = soup.find()

books = []

with open("books.csv","w",newline="",encoding="utf-8") as file:

    writer = csv.writer(file)
    writer.writerow(books[0].__dict__)
    for x in range(0,len(books)):
        writer.writerow(books[x].__dict__.values())