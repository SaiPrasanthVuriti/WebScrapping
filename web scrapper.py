inimport requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    # Fetch the webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the page title
    title = soup.find(id='firstHeading').get_text(strip=True)
    
    # Extract the first paragraph of the main content
    first_paragraph = soup.select_one('.mw-parser-output > p').get_text(strip=True)
    
    # Extract external links
    external_links = [
        a['href'] for a in soup.select('.mw-parser-output a[href^="http"]')
        if 'wikipedia.org' not in a['href']
    ]
    
    # Extract images and their alt text
    images = [
        {
            'url': 'https:' + img['src'],
            'alt': img.get('alt', 'No alt text')
        }
        for img in soup.select('.mw-parser-output img')
    ]
    
    return {
        'title': title,
        'first_paragraph': first_paragraph,
        'external_links': external_links,
        'images': images
    }

# Example Usage
url = input()
data = scrape_wikipedia(url)
print(data)
