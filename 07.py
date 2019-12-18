'''
择一张图片，从客户端上传到服务端
温馨提示： 客户端读取图片的内容
将内容发送给服务端
服务端接受图片内容
保存在服务端某个位置
文件名　客户端发送请求给服务器，请求上传，
服务器接收到请求，回复确认
客户端收到回复开始上传文件
'''
from socket import *
import os
s=socket(AF_INET,SOCK_STREAM)
s.connect(('127.0.0.1',7714))
file=input('input file_url(绝对路径):')
# /home/tarena/wz/review/07_file_upl_client.py
file_name=os.path.split(file)[-1].encode() #获取文件名称
print(file_name)
print(os.path.splitext(file)) #打印文件后缀名
while True:
    try:
        f=open(file,'rb')
        break #判断文件是否存在，如果存在，继续向下执行
    except Exception as e:
        print('文件不存在！')
        continue
s.send(b'UPLOAD#'+file_name)
if s.recv(1024)==b'OK':
    #准备开始传送文件
    while True:
        data=f.readline()
        if not data:
            s.send(b'##@@OK@@##') #文件发送完成，向服务器发送消息确定
            break
        s.send(data)
else:
    print('服务器无法上传该文件！')
print('文件上传完成！')
s.close()










