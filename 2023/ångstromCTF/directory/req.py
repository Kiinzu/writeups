import requests
from bs4 import BeautifulSoup

for i in range(5000):
	url = f"https://directory.web.actf.co/{i}.html"
	response = requests.get(url)

	if response.status_code == 200:
		soup = BeautifulSoup(response.content, 'html.parser')
		content = soup.get_text()
		if "your flag is in another file" not in content:
			print(f"Content of {url}: {content}")
			break
		else:
			print(f"{i} doesn't have our flag")
	else:
		print(f"Failed to retrieve content of {url}")