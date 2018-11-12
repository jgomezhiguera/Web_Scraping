import requests as rq
from bs4 import BeautifulSoup
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')
page = rq.get("https://www.exito.com/browse?Ntt=0f3r7a2_d3l_d1a&No=0&Nrpp=2000")
soup = BeautifulSoup(page.content)

objectives = soup.find_all('div', {"class" : "col-xs-8 col-sm-12 col-data"})

filename = "offers.csv"
f = open(filename, "w") # You need to change 'w' to 'a' for append new results
headers = "product, brand, current_price, offer_date\n"
f.write(headers)

for objective in objectives:
    product = objective.findAll("span", {"class" : "name"})[0].text.strip()
    brand = objective.findAll("span", {"class": "brand"})[0].text.strip()
    price = objective.findAll("span", {"class": "money"})[0].text.strip()
    offer_date = datetime.now().strftime("%Y-%m-%d")

    print "Product: " + product
    print "Brand: " + brand
    print "Offer's price: " + price
    print "Offer's date: " + offer_date

    f.write(product + "," + brand + "," + price + "," + offer_date  + "\n")

f.close()
