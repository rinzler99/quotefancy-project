from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import os

home = os.path.expanduser('~')
os.makedirs(home + '/Desktop/Qoutes', exist_ok=True)
url1 = "https://quotefancy.com/"
html = urlopen("https://quotefancy.com")
soup = BeautifulSoup(html)
l = soup.find_all(name='img')
urlist = []

for i in l:
    f = i.get("alt")
    link = url1 + str(f).lower().replace(" ", "-")
    urlist.append(link)
dic = {}

for i in urlist:
    g = i.split('/')[-1]
    dic[g] = []
    html1 = urlopen(i)
    soup = BeautifulSoup(html1)
    l = soup.find_all(name='img')
    for i1 in l:
        f = i1.get("data-original")
        dic[g].append(f)

os.makedirs(home + '/Desktop/Qoutes'+'/all-links',exist_ok=False)
for k in dic:
    s=''
    for i in dic[k]:
        if i != None :
            q = i.split('Quote-')
            if 'https' not in q[-1]:
                s+=i+'\n'
    f=open(home + '/Desktop/Qoutes'+'/all-links/'+k,'w+')
    f.write(s)

for k in os.listdir(home + '/Desktop/Qoutes' + '/all-links'):
    os.makedirs(home + '/Desktop/Qoutes/' + k, exist_ok=True)
    f = open(home + '/Desktop/Qoutes' + '/all-links/' + k, 'r')
    dic = f.readlines()
    print("Downloading files from " + k)
    nofile = 0
    for image_url in dic:
        if image_url != None:
            q = image_url.split('Quote-')
            if 'https' not in q[-1]:
                save = home + '/Desktop/Qoutes/' + k + '/'
                er = image_url.split('\n')[0]
                try:
                    r = requests.get(er)
                    with open(save.split('\n')[0], 'wb') as f:
                        f.write(r.content)
                    nofile += 1
                except:
                    print("Somthing went wrong")
    print(nofile, " Successfully Downloaded...")
