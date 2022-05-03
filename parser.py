import requests
from bs4 import BeautifulSoup
import re

#take input url
url = 'https://londongrapple.co.uk'

# define a function that sends http(s) request to url
response = requests.get(url)

#define a function that parses the html
content = BeautifulSoup(response.text, 'html.parser')

for link in content.find_all('a'):
    print(link.get('href'))
#search the parse tree for links that are not external