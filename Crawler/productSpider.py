import scrapy
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Add 403 code to retry_codes of settings.py


class ProductSpider(scrapy.Spider):
    name = 'products'
    start_urls = [
        'https://www.digikala.com/',
    ]
    page_number = 1

    def parse(self, response):

        mainCategoriesLinks = response.css(
            'div.c-navi-new-list__inner-categories  a')
        yield from response.follow_all(mainCategoriesLinks, self.parse_categories)

    def parse_categories(self, response):

        categoriesLinks = response.css(
            'li.c-catalog__plain-list--formatting a.c-catalog__plain-list--category-title')
        
        for category in categoriesLinks:
            self.page_number = 1
            yield response.follow(category, self.parse_products)

    def parse_products(self, response):
        print("\n\n\n\nStarted\n\n\n\n")
        for product in response.css('div.c-product-box'):
            yield {
                "product-data":    product.xpath('@data-enhanced-ecommerce').get(),
            }

        self.page_number += 1
        page = self.page_number
        next_page = response.css(
            f"li.js-pagination__item a.c-pager__item [data-page='{page}']").get("href")
        if next_page is not None and page < 5:
            print("\n\n\n\n\n\n\n", next_page)
            yield response.follow(next_page, self.parse)
