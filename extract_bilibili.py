import tkinter as tk
import time,re,urllib3
import threading,os,requests,sys
from PIL import Image, ImageTk
import tkinter.messagebox
import multiprocessing
def update_time(ab):
    while True:
        datetime = time.localtime()
        c = ("一","二","三","四","五","六","日")
        a = time.strftime("%Y-%m-%d %H:%M:%S %w",datetime)
        a = a.split(" ")
        a =  a[0] + " " + a[1]+ " "   '星期'+c[(int(a[2])-1)]
        ab.set(a)


def guanji():
    os.system("shutdown -s -t 1")
def xianshi(filname,lp):
        app = tk.Tk()
        app.title("%s.jpg"%lp)
        image2 =Image.open(filname)
        background_image = ImageTk.PhotoImage(image2)
        w = background_image.width()
        h = background_image.height()
        app.geometry('%dx%d+0+0' % (w,h))

        background_label = tk.Label(app, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        app.mainloop()
def xiazai():
        if re.match("^av\d+",var.get()):
                lp = var.get()
                url = 'https://www.bilibili.com/video/%s'%lp
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
                        'Referer': 'https://www.bilibili.com'}
                urllib3.disable_warnings()
                response = requests.get(url, headers=headers, verify=False)
                if str(response) == "<Response [200]>":
                        data = response.text
                        data = re.search('''content="(http:.*?)"''',data,re.S)
                        try:
                                data = data.group(1)
                        except AttributeError:
                                tk.messagebox.showerror("错误提示","该视频不见了!")
                        mmm = requests.get(data)
                        filename = os.path.dirname(sys.argv[0]) + "/" + "bili.jpg"
                        with open(filename,'wb') as f:
                                f.write(mmm.content)
                        ttt = multiprocessing.Process(target=xianshi,args=(filename,lp))
                        ttt.start()
                else:
                        tk.messagebox.showerror("错误提示","该av号不存在!")

        else:
                tk.messagebox.showerror("错误提示","请输入正确的av号！")


if __name__ == "__main__":
        mai = tk.Tk() #创建一个Tk类的实例（即主窗口对象）
        mai.title("bilibili封面提取") 
        mai.minsize(400,400)
        canvas = tk.Canvas(mai, height=320, width=500)
        kj = os.path.dirname(sys.argv[0]) + "/"+ "dpp.gif"
        image_file = tk.PhotoImage(file=kj)
        image = canvas.create_image(250, 0, anchor='n',image=image_file)
        canvas.pack()
        image = canvas.create_image(250, 0, anchor='n',image=image_file) 
        datetime = time.localtime()
        c = ("一","二","三","四","五","六","日")
        a = time.strftime("%Y-%m-%d %H:%M:%S %w",datetime)
        a = a.split(" ")
        a =  a[0] + " " + a[1]+ " "   '星期'+c[(int(a[2])-1)]
        ab = tk.StringVar()
        ab.set(a)
        lblTime = tk.Label(mai,textvariable =ab,bg = "yellow")
        lblTime.pack()
        t = threading.Thread(target=update_time,args=(ab,),daemon=True)
        t.start()


        var=tk.StringVar()
        username = tk.Entry(mai,textvariable = var)
        username.configure(width=50)
        username.pack()
        btnPower = tk.Button(mai,text = "下载",command = xiazai,bg = "green")
        btnPower.pack()
        mai.mainloop()#事件循环
