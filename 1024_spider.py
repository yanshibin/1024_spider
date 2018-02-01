import requests
import threading
import re
import os
def download_pic(url,dir,filename):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'https://t66y.com'}
    req=requests.get(url=url,headers=headers)
    if req.status_code==200:
        with open(str(dir)+'/'+str(filename)+'.jpg','wb') as f:
            f.write(req.content)
flag=1
while flag<=270:
    base_url='https://t66y.com/'
    page_url='https://t66y.com/thread0806.php?fid=8&search=&page='+str(flag)
    get=requests.get(page_url)
    article_url=re.findall(r'<h3><a href="(.*)" target="_blank" id="">(?!<.*>).*</a></h3>',str(get.content,'gbk',errors='ignore'))
    for url in article_url:
        getpage=requests.get(str(base_url)+str(url))
        tittle=re.findall(r'<h4>(.*)</h4>',str(getpage.content,'gbk',errors='ignore'))
        file=tittle[0]
        if  os.path.exists(file)==False:
            os.makedirs(file)
            img_url=re.findall(r'<input src=\'(.*?)\'',str(getpage.content,'gbk',errors='ignore'))
            filename=0
            print('开始下载：'+file)
            for download_url in img_url:
                print('下载第'+str(filename+1)+'张图片中~~~')
                download_pic(download_url,file,filename)
                print('下载完成')
                filename=filename+1
            print('下载完成，共'+str(filename)+'张图片')
        else:
            print('文件夹已存在，跳过')
    print('第'+str(flag)+'页下载完成')
    flag=flag+1
    