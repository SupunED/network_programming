import requests
import time

urls = [
    "http://quotes.toscrape.com",
    "http://books.toscrape.com",
    "http://olympus.realpython.org/profiles/dionysus",
]

for url in urls:
    start_time = time.time()
    response = requests.get(url)
    
    print(f"\nTotal time taken (Blocking):{time.time() - start_time:.2f} seconds")
     
    if response.status_code == 200:
        try :
            data = response.json()
            print("Title:",data.get("title","No Title Found"))
            
        except requests.exceptions.JSONDecodeError:
            print("Error: Response is not in JSON format")
            print(response.headers)
    else:
        print(f"Error {response.status_code}: {response.text}")
        