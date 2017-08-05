import scrapy

class JobsSpider(scrapy.Spider):
    name = "jobsone"
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://newyork.craigslist.org/search/egr"]

    def parse(self, response):
        jobs = response.xpath('//p[@class="result-info"]')
        
        for job in jobs:
            relative_url = job.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)
            title = job.xpath('a/text()').extract_first()
            address = job.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
            
            yield{'URL':absolute_url, 'Title':title, 'Address':address}