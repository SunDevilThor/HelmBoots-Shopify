# Helm Boots - Shopify Store - JSON
# Tutorial from John Watson Rooney YouTube channel

import requests
import json
import pandas as pd

url = 'https://helmboots.com/products.json?limit=250&page=1'

response = requests.get(url)

data = response.json()

product_list = []

for item in data['products']:
    title = item['title']
    handle = item['handle']
    created = item['created_at']
    product_type = item['product_type']
    # print(title, handle, created, product_type)
    for image in item['images']:
        try:
            imagesrc = image['src']
        except:
            imagesrc = 'None'

    for variant in item['variants']:
        price = variant['price']
        sku = variant['sku']
        available = variant['available']

        product = {
            'title': title, 
            'handle': handle, 
            'created': created, 
            'product_type': product_type,
            'price': price, 
            'sku': sku, 
            'available': available, 
            'image': imagesrc,
        }

        product_list.append(product)

print(product_list)

df = pd.DataFrame(product_list)
df.to_csv('HelmBoots.csv')
print(df.head())
print('Saved to CSV file.')

# NOTES: 
# - Put products.json after the end of a URL of a Shopify store
# - Example: https://helmboots.com/products.json

# - To up the amount of products shown at a time, put ?limit=250 at the end of the URL. 
# - Example: https://helmboots.com/products.json?limit=250

# - If the site you are looking has more than 250 products, put &page=1 at the end of the URL, then run through each page.
# - Example: https://helmboots.com/products.json?limit=250&page=1 
