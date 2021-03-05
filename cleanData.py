import ast
import csv

PRODUCT_START_URL = 'http://www.digikala.com/product/dkp-'

with open('Crawler/products.jl') as messy_data:
    with open('products.csv', mode='w') as output:
        cleaner = csv.writer(output, delimiter=',',
                             quotechar='"', quoting=csv.QUOTE_MINIMAL)
        cleaner.writerow(['index', 'id', 'category', 'title', 'price', 'url'])

        for index, dataline in enumerate(messy_data.readlines()):
            try:
                deserialized = ast.literal_eval(dataline)
            except ValueError:
                continue

            if deserialized['product-data'] is not None:
                try:
                    data = ast.literal_eval(deserialized["product-data"])
                except:
                    continue

                url = PRODUCT_START_URL + str(data['id'])
                cleaner.writerow(
                    [index+1, data['id'], data['category'], data['name'], data['price'], url])
