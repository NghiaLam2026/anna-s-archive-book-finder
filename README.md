# Anna's Archive Scraper

A Python command-line tool for searching and generating download links for books from Anna's Archive. The tool allows users to search for books by title, specify the desired file format, and select a download server.

## Features

- Search for books by title on Anna's Archive
- Specify file format (PDF, EPUB, etc.)
- Select from multiple download servers
- Automatic URL encoding for special characters in book titles

## Requirements

- Python 3.6 or higher

## Installation

1. Clone or download this repository

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Dependencies

- `requests` - For making HTTP requests
- `beautifulsoup4` - For parsing HTML content
- `playwright==1.57.0` - Web automation library

## Usage

Run the script:

```bash
python main.py
```

The script will prompt you for:
1. **Book name**: Enter the title of the book you want to search for
2. **File format**: Specify the desired format (e.g., `pdf`, `epub`)
3. **Server number**: Choose a download server (1, 2, or 3)

The script will then:
- Convert your book title to a URL-encoded format
- Search Anna's Archive for matching results
- Display the first few book links found
- Generate a download link based on your server selection

## How It Works

1. The tool converts the book title to a URL-encoded format, handling spaces and special characters
2. It constructs a search URL for Anna's Archive with your specified format
3. It parses the search results page to extract book links
4. Based on your server selection, it constructs the final download link

## Notes

- The script extracts the first 3 book links from search results
- Download links are generated for Anna's Archive's slow download servers
- Make sure you have a stable internet connection when using this tool