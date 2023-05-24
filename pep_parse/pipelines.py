import collections
from datetime import datetime
import csv
from pep_parse import settings

BASE_DIR = settings.BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = collections.defaultdict(int)

    def close_spider(self, spider):
        filename = f"{BASE_DIR}/results/status_summary_" +
                   f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
        data = [('Статус', 'Количество')] +
        list(self.statuses.items()) +
        [('Total', sum(self.statuses.values()))]

        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item
