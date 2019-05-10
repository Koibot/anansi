from typing import Any, Union
import requests
from bs4 import BeautifulSoup
import re
import jieba



s1_url = 'https://bbs.saraba1st.com/2b/'

class data:
    def __init__(self, pid, cont, user_name):
        self.postid = pid
        self.content = cont
        self.user = user_name

def cook_soup(url):
    rsp = requests.get(url)
    rsp.encoding = 'utf-8'
    soup = BeautifulSoup(rsp.text, "html.parser")
    return soup

def filter_single_post(post):
    q_tag = post.blockquote
    if q_tag != None:
        remove_quote = post.blockquote.extract()
    i_tag = post.i
    if i_tag != None:
        remove_pinfo = post.i.extract()
    device_info = post.a
    if device_info != None:
        remove_dinfo = post.a.extract()
    img_tag = post.img
    if img_tag != None:
        remove_img_info = post.img.extract()
    filtered_text = post.get_text(strip=True)
    filtered_data = ''.join(re.findall(r'[a-zA-Z0-9\u4e00-\u9fa5]', filtered_text))
    #print(filtered_data)
    return filtered_data

def get_posts_in_a_thread(thread_url):
    cont_soup = cook_soup(thread_url)
    thread_body = cont_soup.body
    wp_div = thread_body.find('div', id = 'wp')

    ct_div = wp_div.find('div', id = 'ct')
    thread_post_list = ct_div.find('div', id = 'postlist')
    post_list = thread_post_list.find_all('div', id = re.compile("post_\d{8}"))
    data_list = []
    for post in post_list:
        #print(post)
        pid = post.find('table')['id']
        user = post.find('div', class_='authi').find('a').text
        content = filter_single_post(post.find('td', class_='t_f'))
        d = [pid, content, user]
        data_list.append(d)
    next_page = cont_soup.find('div', class_ = 'pgbtn')
    if next_page != None:
        np_url_suffix = next_page.find('a')['href']
        np_url: Union[str, Any] = s1_url+np_url_suffix
        np_data_list = get_posts_in_a_thread(np_url)
        data_list += np_data_list
    print(data_list)
    return data_list

def test():
    print('???')
    get_posts_in_a_thread('https://bbs.saraba1st.com/2b/thread-1815503-1-5.html')

test()