# Create a virtual environment

# py -3 -m API .venv

#pip install beautifulsoup4
#pip install Flask


#1
from bs4 import BeautifulSoup
#2
import urllib.request
#3
soup = BeautifulSoup('Extremely bold',"html.parser")
#4
tag = soup.b
#5
print(tag['class'])