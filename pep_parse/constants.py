DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H-%M-%S'
STATUS_DT_FORMAT = '%Y-%m-%d_%H-%M-%S'

CSV_FIELDS = ['number', 'name', 'status']


ALLOWED_DOMAINS_FOR_PEP = 'https://peps.python.org/',
START_URLS_FOR_PEP = ['https://peps.python.org/']


PEP_NUMBER_XPATH = '//table[@class="list"]/tbody/tr/td[1]/text()'
PEP_TITLE_XPATH = '//table[@class="list"]/tbody/tr/td[2]/a/text()'
PEP_STATUS_XPATH = '//table[@class="list"]/tbody/tr/td[3]/text()'
