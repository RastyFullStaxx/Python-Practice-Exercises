import requests
from bs4 import BeautifulSoup

url = 'https://example-news-site.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

article_titles = []
for article in soup.find_all('article'):
    title = article.find('h2').text
    article_titles.append(title)

print(article_titles)
