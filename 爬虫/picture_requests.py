import requests
import os

url="http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
root=r"/home/pi/Workspace/爬虫/"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("The files saved succesfully")
    else:
        print("The file is already existed")
except:
    print("The spider is failed")
    
