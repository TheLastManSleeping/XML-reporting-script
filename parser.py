from datetime import datetime
from bs4 import BeautifulSoup

with open('karnel_logs_20220414.xml', 'r') as f:
    data = f.read()

bs_data = BeautifulSoup(data, 'xml')

for e in bs_data.find_all('transaction'):
    status = e.find('status')
    if status is None or status.text == '03' or status.text == '02':
        print(str(datetime.now()) + ' | ' + e.find('id').text + ' | ' + e.find('start_time').text + ' | ' + (
            'No data' if e.find('status') is None else e.find('status').text))
