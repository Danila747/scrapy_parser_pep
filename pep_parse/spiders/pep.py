from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from pep_parse import constants as const


class PepSpider(CrawlSpider):
    name = 'pep'
    allowed_domains = const.ALLOWED_DOMAINS_FOR_PEP
    start_urls = const.START_URLS_FOR_PEP

    rules = (
        Rule(LinkExtractor(css='#numerical-index tbody a'), 
           callback='parse_pep'
        ),
    )

    def parse_pep(self, response):
        number, name = response.css('.page-title::text').get().split(' – ')
        yield {
            'number': int(number.split()[1]),
            'name': name,
            'status': response.css(
                                 'dt:contains("Status") + dd abbr::text'
                      ).get(),
        }
