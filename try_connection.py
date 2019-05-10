import pymssql
import pickle
import nltk
import jieba
import jieba.analyse


def con():
    connection = pymssql.connect(server = '.', database='Amsterdam')
    if connection:
        print('connect to the sql server successfully')
    connection.close()
    return


def load_data(i):
    with open('page'+str(i)+'.plk', 'rb') as f:
        return pickle.load(f)



def go_to_Amsterdam():
    connection = pymssql.connect(server='.', database='Amsterdam')
    if connection:
        print('connect to the sql server successfully')
    return connection

global connection
connection = go_to_Amsterdam()

def leave_Amsterdam():
    global connection
    if connection:
        connection.close()
    if connection:
        print('why this connection is not closed properly?')


def save_data(obj, i):
    with open('page'+str(i)+'.plk', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        print('data in page '+str(i)+' is saved')


def save_data_to_db(i):
    global connection
    data_list = load_data(i)
    failed = []
    cursor = connection.cursor()
    for d in data_list:
        pid = d[0]
        text = d[1]
        user_name = d[2]
        print(pid+r', '+text+r', '+user_name)
        query = 'insert into pre_processed_text values(\''+pid+'\', \''+text+'\', \''+user_name+'\')'
        try:
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print('error occur: ')
            failed+=d
            continue
    save_data(failed, 'failed-'+str(i))
    return

def cut_contents(filtered_content):
    global stopwords
    words_list = jieba.lcut(filtered_content)
    r = []
    for w in words_list:
        if w not in stopwords and len(w)<25:
            print(w)
            r.append(w)
    print(r)
    return r


def save_all_data():
    for i in range(7,16):
        save_data_to_db(i)


def load_stopwords(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding = 'utf-8').readlines()]
    c = stopwords.pop(0)
    #print(stopwords)
    return stopwords

global stopwords
stopwords = load_stopwords('stopwords.txt')

def update_word_frequency():
    global connection
    freq_dict = {}
    global stopwords
    print(stopwords)
    cur = connection.cursor()
    cur.execute('select * from dbo.pre_processed_text where pid in (select pid from dbo.pre_processed_text) order by pid')
    r = cur.fetchone()
    while r:
        cont = r[1]
        print('contents: '+cont)
        words_in_one_post = cut_contents(cont)
        print(words_in_one_post)
        for w in words_in_one_post:
            if w in freq_dict:
                freq_dict[w]+=1
            else:
                freq_dict[w] = 1
        r = cur.fetchone()

    for key in freq_dict:
        print(key)
        cur.execute('select * from dbo.key_word_table where word = %s', key)
        word_freq = cur.fetchone()
        print(word_freq)
        if word_freq:
            c = word_freq[1]+freq_dict[key]
            cur.execute('update dbo.key_word_table set freq = '+str(c)+' where word =\' '+key+'\'')
            connection.commit()
        else:
            cur.execute('insert into dbo.key_word_table values(\''+key+'\',' +str(freq_dict[key]) +')')
            connection.commit()




update_word_frequency()
leave_Amsterdam()

