import scrapy
import pickle

with open('lista_canciones.pickle', 'rb') as handle:
    lista_canciones = pickle.load(handle)

class LyricSpider(scrapy.Spider):
    name = 'GetSongLyrics'

    start_urls = lista_canciones

    def parse(self, response):
        for letra in response.css("div.cnt-letra"):

            yield{
                'lyrics': letra.css("p::text").extract(),
            }
