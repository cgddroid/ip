import requests
import re
import time
from parsel import Selector
import concurrent.futures
import db
redis2=db.redis1()
#云代理ip
def yundaill():
    compile=re.compile(".*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5})",re.S)
    a=[]
    for i in range(1,11):
        time.sleep(1)
        url=f"http://www.ip3366.net/?stype=1&page={i}"
        data=requests.get(url=url).text
        ip_data=re.findall(compile,data)
        for n in ip_data:
            a.append( f'{n[0]}:{n[1]}')
    return a
#芝麻ip
def zimadaill():
    head={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    compile=re.compile(".*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5})",re.S)
    url="https://jahttp.zhimaruanjian.com/?utm-source=bdtg&utm-keyword=?ocpc1088&bd_vid=11853667554564052828"
    data=requests.get(url=url,headers=head,timeout=3)
    data.encoding=data.apparent_encoding
    data_2=Selector(data.text)
    data_3=data_2.css('div .free-box').get()
    ip_data=re.findall(compile,data_3)
    a = []
    for n in ip_data:
        a.append(f'{n[0]}:{n[1]}')
    return a
#其他代理ip
def qitaip():
    compile=re.compile(".*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5})",re.S)
    url="https://proxy.seofangfa.com/"
    data=requests.get(url=url).text
    ip_data=re.findall(compile,data)
    a = []
    for n in ip_data:
        a.append(f'{n[0]}:{n[1]}')
    return a
#89代理ip
def bajiuip():
    compile = re.compile(".*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5})", re.S)
    a=[]
    for i in range(1, 29):
        time.sleep(1)
        url = f"https://www.89ip.cn/index_{i}.html"
        data = requests.get(url=url).text
        ip_data = re.findall(compile, data)
        for n,m in ip_data:
            a.append( f'{n}:{m}')
    return a
#快代理
def kuaiip():
    compile = re.compile(".*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,5})", re.S)
    a=[]
    for i in range(1, 11):
        time.sleep(1)
        url = f"https://www.kuaidaili.com/ops/proxylist/{i}/"
        data = requests.get(url=url)
        data.encoding=data.apparent_encoding
        data_1=Selector(data.text)
        data_2=data_1.css('#freelist').get()
        ip_data = re.findall(compile, data_2)
        for n in ip_data:
            a.append( f'{n[0]}:{n[1]}')
    return a
# if __name__ == '__main__':
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exu:
#         duixiang1=exu.submit(yundaill)
#         duixiang2=exu.submit(zimadaill)
#         duixiang3=exu.submit(qitaip)
#         duixiang4=exu.submit( bajiuip)
#         duixiang5=exu.submit(kuaiip)
#     data_0 = list(duixiang1.result())
#     data_1 = list(duixiang2.result())
#     data_2 = list(duixiang3.result())
#     data_3 = list(duixiang4.result())
#     data_4 = list(duixiang5.result())
#     data=data_0+data_1+data_2+data_3+data_4
#     print(data)
#     for i in data:
#         redis2.add(i)
