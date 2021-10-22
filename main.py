from os import path, system, name
from scraping import Scrapping

Scrpp = Scrapping()

if not path.exists(Scrpp.file_name):
    Scrpp.create_csv_file()

if __name__ == '__main__':
    system('cls' if name == 'nt' else 'clear')
    Scrpp.get_dollar_value()
