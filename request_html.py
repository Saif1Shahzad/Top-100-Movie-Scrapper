import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

link = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
soup = fetch_and_parse(link)

with open("Top_100_Movies.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
