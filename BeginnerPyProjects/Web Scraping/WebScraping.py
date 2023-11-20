import requests
from bs4 import BeautifulSoup


# Scraping Yahoo for stock prices

def get_stock_profit(symbol):
    # URl of yahoo for stock symbol
    url = f"https://finance.yahoo.com/quote/{symbol}"

    # Send a GET request to the website
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    # Check if the request  was successful (status code 200)
    if response.status_code == 200:
        # Parse the html content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the element containing the stock price (modify this based on the structure of the website)
        price_element = soup.find('div', {'value': '50'})

        if price_element:
            return price_element.text
        else:
            return f"Couldn't find the stock price for {symbol}."

    else:
        return f"Failed to retrieve the page for {symbol}. Status code: {response.status_code}"


# Example: Get the stock price for Apple Inc. (AAPL)

symbol = "APPL"
stock_price = get_stock_profit(symbol)
print(f"The stock price of {symbol} is: {stock_price}")
