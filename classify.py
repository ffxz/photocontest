#!/usr/bin/env python3
# coding = utf - 8

import urllib.request
from bs4 import BeautifulSoup
import re
import urllib.parse

def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('utf-8')
    return html

def get_h_o(html):
    org_list = []
    home_list = []
    soup = BeautifulSoup(html, 'html.parser')
    for k in soup.find_all('h3', attrs={'class': 'r'}):
        imgtag = k.select("a")
        #org为文本
        org = k.get_text("href")
        if org:
            pass
        #homepage为主页网址
        #print(imgtag[0]['href'])
        homepage = imgtag[0]['href']
        org_list.append(org)
        home_list.append(homepage)
    return([org_list, home_list])


def creat_dic(url):
    #mytxt = urllib.parse.urlparse('http://www.tsinghua.edu.cn/publish/eeaen/1699/2010/20101216113731526710440/20101216113731526710440_.htm')
    mytxt = urllib.parse.urlparse(url)

    #print(mytxt)

    netloc_list = mytxt.netloc
    path_list = mytxt.path
    params_list = mytxt.params
    query_list = mytxt.query
    #path_list = re.sub('[\.]', ' ', path_list)
    #去除.后面的内容
    pathii = path_list.split(".")
    path_list = pathii[0]
    path_list = re.sub('[^a-zA-Z]', ' ', path_list)
    #print(path_list)

    #netloc_str = netloc_list.split(".")
    netloc_str = re.split(r'[\W_]+', netloc_list)
    #path_str = re.sub('[^a-zA-Z]', ' ', path_list)
    path_str = re.split(r'[\W_]+', path_list)
    params_str = re.split(r'[\W_]+', params_list)
    query_str = re.split(r'[\W_]+', query_list)

    #print(netloc_str)
    #return(netloc_str + path_str + params_str + query_str)
    return (netloc_str)



'''
l1 = creat_dic('http://www.physics.manchester.ac.uk/people/staff/profile/?ea=terry.wyatt')
l2 = creat_dic('http://www.agri.sjtu.edu.cn/En/Data/View/2949')
l3 = l1+l2
l3 = list(set(l3))
print(l3)
'''

#获取文档的总行数
file = open('training.txt', encoding='utf-8')
lines = file.readlines()
file.close()
allline = 0
for line1 in lines:
    allline += 1

file = open('training.txt', encoding='utf-8')
ii = 1
num = 1
name_keyword = [' ']  #初始化这个list
org_keyword = [' ']
cache_list = []
l0 = []
for dida in range(100):                 #allline
    reg = r"#search_results_page:(.*)"
    reg_name = r"#name:(.*)"
    reg_org = r"#org:(.*)"
    line = file.readline()
    imgre = re.compile(reg)

    if (line == '\n'):
        ii += 1
        continue   #丢掉空行或是以空行为标志识别下一个人的数据

    # 匹配搜索页的网址
    imglist = re.findall(imgre, line)
    # 打印相应的网址(格式为列表)
    #print(imglist)

    # 将列表格式转化为str格式，因为urlopen后的网址参数需要是str
    url = ('').join(imglist)
    #print(url)
    if url:
        html = get_html(url)
        homepage = get_h_o(html)[1]
        sizehomepage = len(homepage)
        for k in range(sizehomepage):
            l1 = creat_dic(homepage[k])
            l0 += l1

l0 = list(set(l0))
print(l0)
file.close()


'''
html = get_html('http://ifang.ml:8081/543280d0dabfae8cc1c0f7a8.html')
homepage = get_h_o(html)[1]
sizehomepage = len(homepage)
'''
#打印org
#print((get_h_o(html)[0]))
#打印homepage
#print(get_h_o(html)[1])
'''
l0 = []
for k in range(sizehomepage):
    l1 = creat_dic(homepage[k])
    l0 += l1

l0 = list(set(l0))
print(l0)'''