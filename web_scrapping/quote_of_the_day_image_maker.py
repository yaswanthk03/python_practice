"""
 Challenge: Quote of the Day Image Maker

Goal:
- Scrape random quotes from https://quotes.toscrape.com/
- Extract quote text and author for the first 5 quotes
- Create an image for each quote using PIL
- Save images in 'quotes/' directory using filenames like quote_1.png, quote_2.png, etc.


"""

import os
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import textwrap

QUOTES_LINK = 'https://quotes.toscrape.com/'
SAVE_DIR = 'quotes'

def get_quotes(url):
    try:
        request = requests.get(url, timeout=10)
        request.raise_for_status()

        soup = BeautifulSoup(request.text, 'html.parser')

        quotes_tags = soup.find_all('div', class_="quote")[:5]

        quotes = []

        for tag in quotes_tags:
            quote = tag.span.text.strip("“”")
            author = tag.find('small', class_ = 'author').text

            quotes.append((quote, author))

        return quotes
    except Exception as e:
        print("Error while fetching quotes -", e)

def create_image(quote: str, author: str, idx: int):
    
    background_color = "#f8d77f"
    text_color = "#262626"

    wrapped_quote = textwrap.fill(quote, width=60)
    author_text = f"- {author}"

    width, height = 800, 300

    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 20)
    author_font = ImageFont.truetype("arial.ttf", 15)

    y_text = 50
    draw.text((40, y_text), wrapped_quote, font=font, fill=text_color)
    y_text += wrapped_quote.count('\n') * 15 + 40
    draw.text((550, y_text), author_text, font=author_font, fill=text_color)

    filename = os.path.join(SAVE_DIR, f"quote_{idx+1}.png")
    image.save(filename)
    print(f"✅ saved: {filename}")

    return image

def main():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    quotes = get_quotes(QUOTES_LINK)

    for idx, (quote, author) in enumerate(quotes):
        create_image(quote, author, idx)

if __name__ == '__main__':
    main()
