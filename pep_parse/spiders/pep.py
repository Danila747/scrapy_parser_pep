from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from pep_parse import constants as const
from pep_parse import items


class PepSpider(CrawlSpider):
    name = 'pep'
    allowed_domains = const.ALLOWED_DOMAINS_FOR_PEP
    start_urls = const.URLS_FOR_PEP

    rules = (Rule(
        LinkExtractor(allow=r'pep-\d{4}'),
        callback='parse_pep'
    ),)

    def parse_pep(self, response):
        return items.PepParseItem(
            number=response.xpath(const.PEP_NUMBER_XPATH).get().strip(),
            name=response.xpath(const.PEP_TITLE_XPATH).get().strip(),
            status=response.xpath(const.PEP_STATUS_XPATH).get().strip()
        )
