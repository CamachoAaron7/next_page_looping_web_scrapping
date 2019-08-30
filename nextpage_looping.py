# import requests
# r = requests.get('https://www.teamleada.com')
# print(r.status_code)
# # returns a 200 code indicating 'OK'.
# """An 'OK' status indicates that we received back some meaningful HTML 
#    from the request. Note that this does NOT mean that the HTML is valid 
#    and well-formed. It tells us that the request was able to hit the server 
#    and detected no signs of unusual error.""" 
# print(r.text)
# #Going off the code from before, you ask for the 'text' parameter to get the html you got back.

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
# also ensure that you have version 4.x.x for your BeautifulSoup version:
 # import main module first
# print(bs4.__version__)


my_url = "https://twinfalls.craigslist.org/search/sss?query=macbook&sort=rel"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')

# print(page_soup.p)

content = page_soup.find_all('p', {'class': 'result-info'})

len(content)

print(len(content))

products = content[0]

# filename = "results.csv"
# f = open(filename, 'w') 

# headers = "product_name, product_price, product_location, post_date\n"

# f.write(headers)

for products in content :
	product = products.find_all("a", {"class":"result-title hdrlnk"})
	product_name = product[0].text.strip()
	products_price = products.find_all("span", {"class":"result-price"})
	product_price = products_price[0].text.strip()
	# products_location = products.find_all("span", {"class":"result-hood"})
	# product_location = products_location[0].text.strip()
	# products_post_date = products.find_all("time", {"class":"result-date"})
	# product_post_date = products_post_date[0]['datetime']
	# conv = time.strptime(product_post_date,"%Y-%m-%d %H:%M")
	# time.strftime("%m/%d/%Y", conv)
	# post_date = time.strftime("%m/%d/%Y", conv)

	print("product_name: " + product_name)
	print("product_price: " + product_price)
	# print("product_location: " + product_location)
	# print("post_date: " + post_date)

	# print(search_results[0]) #printing the first element.
# print(search_results[0]['href'])

# 	f.write(product_name.replace(",", "|") + "," + product_price + "," + "," + post_date + "\n")
	
# f.close()