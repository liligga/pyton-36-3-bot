import requests
from parsel import Selector
from pprint import pprint

# httpx, aiohttp
# crawling, scraping, parsing

class CarsKgScraper:
    MAIN_URL = 'https://cars.kg/offers'
    BASE_URL = 'https://cars.kg'

    def get_html(self, url = MAIN_URL):
        response = requests.get(url)
        # print(response.status_code)
        if response.status_code == 200:
            return response.text

    def get_title(self, html):
        selector = Selector(text = html)
        title = selector.css('title::text').get()
        # title = selector.xpath('//title/text()').get()
        return title

    def paginate(self, from_page = 1, to_page = 10):
        for page in range(from_page, to_page + 1):
            yield f"{self.MAIN_URL}/{page}"
    
    def get_cars(self, html):
        selector = Selector(text = html)
        cars = selector.css('.catalog-list-item')
        all_cars = []
        for car in cars:
            title = car.css(".catalog-item-caption::text").get().strip()
            mileage = car.css(".catalog-item-mileage::text").get()
            if mileage is not None:
                mileage = mileage.strip()
            thumbnail_url = car.css(".catalog-item-cover img").attrib.get('src')
            price_usd = car.css(".catalog-item-price::text").get()
            price_kgs = car.css(".catalog-item-price").attrib.get('title', '').replace("или ~ ", "")
            link = car.attrib.get('href')
            all_cars.append({
                'title': title,
                'mileage': mileage,
                'thumbnail_url': thumbnail_url,
                'price_usd': price_usd,
                'price_kgs': price_kgs,
                'link': f"{self.BASE_URL}{link}"
            })
        return all_cars

    def get_car_links(self):
        links = []
        for url in self.paginate(1, 3):
            html = self.get_html(url)
            selector = Selector(text = html)
            cars = selector.css('.catalog-list-item')
            for car in cars:
                link = car.attrib.get('href')
                links.append(f"{self.BASE_URL}{link}")
        return links

if __name__ == '__main__':
    scraper = CarsKgScraper()
    html = scraper.get_html()
    ### get html
    # print(html[:250])
    ### показать заголовок
    # title = scraper.get_title(html)
    # print(title)
    ### показать все данные машин
    # cars = scraper.get_cars(html)
    # pprint(cars)
    # print("=======================")
    ### показать все ссылки
    links = scraper.get_car_links()
    pprint(links)
    print(len(links))