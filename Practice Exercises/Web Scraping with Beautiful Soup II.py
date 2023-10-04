import requests
from bs4 import BeautifulSoup

url = "https://example.com"  # Replace with the URL of the website you want to scrape
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data from the webpage using BeautifulSoup
# Example: print the title of the page
print(soup.title.text)
