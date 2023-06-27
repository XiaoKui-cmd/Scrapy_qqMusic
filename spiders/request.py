# 用requests爬取qq音乐信息
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent().random

url = "https://y.qq.com/n/ryqq/singer_list"
try:
    res = requests.get(url, headers={"User-Agent": ua})
    if res.status_code != 200:
        raise requests.RequestException
except requests.RequestException:
    print("无法链接到目标url！这是否是合法的url？")
    exit()
    
soup = BeautifulSoup(res.text, 'html.parser')
res2 = soup.select("#app > div > div.main > div.mod_singer_list > ul")


items = res2[0].find_all("li")
# 如何拿到res2中的所有“class="singer_list__item"”的数据


# print(res2)
print(items)
