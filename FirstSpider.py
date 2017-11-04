import scrapy

class FirstSpider(scrapy.Spider):
    name = "cl_pets"
    start_urls = ['https://newyork.craigslist.org/search/pet',]

    def parse(self, response):
        for title in response.xpath("//li[@class='result-row']//p"):
            yield {
                'tittle': tittle.xpath("a/text()").extract_first()
            }


    
