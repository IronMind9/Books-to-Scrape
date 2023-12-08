import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    """
    Fetch HTML content from the specified URL.

    Args:
    - url (str): The URL to fetch HTML content from.

    Returns:
    - bytes: The HTML content as bytes if successful, else None.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

def extract_book_info(book):
    """
    Extract book information from a BeautifulSoup book element.

    Args:
    - book (Tag): BeautifulSoup book element.

    Returns:
    - str: Formatted book information.
    """
    name = book.h3.a["title"]
    rating = book.select_one("p[class*='star-rating']")['class'][1]
    price = book.select_one(".price_color").text
    return f"The book title is: {name}, has a rating: {rating}, and the price is: {price}"

def main():
    """
    Main function to fetch HTML content, parse it, and print book information.
    """
    url = "https://books.toscrape.com/"
    html_content = get_html_content(url)

    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        books = soup.find_all("article")

        for book in books:
            book_info = extract_book_info(book)
            print(book_info)

if __name__ == "__main__":
    main()
