import requests
import db
redis2=db.redis1()
import concurrent.futures
#检验代理ip是否合格
def jianyan(proxy):
    proxies = {
        "http": "http://" + proxy,
        "https": "https://" + proxy,
    }
    url="https://www.baidu.com"
    try:
        response=requests.get(url=url,proxies=proxies,timeout=2)
        if response.status_code in [200, 206, 302]:
            redis2.max(proxy)
            print("代理ip检验合格*************：",proxy)
        else:
            redis2.jianyan(proxy)
            print("代理ip检验不合格！",proxy)
    except Exception as r:
        redis2.jianyan(proxy)
        print("代理ip超时！",proxy)
def threa():
    data=redis2.quanbuip()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as exu:
        for i in data:
            exu.submit(jianyan,i)
    ip=redis2.quanbumax()
    ip_1=redis2.huoqu()
    # print(ip)
    # print(ip_1)
if __name__ == '__main__':

    pass