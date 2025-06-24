import urllib.request
import urllib.error
import ssl
from bs4 import BeautifulSoup

# Create SSL context to ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch_html(url):
    """Fetches HTML content from the given URL with SSL context."""
    try:
        response = urllib.request.urlopen(url, context=ctx)
        return response.read()
    except Exception as e:
        print(f'Error fetching URL: {url}\n{e}')
        return None

def get_link_at_position(url, position):
    """Returns the href at the given position from the anchor tags."""
    html = fetch_html(url)
    if html is None:
        return None

    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    if position <= 0 or position > len(tags):
        print(f'Invalid position: {position}. Found only {len(tags)} links.')
        return None

    selected_tag = tags[position - 1]
    href = selected_tag.get('href', None)
    print(f'Retrieving: {href}')
    return href

def main():
    url = input('Enter URL: ').strip()
    try:
        repeat_count = int(input('Enter count: ').strip() or 0)
    except ValueError:
        repeat_count = 0

    try:
        position = int(input('Enter position: ').strip() or 1)
    except ValueError:
        position = 1

    if repeat_count == 0:
        print('** No count specified. Only the initial URL will be fetched.')
    if position <= 0:
        print('** Invalid position. Using default position 1.')
        position = 1

    print(f'Retrieving: {url}')
    current_url = url
    for _ in range(repeat_count):
        next_url = get_link_at_position(current_url, position)
        if not next_url:
            break
        current_url = next_url

if __name__ == '__main__':
    main()
