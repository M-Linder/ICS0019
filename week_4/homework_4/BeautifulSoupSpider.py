from bs4 import BeautifulSoup
import requests
import json
"""
@author: matlin
"""

start_url = 'https://anix-shop.com/product-category/figuurid-ja-manguasjad/'
result = []


def parse(start_urls):

    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')

    brics_list = soup.find_all("li", class_='product')

    for brick in brics_list:
        data = {'name': '', 'price': '', 'picture': '', }

        data['name'] = brick.h2.get_text()

        prices = brick.findNext("span", class_='price').text.split(" ")

        # If the website displays two or more prices, the first one is the original one. The second the actual one.
        if len(prices) == 1:
            data['price'] = prices[0]
        elif len(prices) == 3:
            data['price'] = ' '.join(prices)
        else:
            data['price'] = prices[1]

        data['picture'] = brick.img['data-src']

        print(data)
        result.append(data)

    try:
        next_page = soup.find("a", class_='next').get("href")
        if next_page:
            print(next_page)
            parse(next_page)
    except:
        # Write resulting list of dictionaries to file.
        with open('output/soup.json', 'w') as file:
            json.dump(result, file, indent=6)

        print("No more pages")


if __name__ == '__main__':
    parse(start_url)



