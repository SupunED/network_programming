import aiohttp
import asyncio
import time

urls = [
    "http://quotes.toscrape.com",
    "http://books.toscrape.com",
    "http://olympus.realpython.org/profiles/dionysus",
]

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
        for url, data in zip(urls, results):
            print(f"Fetched {url}: {data}")
            
    print(f"\nTotal time taken (Non-Blocking):{time.time() - start_time:.2f} seconds")
    
asyncio.run(main())