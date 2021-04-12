import requests
from bs4 import BeautifulSoup as bs

github_username = input('Please enter the GitHub username: ')
url = 'https://github.com/' + github_username
r = requests.get(url)
soup = bs(r.content, 'html.parser')

username_image = soup.find('img', {'alt': 'Avatar'})['src']

print(username_image)