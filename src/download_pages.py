import os
from urllib.request import urlopen, Request

from src.common_util import get_file_name
from src.download_info import parkruns

RAW_HTML_DIR = '../data'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
URL_TEMPLATE = 'https://www.parkrun.org.uk/{parkrun}/results/{event_num}/'


def download_page(url):
    req = Request(url, headers={'User-Agent': USER_AGENT})
    resp = urlopen(req)
    data = resp.read().decode('utf-8')
    return resp.getcode(), data


def store_html_content(parkrun, num, html):
    filename = get_file_name(parkrun, num)

    complete_name = os.path.join(RAW_HTML_DIR, filename)

    file = open(complete_name, "w")
    file.write(html)
    file.close()


if __name__ == "__main__":
    for parkrun in parkruns():
        current_event_num = parkrun.first_race

        while True:
            url = URL_TEMPLATE.format(parkrun=parkrun.name, event_num=str(current_event_num))
            status, html = download_page(url)

            if status == 200:
                store_html_content(parkrun.name, current_event_num, html)
            else:
                break

            current_event_num += 1

            print(url)
