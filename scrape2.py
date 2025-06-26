import requests
from bs4 import BeautifulSoup
import csv
import re

def scrape_books(url):
    books = []
    
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for book in soup.select('article.product_pod'):
            title = book.h3.a.attrs['title']
            price = re.sub(r'[^\d\.]', '', book.select_one('.price_color').text.strip())
            availability = book.select_one('.availability').text.strip()
            books.append([title, price, availability])
        
        next_page = soup.select_one('.next a')
        if next_page:
            url = "https://books.toscrape.com/catalogue/" + next_page.attrs['href']
        else:
            url = None
    
    return books

def save_to_csv(books, filename='books.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Availability'])
        writer.writerows(books)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    start_url = "https://books.toscrape.com/catalogue/page-1.html"
    book_data = scrape_books(start_url)
    save_to_csv(book_data)
