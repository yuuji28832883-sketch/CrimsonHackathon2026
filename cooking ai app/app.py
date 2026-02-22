#receives the data from js and processes it
import requests
from bs4 import BeautifulSoup

# 1. Define custom headers to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

url = 'https://www.allrecipes.com/12-vintage-casseroles-you-can-make-in-your-slow-cooker-11882709'

# 2. Make the request, passing the headers to circumvent the security block
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Successfully bypassed the blocker!oi\n")
    
    # 3. Parse the raw HTML text using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 4. Extract data by traversing the HTML hierarchy. 
    # For example, let's find the main heading (H1 tag) of the page:
    title = soup.find('h1')
    
    if title:
        print(f"Recipe Title: {title.text.strip()}")
    else:
        print("Could not find the title tag.")
        
else:
    print(f"Error: Received status code {response.status_code}")