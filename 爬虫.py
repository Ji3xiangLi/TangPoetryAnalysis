import requests

import json
from bs4 import BeautifulSoup
#从古诗文网站上爬取全唐诗和宋词 文件下载到./doc文件夹
def get_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chorme/65.0.3325.162 Safari/537.36'
    }
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        return response.text

    return None

def parse_page(html):
    soup = BeautifulSoup(html).find_all(class_="contson")
    soup_text = BeautifulSoup(str(soup))
    # 将\xa0无法解码的字符删除
    return soup_text.div.text.replace('\xa0', '')

def write_to_file(content,file):
    text = content.split('\n')
    with open(file,'a',encoding = 'utf-8') as f:
        for line in text:
            f.writelines(json.dumps(line,ensure_ascii= False))


def main(url):
    html = get_page(url)
    # write_to_file(parse_page(html),'./doc/全唐诗.txt')
    write_to_file(parse_page(html), './doc/全宋词.txt')

# for i in range(1109,2010):
#     url = 'https://www.gushiwen.org/wen_{}.aspx'.format(i)
#
#     main(url)
#     print(i)

for i in range(2687,3327):
    url = 'https://www.gushiwen.org/wen_{}.aspx'.format(i)
    main(url)
    print(i)
