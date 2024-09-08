import scrapy


class WorlpopSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/world-population/population-by-country/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath('//td/a')
        
        for country in countries:
            name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()
        
        yield {
            'country name': name,
            'country link': link
        }

# /html/body/div[2]/div[2]/div/div/div[2]/table/tbody/tr[3]/td[2]/a