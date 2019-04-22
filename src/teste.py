import scrapy, os

class legco(scrapy.Spider):
    name = "sec_gov"

    start_urls = ["https://www.sec.gov/cgi-bin/browse-edgar?company=&match=&CIK=&filenum=&State=&Country=&SIC=2834&owner=exclude&Find=Find+Companies&action=getcompany"]

    def parse(self, response):
        for link in response.xpath('//table[@summary="Results"]//td[@scope="row"]/a/@href').extract():
            absoluteLink = response.urljoin(link)
            yield scrapy.Request(url = absoluteLink, callback = self.parse_links)

    def parse_links(self, response):
        for links in response.xpath('//table[@summary="Results"]//a[@id="documentsbutton"]/@href').extract():
            targetLink = response.urljoin(links)
            yield scrapy.Request(url = targetLink, callback = self.collecting_file_links)

    def collecting_file_links(self, response):
        for links in response.xpath('//table[contains(@summary,"Document")]//td[@scope="row"]/a/@href').extract():
            if links.endswith(".htm") or links.endswith(".txt"):
                baseLink = response.urljoin(links)
                yield scrapy.Request(url = baseLink, callback = self.download_files)

    def download_files(self, response):
        path = response.url.split('/')[-1]
        dirf = r"C:\Users\ToPath"
        if not os.path.exists(dirf):os.makedirs(dirf)
        os.chdir(dirf)
        with open(path, 'wb') as f:
            f.write(response.body)