from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pep_parse import items


class PepSpider(CrawlSpider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    rules = (
        Rule(
            LinkExtractor(allow=r'pep-\d{4}'),
            callback='parse_pep'
        ),
    )

    def parse_pep(self, response):
        return items.PepParseItem(
            number=response.xpath(
                                  '//dt[contains(., "PEP")]/following-sibling::dd/text()'
                                  ).get().strip(),
            name=response.xpath(
                                '//*[@id="pep-content"]/h1/text()'
                                ).get().strip(),
            status=response.xpath(
                                  '//dt[contains(., "Status")]/following-sibling::dd/text()'
                                  ).get().strip()
        )
