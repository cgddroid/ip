
import requests
import getip
import concurrent.futures
import copy
url="https://www.baidu.com"#119.59.125.189:3128
proxies = {
    "http": "http://123.56.175.31:3128",
    "https": "https://123.56.175.31:3128",
}
print(requests.get(url=url))
# print(a[:3])
#对集合进行操作
# https://blog.csdn.net/weixin_46307478/article/details/122953512
#对字典进行操作，不过操作之前需要用json.dumps进行序列化操作把字典变成字符串
# https://www.csdn.net/tags/Mtzakg5sMzM1NDEtYmxvZwO0O0OO0O0O.html
# redis各种命令