

import requests
from bs4 import BeautifulSoup
#Import libraries;requests so python can send HTTP requests
#Import BeautifulSoup to be able to search through raw HTML

url = "https://webscraper.io/test-sites/pagination"
r = requests.get(url)
# print("status code:", r.status_code)
# Storing target website into a variable url
# requests sends the request to download the webpage content and saves the response in the variable r
# print the status code to get the accessibility permission of the website

soup = BeautifulSoup(r.text,"html.parser")
print(soup.prettify()) 
#covert the raw HTML into a structured readable HTML tree using built in HTML parser

# cards = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
# print(len(cards))
# print(cards)
#looks for all the div tags in the html tree with the class provided.

car_categories = soup.find_all("li", class_ = "nav-item")
# print(len(car_category))
# print(car_category)
#listing all the navigation items in the left 
# look for li tags in the entire HTML tree that have the class we gave
for category in car_categories:
    car_brd = category.find("span")
    if car_brd:
        car_brand = car_brd.text.strip()
        print (car_brand)



