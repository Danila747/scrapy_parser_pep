import collections
from datetime import datetime
import csv
import os
from pep_parse import settings

BASE_DIR = settings.BASE_DIR
BASE_DIR_1 = f"{BASE_DIR}/results/status_summary_"
LIST = ('Статус', 'Количество')
T = 'Total'
DATEFORM = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = collections.defaultdict(int)

    def close_spider(self, spider):
        filename = f"{BASE_DIR_1}{datetime.now().strftime(DATEFORM)}.csv"
        he = [(T, sum(self.statuses.values()))]
        data = [LIST] + list(self.statuses.items()) + he

        if os.path.exists(filename):
            os.remove(filename)
        
        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(data)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item
