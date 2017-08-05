import scrapy

class JobsSpider(scrapy.Spider):
    name = "titles"
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://newyork.craigslist.org/search/egr"]

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        
        for title in titles:
            yield {'Title': title}