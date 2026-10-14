
import requests
from bs4 import BeautifulSoup
#Import libraries;requests so python can send HTTP requests
#Import BeautifulSoup to be able to search through raw HTML

url = "https://webscraper.io/test-sites/pagination"
r = requests.get(url)
print("status code:", r.status_code)
# Storing target website into a variable url
# requests sends the request to download the webpage content and saves the response in the variable r
# print the status code to get the accessibility permission of the website

soup = BeautifulSoup(r.text,"html.parser")
print(soup) 
#covert the raw HTML into a structured readable HTML tree using built in HTML parser