# God's Eye

## Project Description
This project is a custom search engine built using Flask and the Google Custom Search API. It allows users to perform searches and displays results in a user-friendly format. The search engine is designed to be simple and efficient, providing relevant search results based on user queries.

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)

## Features
- Customizable search parameters (API key, search engine ID)
- Displays search results with titles, links, and snippets
- Results are stored and ranked for improved relevance
- Responsive design for mobile and desktop users

## Technologies Used
- **Flask**: A lightweight WSGI web application framework in Python.
- **Pandas**: For storing and manipulating search results.
- **Requests**: For making HTTP requests to the Google Custom Search API.
- **HTML/CSS**: For creating the user interface.

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/PrinceOdein/Eye-of-God.git
   cd Eye-of-God
   
2. Install the required dependencies:
    ```bash
    pip install Flask requests pandas

3. Update the settings.py file with your Google API key and search engine ID.

## Usage
1. Run the application:
   ```bash
    python app.py
2. Open your web browser and navigate to http://127.0.0.1:5000/.
3. Enter your search query in the search box and click "Search" to view results.
