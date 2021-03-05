# Digikala Product Crawler

create a virtual environment using venv wrapper and activate it:
```bash
python3 -m venv env
source env/bin/activate
```

install the dependencies:
```bash
pip install -r requirements.txt
```
## Crawling Process

The spider crawls from the homepage and navigates through each main category. Then, it would crawl the first 5 pages of each primary sub category to extract concise information about each product. The most visited order filter on products fits our advertising purpose.

The output can be saved to a .jl file, each product in a new line, with the following command:

```bash
cd Crawler && scrapy runspider productSpider.py -o products.jl
```

## Cleaning the data

The output of the crawlers contains faulty and redundant data. The __cleanData.py__ script would create a comma separated values of these columns ['index', 'id', 'category', 'title', 'price', 'url']. Scrapy sends string as unicode not ascii. The built-in **ast** package to encode the results and transform the string to python dictionary. 

```bash
python cleanData.py
```
The csv file would be generated as __products.csv__