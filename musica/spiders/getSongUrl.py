import scrapy
import pickle

with open('lista_artistas.pickle', 'rb') as handle:
    lista_artistas = pickle.load(handle)

class LyricSpider(scrapy.Spider):
    name = 'GetSongUrl'
    start_urls = lista_artistas

    def parse(self, response):
        for song in response.xpath("//ul[@class='cnt-list']"):

            yield{
                'urls': song.xpath(".//li//a//@href").extract(),
            }
