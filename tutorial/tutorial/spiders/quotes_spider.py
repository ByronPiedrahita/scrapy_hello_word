#1) Importar Scrapy
import scrapy

# 2) Definir la lógica para extraer toda la información que queremos de la 
# página, en este caso, extraer todo el html
# Esta clase hereda de scrapy.Spider
class QuotesSpider(scrapy.Spider):

    # 3) Se definen los atributos name y start_urls (lista de direcciones web a 
    # a las que se quiere apuntar)
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    # 4) se define el método parse que recibe self y response (hace referencia
    # a la respuesta http en este caso de http: quotes.toscrape.com/' )
    def parse(self,response):
        with open('resultados.html','w',encoding='utf-8') as f:
            f.write(response.text)