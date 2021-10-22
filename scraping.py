from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import csv
from time import sleep
from colorama import Fore, Style


class Scrapping:
    def __init__(self):
        self.site = urlopen('https://dolarhoje.com/')

        self.soup = BeautifulSoup(self.site, 'html.parser')
        self.real = 0
        self.daily_records = 0

        self.file_name = 'CotaçãoDolar.csv'
        self.time_list = ['13:00:00', '14:00:00', '15:00:00', '16:00:00', '17:00:00', '18:00:00']

    def get_dollar_value(self):
        print(f'{Fore.LIGHTGREEN_EX}Init data collection!{Style.RESET_ALL}')
        while True:
            now = datetime.datetime.now()
            if self.time_list.__contains__(now.strftime('%H:%M:%S')):
                print(f'{Fore.LIGHTGREEN_EX}Collecting dollar value on time '
                      f'{now.strftime("%H:%M:%S")}{Style.RESET_ALL}')
                for dr in self.soup.find_all(id='nacional'):
                    self.real = dr.get('value').replace(',', '.')

                with open(self.file_name, 'a', newline='') as csv_file:
                    writer = csv.writer(csv_file, delimiter=';')

                    writer.writerow([now.strftime('%d/%m/%Y'), now.strftime('%H:%M:%S'), 1, self.real])

                    csv_file.close()
                self.daily_records += 1

            if now.strftime('%H:%M:%S') == '18:00:02':
                print(f'{Fore.GREEN}Closing the daily application on time {now.strftime("%H:%M:%S")}{Style.RESET_ALL}')
                print(f'{Fore.GREEN}Made {self.daily_records} collections today{Style.RESET_ALL}')
                break
            sleep(0.99)

    def create_csv_file(self):
        with open(self.file_name, 'x', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')

            writer.writerow(['Data', 'Hora', 'Dollar', 'Real'])
            csv_file.close()
