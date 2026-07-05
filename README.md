# Stock Trading Alert Project

A Python stock alert project that checks daily stock price movement and sends a news email alert when the stock changes significantly.

This project was built using Python, APIs, environment variables, JSON data, email automation, and basic project refactoring with functions.

---

## Features

- Fetches daily stock price data from the Alpha Vantage API
- Uses a stock symbol, such as `NVDA`
- Extracts the latest and previous closing prices
- Calculates the percentage difference between two trading days
- Checks if the stock changed above a chosen percentage threshold
- Fetches related company news from NewsAPI
- Extracts the first 3 relevant news articles
- Formats article headlines and descriptions
- Sends an email alert using SMTP
- Keeps API keys and email credentials hidden using a `.env` file
- Uses functions to separate stock and news API requests

---

## What I practiced

- Working with external APIs using `requests`
- Passing API parameters with dictionaries
- Reading JSON responses from APIs
- Navigating nested dictionaries and lists
- Extracting data using dictionary keys
- Converting string numbers into `float`
- Calculating percentage change
- Using `abs()` to check movement in both directions
- Protecting secrets with environment variables
- Using `python-dotenv`
- Sending emails with `smtplib`
- Refactoring repeated logic into functions
- Writing cleaner variable names such as `STOCK_SYMBOL`, `STOCK_API_KEY`, and `NEWS_API_KEY`

---

## Project structure

```
main.py
.env
.gitignore
README.md
```

---

## How to run

First, install the required packages:

```bash
pip install requests python-dotenv
```

Create a `.env` file in the project root and add your own keys:

```env
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key
NEWS_API_KEY=your_news_api_key
MY_EMAIL=your_email@gmail.com
MY_EMAIL_PASSWORD=your_gmail_app_password
```

Run the project with:

```bash
python main.py
```

---

## Technologies used

- Python
- Requests
- Alpha Vantage API
- NewsAPI
- SMTP
- Gmail App Password
- Environment variables
- python-dotenv
- JSON

---

## Note

This project was created as part of my Python learning journey through Angela Yu’s Udemy course.

The `.env` file is used to keep API keys and email credentials private.  
It should never be uploaded to GitHub.

---

## Author

Alex — Aspiring Python developer building projects step by step through daily practice, with the long-term goal of becoming a professional software developer.