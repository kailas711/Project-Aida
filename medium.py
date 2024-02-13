import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
website = "https://medium.com/"

# Send an HTTP GET request to the website
response = requests.get(website)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

def get_medium():
    medium = " "
    for  i in soup.find_all("a")[7:35]:
        # print(i.get_text())

        medium += i.get_text() 
        medium += "      "

    return medium
