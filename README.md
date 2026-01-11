# Top 100 Movies Scraper

A Python web scraping project that fetches and parses Empire Online's list of the Top 100 Greatest Movies of All Time.

## 📖 Overview

This project demonstrates web scraping techniques using Python to extract movie titles from Empire Online's archived "Best Movies" article. The scraper retrieves the HTML content, parses it using BeautifulSoup, and generates a clean, numbered list of the top 100 movies.

## 🚀 Features

- **Web Scraping**: Fetches movie data from Empire Online's archived page
- **HTML Parsing**: Uses BeautifulSoup to extract movie titles from HTML
- **Data Processing**: Reverses and formats the list in correct ranking order
- **File Export**: Saves the movie list to a text file

## 🛠️ Technologies Used

- **Python 3**
- **BeautifulSoup4** - HTML parsing library
- **Requests** - HTTP library for fetching web content

## 📁 Project Structure

```
Top-100-Movie-Scrapper/
│
├── request_html.py              # Fetches HTML from the web
├── beautiful_soup_movie_parser.py  # Parses HTML and extracts movie titles
├── Top_100_Movies.html          # Downloaded HTML file
├── movie_list.txt               # Output file with ranked movies
└── README.md                    # Project documentation
```

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Top-100-Movie-Scrapper.git
   cd Top-100-Movie-Scrapper
   ```

2. **Install required packages**
   ```bash
   pip install beautifulsoup4 requests
   ```

## 💻 Usage

### Step 1: Download the HTML

Run the script to fetch the HTML content from Empire Online:

```bash
python request_html.py
```

This will download the HTML and save it as `Top_100_Movies.html`.

### Step 2: Parse and Extract Movie Titles

Run the parser to extract and format the movie list:

```bash
python beautiful_soup_movie_parser.py
```

This will create a `movie_list.txt` file with the top 100 movies in ranked order.

## 📝 Output

The generated `movie_list.txt` contains movies numbered from 1 to 100, for example:

```
1. The Godfather
2. The Shawshank Redemption
3. Pulp Fiction
...
```

## 🔍 How It Works

1. **`request_html.py`**:

   - Sends an HTTP GET request to the Empire Online archive
   - Retrieves the HTML content
   - Saves it locally as `Top_100_Movies.html`

2. **`beautiful_soup_movie_parser.py`**:
   - Reads the local HTML file
   - Uses BeautifulSoup to find all `<h3>` tags with class "title"
   - Reverses the list (since the original is in reverse order)
   - Strips ranking numbers and formats the titles
   - Writes the formatted list to `movie_list.txt`

## 🎯 Learning Outcomes

This project demonstrates:

- Web scraping with Python
- HTML parsing with BeautifulSoup
- HTTP requests handling
- File I/O operations
- Data manipulation and formatting

## ⚠️ Note

This project uses the Wayback Machine's archived version of the Empire Online article. Always respect website terms of service and robots.txt when scraping.

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

**Made with ❤️ for learning web scraping**
