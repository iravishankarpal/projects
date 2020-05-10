import requests
from bs4 import BeautifulSoup

user_input= input("enter something to search:")
print("serching..")

google_search=requests.get("https://www.google.com/search?q="+user_input)

soup=BeautifulSoup(google_search.text,'html.parser')

search_results= soup.find_all('a')
all_links= set()

for link in search_results[15:30]:
	if (link.get('href') != '#'):
		linkText="https://www.google.com/"+link.get('href')
		all_links.add(link)
		print(linkText
		
