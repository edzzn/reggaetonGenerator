import scrapy

class LyricSpider(scrapy.Spider):
    name = 'GetArtistUrl'

    start_urls = [
                    'https://www.letras.com/estilos/reggaeton/artistas.html',
                ]

    def parse(self, response):
        for artist in response.xpath("//ul[@class='cnt-list-thumb-l cnt-list--col3 ']"):

            yield{
                'artist': artist.xpath(".//li//a/@href").extract(),
            }
