import random
import time
from bs4 import BeautifulSoup
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/69.0.3497.92 Safari/537.36',
}


def cook_soup(url):
    #gingerbreadjar = save_cookies()
    #jar = requests.cookies.cookiejar_from_dict(gingerbreadjar)

    content = requests.get(url, headers = HEADERS)#, cookies = jar#)
    content.encoding = 'utf-8'
    print(content.status_code)
    s = random.randint(1,9)
    print('sleep for '+str(s)+' secs in cook_soup')
    time.sleep(s)
    soup = BeautifulSoup(content.text, "html.parser")
    return soup


def get_page():
    s = random.randint(4, 16)
    print('sleep for ' + str(s) + ' secs in get_page')
    time.sleep(s)
    preview_page_url = r'https://bbs.saraba1st.com/2b/forum-75-10000.html'
    #print(preview_page_url)
    waiye_soup = cook_soup(preview_page_url)
    preview_page_body = waiye_soup.body
    print('length of preview_page_body: ')
    print(preview_page_body)
    preview = preview_page_body.find('div', id='threadlist')
    print('preview: ')
    print(preview)
    all_preview = preview.find_all('tbody')
    for preview in all_preview:
        tbody_id = preview['id']
        if tbody_id[:13] == 'normalthread_':
            print(tbody_id)
    return

get_page()