import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books(url):
    products = []

    while url:
        print(f"Scraping: {url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all products on the page
        articles = soup.find_all("article", class_="product_pod")

        for article in articles:
            name = article.h3.a['title']
            price = article.find("p", class_="price_color").text.strip()
            rating_class = article.p["class"][1]  # rating class like 'One', 'Two' etc.
            rating = convert_rating(rating_class)

            products.append({
                "Name": name,
                "Price": price,
                "Rating": rating
            })

        # Find next page URL
        next_button = soup.find("li", class_="next")
        if next_button:
            next_page = next_button.a["href"]
            url = url.rsplit('/', 1)[0] + "/" + next_page
        else:
            url = None

    return products

def convert_rating(rating_class):
    ratings_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings_map.get(rating_class, 0)

def main():
    start_url = "http://books.toscrape.com/catalogue/page-1.html"
    products = scrape_books(start_url)

    # Save to CSV
    df = pd.DataFrame(products)
    df.to_csv("books.csv", index=False)
    print(f"Saved {len(products)} books to books.csv")

if __name__ == "__main__":
    main()
