from bs4 import BeautifulSoup
import requests

url = r"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/109.0.0.0 Safari/537.36"}

r = requests.get(url, headers=header)
soup = BeautifulSoup(r.content, 'html.parser')
soup1 = BeautifulSoup(soup.prettify(), 'html.parser')

lists = soup1.find_all('div', class_="sg-col-inner")  # This is used to access the whole product details of a page.

print("-----------------------------------------------------------------------------------------------------------")
print("Product LIKNS")
print("-----------------------------------------------------------------------------------------------------------")
for link in soup1.find_all('a', attrs={'class': 'a-link-normal s-underline-text s-underline-link-text '
                                                's-link-style a-text-normal'}):
    links = link.get('href')
    product_url = 'https://amazon.com' + links
    print(product_url)
print(" "
      " ")


print("-----------------------------------------------------------------------------------------------------------")
print("Product Titles")
print("-----------------------------------------------------------------------------------------------------------")
for title in soup1.find_all('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'}):
    product_name = title.text.strip()
    print(product_name)
print(" "
      " ")

print("-----------------------------------------------------------------------------------------------------------")
print("Product PRICES")
print("-----------------------------------------------------------------------------------------------------------")
for price in soup1.find_all('span', attrs={'class': 'a-price-whole'}):
    product_price = price.text.strip()
    print(product_price)
print(" "
      " ")


print("-----------------------------------------------------------------------------------------------------------")
print("Product REVIEWS")
print("-----------------------------------------------------------------------------------------------------------")
for review in soup1.find_all('span', attrs={'class': 'a-size-base s-underline-text'}):
    product_reviews = review.text.strip()
    print(product_reviews)
print(" "
      " ")


print("-----------------------------------------------------------------------------------------------------------")
print("Product RATINGS")
print("-----------------------------------------------------------------------------------------------------------")
for ratings in soup1.find_all('i', attrs={'class': 'a-icon a-icon-star-small a-star-small-4 aok-align-bottom'}):
    product_ratings = ratings.text.strip()
    print(product_ratings)
print(" "
      " ")

