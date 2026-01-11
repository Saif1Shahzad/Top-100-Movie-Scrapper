# Top 100 Movies Scraper

A Python web scraping project that automatically fetches and organizes Empire Online's list of the Top 100 Greatest Movies of All Time.

---

## 📖 What Does This Project Do?

**In Simple Terms:** This project is an automated movie list creator. It:
1. **Downloads** a webpage with a list of the top 100 movies
2. **Extracts** the movie titles from that webpage
3. **Organizes** them in the correct ranking order (1-100)
4. **Saves** the final list to a text file that you can read and share

Think of it as automating the task of manually copying a movie list from a website into a text file.

---

## ✅ Requirements

### System Requirements
- **Operating System**: Windows, Mac, or Linux
- **Python**: Version 3.6 or higher
  - Check if you have Python: Open Command Prompt/Terminal and type `python --version`

### Python Libraries Needed
These are tools Python uses to help with specific tasks:
- **requests** - Downloads webpages from the internet
- **beautifulsoup4** - Reads and extracts information from webpages

---

## 🚀 Features

- **Automatic Web Download**: Fetches movie data from Empire Online's archived page
- **Smart Parsing**: Extracts movie titles accurately from the webpage
- **Automatic Ranking**: Orders movies 1-100 correctly
- **Easy Output**: Saves results to a text file

---

## 🛠️ Technologies Used

- **Python 3** - Programming language
- **BeautifulSoup4** - Tool for reading webpages
- **Requests** - Tool for downloading webpages

---

## 📁 Project Structure

```
Top-100-Movie-Scrapper/
│
├── request_html.py                    # Downloads the webpage
├── beautiful_soup_movie_parser.py     # Reads and extracts movie titles
├── Top_100_Movies.html                # Downloaded webpage data
├── movie_list.txt                     # Final list of 100 movies (created after running)
├── requirements.txt                   # List of Python tools needed
└── README.md                          # This file - instructions
```

---

## 🔧 How to Set Up (Step-by-Step for Beginners)

### Step 1: Install Python
If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/)
- **Windows**: Run the installer and check "Add Python to PATH" during installation
- **Mac/Linux**: Follow the installation guide on python.org

### Step 2: Clone the Repository
Open Command Prompt or Terminal and type:
```bash
git clone https://github.com/yourusername/Top-100-Movie-Scrapper.git
cd Top-100-Movie-Scrapper
```

### Step 3: Install Required Tools
Copy and paste this into Command Prompt/Terminal:
```bash
pip install -r requirements.txt
```

This command automatically downloads and installs all the tools this project needs.

---

## 💻 How to Use (Step-by-Step)

### Step 1: Download the Movie Webpage

Open Command Prompt or Terminal, navigate to your project folder, and type:

```bash
python request_html.py
```

**What this does**: Downloads the webpage containing the movie list and saves it as `Top_100_Movies.html`

### Step 2: Extract and Rank the Movies

In the same Command Prompt/Terminal, type:

```bash
python beautiful_soup_movie_parser.py
```

**What this does**: Reads the downloaded webpage, extracts all movie titles, and saves them as a numbered list in `movie_list.txt`

### Step 3: View Your Results

Open the `movie_list.txt` file with any text editor (Notepad, Word, etc.) to see your ranked list!

---

## 📝 What the Output Looks Like

The `movie_list.txt` file will contain the movies numbered 1 to 100, for example:

```
1. The Godfather
2. The Shawshank Redemption
3. Pulp Fiction
4. The Godfather Part II
5. The Dark Knight
...
100. Singin' in the Rain
```

---

## ❓ Troubleshooting (Common Problems)

### Problem: "Python not found" or "command not recognized"
**Solution**: Python isn't in your PATH. Reinstall Python and make sure to check "Add Python to PATH" during installation.

### Problem: "ModuleNotFoundError: No module named 'requests'"
**Solution**: You skipped Step 3 of setup. Run this command:
```bash
pip install -r requirements.txt
```

### Problem: The script runs but creates an empty list
**Solution**: The website might have changed. Try running both scripts again, or check if the website is still available.

---

## 🎓 How This Project Works (For Curious Minds)

**Step 1 - Download**: The first script downloads a webpage from the internet, just like opening a website in your browser.

**Step 2 - Extract**: The second script reads that webpage and finds all the movie titles by looking for specific patterns in the page.

**Step 3 - Save**: Both scripts save their results to files so you can view them anytime.

---

## ⚠️ Important Note

This project uses the Wayback Machine's archived version of the Empire Online article. Always be respectful when scraping websites and check their terms of service.

---

## 📄 License

This project is open source and available for educational purposes.

---

## 🤝 Contributing

Found a bug or have ideas to improve this? Feel free to fork this project and submit a pull request!

---

## 📧 Questions or Issues?

If you encounter any problems, please open an issue on GitHub or contact the project maintainer.

---

**Made with ❤️ for learning web scraping**
