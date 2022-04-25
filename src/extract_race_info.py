import os

from bs4 import BeautifulSoup

DIR = '../data/'

if __name__ == "__main__":
    files = os.listdir(DIR)
    for file in files:
        soup = BeautifulSoup(open(DIR + file).read())
        all_rows = soup.find_all("tr", {"class": "Results-table-row"})

        for row in all_rows:



