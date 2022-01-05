from bs4 import BeautifulSoup
import requests

def getHTML(url):
    response = requests.get(url)
    return response.text

html = getHTML("http://books.toscrape.com/")

soup = BeautifulSoup(html,'html.parser')