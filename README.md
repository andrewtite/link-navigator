# Link Navigator

A simple Python script that crawls through a sequence of web pages by following a link at a specific position on each page. <br/>
This script is intended for learning purposes and demonstrates basic web scraping using `urllib` and `BeautifulSoup`.

## 📌 Features

- Navigates through links on web pages by position
- Handles SSL certificate errors gracefully
- Uses BeautifulSoup to parse and extract HTML content
- Fully customizable through user input

## 🧰 Requirements

Python 3.x is required.

Install required libraries using:

```bash
pip install -r requirements.txt
```

requirements.txt contents:

- beautifulsoup4
- soupsieve

## 🚀 How to Use

Run the script using:

python navigator.py

You’ll be prompted to enter:
- A starting URL (e.g., http://example.com)
- A count – the number of times to follow a link (e.g., 4)
- A position – which link to follow on each page (e.g., 3 for the third link)

### 💻 Example Input

Enter URL: https://py4e-data.dr-chuck.net/known_by_Harry.html

**Enter count**: 2 <br/>
**Enter position**: 3

This will:

1. Retrieve the starting page 
2. Find and follow the 3rd link on that page 
3. Repeat for the next 2 pages

### 📂 Example Output

Retrieving: http://example.com <br/>
Retrieving: http://example.com/page3 <br/>
Retrieving: http://example.com/page3/link3

## ⚠️ Notes

- Always check a website’s robots.txt before scraping.
- This script is for educational use only.
- Avoid making too many rapid requests to the same server.

## 🧑‍🎓 Educational Purpose

This project is designed for university-level learning and demonstrates how to:
- Make HTTP requests with urllib
- Handle SSL errors safely
- Parse and navigate HTML with BeautifulSoup

## 🙏 Special Thanks

**Dr. Charles Russell Severance** <br/>
Clinical Professor, University of Michigan <br/>
🔗 www.dr-chuck.com

Thank you for your engaging course material and for making web data accessible and fun to work with.

## 👤 Author

**Andrew Tite** <br/>
📧 andrewtite@gmail.com <br/>
🔗 https://github.com/andrewtite <br/>
<a href="[https://www.linkedin.com/in/YOUR_USERNAME](https://www.linkedin.com/in/andrew-tite/)" target="_blank">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn" width="18" /> https://www.linkedin.com/in/andrew-tite/
</a>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)]([https://www.linkedin.com/in/YOUR_USERNAME](https://www.linkedin.com/in/andrew-tite/))

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
