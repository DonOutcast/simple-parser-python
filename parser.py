import requests
from bs4 import BeautifulSoup

url = "https://edu.21-school.ru/projects/code-review"

response = requests.get(url)
# print(response.status_code)
soup = BeautifulSoup(response.text, "lxml")
# print(soup)
data = soup.find("section", {"class": "jss1431"})
print(data)
