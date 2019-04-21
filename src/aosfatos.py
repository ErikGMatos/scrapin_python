import scrapy

class AosFatosSpider(scrapy.Spider):
    name = 'aosfatos'
    start_urls = ['http://aosfatos.org/']

    def parse(self, response):
        links = response.xpath(
            '//nav//ul//li/a[re:test(@href,"checamos")]/@href').getall()
        for link in links:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse_categoty
            )

    def parse_categoty(self, response):
        news = response.css('.card::attr(href)').getall()
        for new_url in news:
            yield scrapy.Request(
                response.urljoin(new_url),
                callback=self.parse_new
            )

        pages_url = response.css('.pagination a::attr(href)').getall()
        for page in pages_url:
            yield scrapy.Request(
                response.urljoin(page),
                callback=self.parse_categoty
            )

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
