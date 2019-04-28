import datetime
import json

import requests
from lxml import etree
import threading
from queue import Queue
import redis
import signal
client = redis.StrictRedis(host="sharemsg.cn",db=12)

url = "http://www.xiachufang.com/explore/"
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'cookie': 'grwng_uid=97c5e884-b49d-42cf-89cb-0706aeed796b'
}
base_url = "http://www.xiachufang.com"
html = requests.get(url,headers=headers).text

res = dict()

def fetch(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise requests.HTTPError("没有啦"+url)

def parse_data(selector):
    title = selector.xpath("//h2[@id='steps'][last()]/text()")[0].strip()
    li_selector = selector.xpath("//div[@class='steps']/ol/li")
    steps = []
    for li in li_selector:
        text = li.xpath(".//p[@class='text']/text()")
        img = li.xpath(".//img/@src")
        alt = li.xpath(".//img/@alt")

        alt = alt[0] if alt else ""
        text = text[0] if text else ""
        img = img[0] if img else ""
        steps.append(alt + ":" + text + "图片是：" + img)
        print(title, steps)


running = True
import time
def download(i):
    while running:
        next_url = client.lpop("xiachufang.links")
        if next_url is not None:

            text_html = fetch(next_url)
            next_selector = etree.HTML(text_html)
            parse_data(next_selector)
            time.sleep(0.2)
    print("进程 %d 结束了" % i)

links_queue = Queue()
threads = []
def stop(signum,frame):
    print("sss")
    global running
    running = False

import sys
if __name__ == '__main__':
    now = datetime.datetime.now()
    if len(sys.argv) > 1:
        url = sys.argv[1]
        selector = etree.HTML(fetch(url))
        links = selector.xpath("//ul[@class='list']/li/div/a/@href")
        for i in links:
            next_url = base_url + i
            print(next_url)
            if client.sadd("xiachufang.seen", next_url):
                client.rpush("xiachufang.links", next_url)
    else:
        signal.signal(signal.SIGINT, stop)
        for i in range(10):
            t = threading.Thread(target=download,args=(i,))
            threads.append(t)
            t.start()

        for i in threads:
            i.join()




