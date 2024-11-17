import requests
import random

from bs4 import BeautifulSoup

url = "https://pixelford.com/blog/"
random_number = random.randint(1,999999999)

response = requests.get(url, headers = {'user-agent': 'random_number'}) #request content from the URL using a random 'user-agent', to avoid being blocked by the website

html = response.content

soup = BeautifulSoup (html, 'html.parser')

a_tags = soup.find_all('a', class_="entry-title-link")
#print(a_tags)

# for a_tag in a_tags:
#     print (a_tag.get_text())

titles = list(map(lambda a_tag: a_tag.get_text(), a_tags))

print(titles)