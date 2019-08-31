#/usr/bin/enve python
# -*- coding = 'utf-8' -*-
import ssl,re,requests,urllib3,os,sys
import tkinter as tk      # 导入Tkinter模块  
from PIL import Image, ImageTk  
# import socket,chardet,gzip,zlib,sys,os
# from PIL import Image,ImageTk
# sock = ssl.wrap_socket(socket.socket())
# sock.connect(("www.bilibili.com",443))

# rql = 'GET /video/av58307567 HTTP/1.1\r\nHost: www.bilibili.com\r\nConnection: Close\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9\r\nCookie: sfcsrftoken=4jTiNxVHoiNC5zO9s0D6XroTN4hu7cNXbuAQBj8g80jDhpzBfdif83ZQop2SIxq1; zh_choose=s\r\nReferer: https://www.bilibili.com\r\n\r\n'
# sock.sendall(rql.encode())

# data = b''
# while True:
#     pp = sock.recv(1000)
#     if not pp:
#         break
#     data += pp
# print(data)

# html = zlib.decompress(data, 16+zlib.MAX_WBITS)
# print(html)
#print(data.decode(encoding='unicode',errors='ignore'))



#head = {"User-Agent":" Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

# ssl._create_default_https_context = ssl._create_unverified_context
# rel = 'https://www.bilibili.com/'
# req = requests.post(rel,verify=True)
# print(req.text)
# req = "https://www.bilibili.com/video/av58307567/?spm_id_from=333.788.videocard.17"
# data = requests.get(req,headers=head)
# print(data.text)
# import socket 
# import ssl,urllib.request,requests,urllib3
# sock = ssl.wrap_socket(socket.socket()) 
# sock.connect(('www.bilibili.com', 443)) 
# data = 'GET /video/av58307567 HTTP/1.1\r\nHost: www.bilibili.com\r\nConnection: Close\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36\r\nReferer: https://www.bilibili.com\r\n\r\n'
# sock.sendall(data.encode())
# recv_data = sock.recv(8192)
# sock.close() 
# print (recv_data.decode())


# url = 'https://www.bilibili.com/video/av29862333'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
#             'Referer': 'https://www.bilibili.com'}
# urllib3.disable_warnings()
# response = requests.get(url, headers=headers, verify=False)
# if str(response) == "<Response [200]>":
#     data = response.text
#     data = re.search('''content="(http:.*?)"''',data,re.S)
#     data = data.group(1)
#     mmm = requests.get(data)
#     filename = os.path.dirname(sys.argv[0]) + "/" + "bili.jpg"
#     with open(filename,'wb') as f:
#         f.write(mmm.content)

#     app = tk.Tk()
#     app.title("bili.jpg")
#     image2 =Image.open(filename)
#     background_image = ImageTk.PhotoImage(image2)
#     w = background_image.width()
#     h = background_image.height()
#     app.geometry('%dx%d+0+0' % (w,h))

#     background_label = tk.Label(app, image=background_image)
#     background_label.place(x=0, y=0, relwidth=1, relheight=1)
#     app.mainloop()
# app = tk.Tk()
# app.title("bili.jpg")
# image2 =Image.open(r"bili.jpg")
# background_image = ImageTk.PhotoImage(image2)
# w = background_image.width()
# h = background_image.height()
# app.geometry('%dx%d+0+0' % (w,h))

# background_label = tk.Label(app, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# app.mainloop()
outfile = "dpp.gif"
root = os.path.dirname(sys.argv[0]) + '/' +'dpc.jpg'
pic = Image.open(root)
a = input("请输入图片的宽度:\t")
b = input("请输入图片的高度:\t")
pic = pic.resize((a, b))
pic.save(outfile)