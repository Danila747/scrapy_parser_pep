from pathlib import Path

BASE_DIR = 'C:\Dev\scrapy_parser_pep\pep_parse\results'
PARSER_NAME = 'pep_parse'

SPIDER_MODULE = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 1000

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}
