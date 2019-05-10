import requests
import nltk
from bs4 import BeautifulSoup




#login_page = 'https://bbs.saraba1st.com/2b/member.php?mod=logging&action=login'



s1_url = 'https://bbs.saraba1st.com/2b/'

waiye_url = s1_url + 'forum-75-2.html'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/69.0.3497.92 Safari/537.36',
}

page = requests.get(waiye_url, headers=HEADERS)
page.encoding = "utf-8"



waiye_soup = BeautifulSoup(page.text, "html.parser")

page_body = waiye_soup.body


page_bodys_direct_children = page_body.contents

threadlist = page_body.find('div', id = 'threadlist')

thread_preview_table = threadlist.find('table',id = 'threadlisttableid' ).find_all('tbody')

l = len(thread_preview_table)

#print(type(content_table))

thread_id = thread_preview_table[2]['id']
a_elem = thread_preview_table[2].find('a')
href = s1_url+a_elem['href']

def get_threads_list_in_page(i):
    preview_page_url = s1_url+ 'forum-75-'+ i +'.html'
    preview_page = requests.get(preview_page_url, headers=HEADERS)
    preview_page.encoding = "utf-8"
    waiye_soup = BeautifulSoup(preview_page.text, "html.parser")
    preview_page_body = waiye_soup.body
    threadlist = preview_page_body.find('div', id='threadlist')
    return threadlist
#for each element in threadlist:
def get_thread_url_from_preview(thread_preview):
    thread_suffix_elem = thread_preview.find('a')
    thread_url = s1_url+thread_suffix_elem['href']
    return thread_url
#print(href)
href = 'https://bbs.saraba1st.com/2b/thread-1814122-1-6.html'

def get_thread_content(thread_url):
    all_content = requests.get(thread_url)
    cont_soup = BeautifulSoup(content.text, "html.parser")
    thread = cont_soup.find('div', id='postlist')

content = requests.get(href)

#def get_first_floor_content()
#print(content.text)
cont_soup = BeautifulSoup(content.text, "html.parser")
thread = cont_soup.find('div', id = 'postlist')
tokens = []
#test_text = thread.find_all('td', class_ ='t_f' )
#print(len(test_text))
#print(test_text)
counter = 0
all_text_list_unfiltered = thread.find_all('td', class_ = 't_f')
for text in all_text_list_unfiltered:
    text_filtered = (text.get_text().replace('br', '')).replace('img', '')
    print(text_filtered)
    print(counter)
    counter += 1

def get_all_text_filtered(thread):
    all_text_list_unfiltered = thread.find_all('td', class_ = 't_f')
    for text in all_text_list_unfiltered:
        text_filtered = (text.get_text().replace('a', '')).replace('br', '')
        print(text_filtered)

for reply in thread:
    #text = ((reply.find('td', class_ = 't_f')).get_text().replace('br', '')).replace('br', '')
#    print(text)
    text = reply.find_all('td', class_ = 't_f')
    print(text)
    tlist = []
    for t in text.split():
        tlist.append(t)
        print(t)

    tokens += tlist
#   tokens += [t for t in text.split()]
#print('start printint tokens...\n')
#print(tokens)


# tbody in content_table:
#    tbody_id = tbody['id']
#    if tbody_id == 'separatorline':
#        continue
#    a_elem = tbody.find('a')
#    href = s1_url+a_elem['href']
#    print(href)
#    content = requests.get(href)




