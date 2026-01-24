from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def fetch_website_contents(url):
    """
    Return the title and contents of the website at the given url;
    truncate to 2,000 characters as a sensible limit
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    titles = []

    for level in range(1, 3):
        title_level = soup.find_all(f"h{level}")

        if len(title_level) == 0:
            continue

        title = [t.get_text() for t in title_level]
        titles.extend(title)

    link = soup.find_all("a")
    link_text = [f"{url}/{l.get('href')}" for l in link]
    link_texts = "\n".join(link_text)

    return {"titles": titles, "links": link_texts}
