import requests
import os,re,time
def download_mp4(url,dir):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'http://91porn.com'}
    req=requests.get(url=url)
    with open(str(dir)+'/1.mp4','wb') as f:
        f.write(req.content)
def download_img(url,dir):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'http://91porn.com'}
    req=requests.get(url=url)
    with open(str(dir)+'/thumb.png','wb') as f:
        f.write(req.content)

flag=1
while flag<=100:
    base_url='http://91porn.com/view_video.php?viewkey='
    page_url='http://91porn.com/v.php?category=rf&viewtype=basic&page='+str(flag)
    get_page=requests.get(url=page_url)
    viewkey=re.findall(r'<a target=blank href="http://91porn.com/view_video.php\?viewkey=(.*)&page=.*&viewtype=basic&category=rf">\n                    <img ',str(get_page.content,'utf-8',errors='ignore'))
    for key in viewkey:
        get=requests.post('https://www.ojbk.us/api',{'url':'http://91porn.com/view_video.php?viewkey='+str(key)})
        getj=get.json()
        if os.path.exists(str(getj['video'][0]['desc']).strip())==False:
            os.makedirs(str(getj['video'][0]['desc']).strip())
            print('开始下载')
            download_mp4(getj['video'][0]['url'],str(getj['video'][0]['desc']).strip())
            download_img(getj['video'][0]['thumb'],str(getj['video'][0]['desc']).strip())
            print('下载完成')
        else:
            print('已存在文件夹,跳过')
            time.sleep(2)
    flag=flag+1
    print('此页已下载完成，下一页是'+str(flag))
    
