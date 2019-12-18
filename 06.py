'''
择一张图片，从客户端上传到服务端
温馨提示： 客户端读取图片的内容
将内容发送给服务端
服务端接受图片内容
保存在服务端某个位置
'''
print('hello test')
print('hello test2222')
from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',7714))
s.listen(5)
#保存位置
file_save_url='/home/tarena/图片/'
#先接受确认消息，如果为b'UPLOAD' 回复确认，准备接受消息
while True:#循环处理客户端请求
    c,addr=s.accept()
    data=c.recv(1024).decode()
    if data.split('#',1)[0]=='UPLOAD':
        c.send(b'OK')
        f=open('copy_%s'%(data.split('#',1)[1]),'wb')
        while True:
            data_=c.recv(1024)
            if data_==b'##@@OK@@##':
                f.close()
                break
            f.write(data_)
    else:
        #请求不正确
        continue #继续等待客户端
