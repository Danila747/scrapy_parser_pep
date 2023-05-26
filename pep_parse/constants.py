DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H-%M-%S'
STATUS_DT_FORMAT = '%Y-%m-%d_%H-%M-%S'

CSV_FIELDS = ['number', 'name', 'status']


ALLOWED_DOMAINS_FOR_PEP = 'https://www.python.org/dev/peps/#numerical-index',
URLS_FOR_PEP = ['https://peps.python.org']


PEP_NUMBER_XPATH = '//dt[contains(., "PEP")]/following-sibling::dd/text()'
PEP_TITLE_XPATH = '//*[@id="pep-content"]/h1/text()'
PEP_STATUS_XPATH = '//dt[contains(., "Status")]/following-sibling::dd/text()'
