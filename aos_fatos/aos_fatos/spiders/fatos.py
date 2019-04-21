# sracpy list = lista os crwalers do projeto
# sracpy shell "http://example.com" = inicia uma janela interativa
# scrapy startproject aos_fatos = inicia um novo projeto de scrapy, entrando nessa pasta e rodando o comando seguinte vai criar um SPYDER pronto pra editar
# scrapy genspider fatos aosfatos.org = cria um spider "fatos= nome do arquivo" "aosfatos.org= url inicial"
# scrapy crawl fatos = roda o arquivo "fatos.py" de um projeto SCRAPY
#  -s HTTPCACHE_ENABLE=1 = para utilizar o cache e nao bater no servidor toda hora, utilizado para desenvolvimento
# -o arquivo.csv = cria um arquivo .csv com as informacoes (ele nao recria o arquivo, vai adicionando as informacoes no msm)
# scrapy runspider src/aosfatos.py -o quotes.csv = roda um arquivo separado que nao foi criado com o start_project
import scrapy
#import w3lib.html
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class FatosSpider(CrawlSpider):
    name = 'fatos'
    allowed_domains = ['aosfatos.org']
    start_urls = ['http://aosfatos.org/']

    rules = [
        Rule(LinkExtractor(restrict_xpaths=(
            '//li[contains(text(), "Checamos")]//ul/li'))
        ),
        Rule(
            LinkExtractor(restrict_css=('a.card')),
            callback='parse_new'
        ),
        Rule(
            LinkExtractor(restrict_css=('.pagination a'))
        )
    ]

    def parse_new(self, response):
        title = response.css('article h1::text').get()
        date = ' '.join(response.css('.publish_date::text').get().split())
        quotes = response.css('article blockquote p')
        quote_text=''
        status=''
        for quote in quotes:
            quote_text = quote.css('::text').get()
            status = quote.xpath(
                './parent::blockquote/preceding-sibling::figure//figcaption//text()').get()

        yield {
            'title': title,
            'date': date,
            'quote_text': quote_text,
            'status': status,
            'url': response.url
        }
