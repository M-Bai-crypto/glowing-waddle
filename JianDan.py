import urllib.request
import os
import random

#索引图片地址
def find_addrs(url):
    html = open_url(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a!= -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append(html[a+11:b+4])
        else:
            b = a + 11

        a = html.find('img src=',b)

    return img_addrs

#保存图片
def saving(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = open_url('http://' + each)
            f.write(img)
    f.close()

#将打开网页集成为一个方法
def open_url(url):
    response = urllib.request.Request(url)
    response.add_header('User_Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
    req = urllib.request.urlopen(url)
    html = req.read()

    return html

#使用代理
'''
    proxies_list = ['116.62.64.196:443','221.224.76.138:808','117.88.4.81:3000']
    proxy = random.choice(proxies_list)

    proxy_support = urllib.request.ProxyHandler({'http':proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
'''    
#下载主程序
def download_img (folder = 'ooxx',page_num = 4):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'

    while (page_num > 0):
        for i in range(page_num):
            page_url = url + 'MjAyMDAyMjktMTk' + str(page_num) + '#comments'
            img_addrs = find_addrs(page_url)
            saving(folder,img_addrs)
        page_num -= 1

if __name__ == '__main__':
    download_img()
