from bs4 import BeautifulSoup

def parse_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    return soup

html_file_path = "Top_100_Movies.html"  # Replace with your local HTML file path
soup = parse_html_file(html_file_path)

# titles = soup.select("h3.title")
titles = soup.find_all("h3", class_="title") # Alternative way to find titles
titles.reverse()  # Reverse the list to get the correct order
movie_list = []
for idx, title in enumerate(titles, start=1):
    movie_list.append(f"{idx}. " + " ".join(title.get_text(strip=True).split()[1:]))  # Skip the ranking number

with open("movie_list.txt", "w", encoding="utf-8") as file:
    for movie in movie_list:
        file.write(movie + "\n")    