import urllib.request
import urllib.parse
import time
import random
import hashlib # 加密
import json



from tkinter import Tk,Button,Entry,Label,Text,END


#后台爬虫翻译程序代码

class YouDaoFanyi(object):
	def __init__(self):
		pass
	def crawl(self,word):
		#获取的是秒
		timestamp = int(time.time()*1000) + random.randint(0,10) #转换为毫秒 再扎转换为整型

		u = "fanyideskweb"
		t = word
		r = str(timestamp)
		s =  "aNPG!!u6sesA>hBAW1@(-"
		    
		sign = hashlib.md5((u+t+r+s).encode('utf-8')).hexdigest()
		url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
		head = {}
		head['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
		data = {
		        'i':word,
		        'from':'AUTO',
		        'to':'AUTO',
		        'smartresult':'dict',
		        'client':'fanyideskweb',
		        #'salt':'1516344328939',
		        'salt' : timestamp,
		        #'sign':'1f7d7e01ed5c59afae4176155d82f446',
		        'sign': sign,
		        'doctype':'json',
		        'version':'2.1',
		        'keyfrom':'fanyi.web',
		        'action':'FY_BY_ENTER',
		        'typoResult':'true',
		        
		        #'ue':'UTF-8'#设置翻译支持中文

		    }

		data = urllib.parse.urlencode(data)

		req = urllib.request.Request(url,data.encode(),head)
		response = urllib.request.urlopen(req)
		trans_result = response.read().decode('utf-8')
		result_dict = json.loads(trans_result)
		#print(trans_result)
		result = result_dict['translateResult'][0][0]['tgt']
		#print(result_dict['translateResult'][0][0]['tgt'])
		return result



class Application(object):
	def __init__(self):
		self.window = Tk()
		self.fanyi = YouDaoFanyi()


		self.window.title(u'小坤翻译')
		#设置窗口大小和位置
		self.window.geometry('310x370+500+300')
		self.window.minsize(310,370)
		self.window.maxsize(310,370)
		#创建一个文本框
		#self.entry = Entry(self.window)
		#self.entry.place(x=10,y=10,width=200,height=25)
		#self.entry.bind("<Key-Return>",self.submit1)
		self.result_text1 = Text(self.window,background = '#ccc')
		self.result_text1.place(x = 10,y = 5,width = 285,height = 155)
		self.result_text1.bind("<Key-Return>",self.submit1)
		
		#创建一个按钮
		#为按钮添加事件
		self.submit_btn = Button(self.window,text=u'自动翻译',command=self.submit)
		self.submit_btn.place(x=170,y=165,width=70,height=25)
		self.submit_btn2 = Button(self.window,text=u'清空',command = self.clean)
		self.submit_btn2.place(x=250,y=165,width=35,height=25)

		#翻译结果标题
		self.title_label = Label(self.window,text=u'翻译结果:')
		self.title_label.place(x=10,y=165)
		#翻译结果

		self.result_text = Text(self.window,background = '#ccc')
		self.result_text.place(x = 10,y = 190,width = 285,height = 165)
		#回车翻译
	def submit1(self,event):
		#从输入框获取用户输入的值
		content = self.result_text1.get(0.0,END).strip().replace("\n"," ")
		#把这个值传送给服务器进行翻译
		
		result = self.fanyi.crawl(content)
		#将结果显示在窗口中的文本框中

		self.result_text.delete(0.0,END)
		self.result_text.insert(END,result)
		
		#print(content)

	def submit(self):
		#从输入框获取用户输入的值
		content = self.result_text1.get(0.0,END).strip().replace("\n"," ")
		#把这个值传送给服务器进行翻译
		
		result = self.fanyi.crawl(content)
		#将结果显示在窗口中的文本框中

		self.result_text.delete(0.0,END)
		self.result_text.insert(END,result)
		print(content)
	#清空文本域中的内容
	def clean(self):
		self.result_text1.delete(0.0,END)
		self.result_text.delete(0.0,END)

	def run(self):
		self.window.mainloop()


if __name__=="__main__":
	app = Application()
	app.run()
	







