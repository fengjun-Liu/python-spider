#!/usr/bin/python3 
# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header
import requests
from bs4 import BeautifulSoup
from datetime import datetime

wea1='''<div id="7d" class="c7d">
<p>我就试试，不咋地</p>
</div>
'''

#获取今日日期
datemd=datetime.now().strftime("%Y/%m%d")
datemd2=datetime.now().strftime("%Y %m-%d")
#北京天气
weatherurl='https://www.tianqi.com/haidian/'
wchaturl = "https://sc.ftqq.com/[yourid].send"

headers={"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

# 第三方 SMTP 服务 
mail_host="smtp.163.com"  #设置服务器
mail_user="user"    #用户名
mail_pass="pass"   #口令 
	 	 
sender = ''
receivers = ['']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

def pushmywchat(text,desp):
	"""
    发送到我的微信
    使用了第三方推送 https://sc.ftqq.com/3.version ，需提前申请自己的key
    """
	dd={'text':text,"desp":desp}
	payload = {}
	headers= {}
	try:
		response = requests.request("GET", wchaturl, params=dd, headers=headers, data = payload)
		response.raise_for_status()
		response.encoding='utf-8'
		return(response.text)
	except:
		return "产生异常，发送微信消息失败"
		
def mail2qq(attcon):
	"""
    发送到我的qq邮箱
    格式为网络图片+文字
    """
	
	message = MIMEMultipart()
	message['From'] = sender
	#邮件主题，正文
	message['Subject'] = Header(datemd2+' 天气状况', 'utf-8')

	######网络图片，正文发送#####
	content = MIMEText('<html><body>'+attcon+'</body></html>', 'html', 'utf-8')
	message.attach(content)
	try:
		smtpObj = smtplib.SMTP() 
		smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
		smtpObj.login(mail_user,mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		smtpObj.quit()
		print ("邮件发送成功")
	except smtplib.SMTPException as err:
		print (err)		
			

wea=requests.get(weatherurl,headers=headers)
weasoup=BeautifulSoup(wea.content,'html.parser')
#查找imgs类型的a
weatag=weasoup.find('dl',{"class":"weather_info"})

weacont='<p>'+weasoup.find('dd',{"class":"week"}).string+'''</p><p>
          当前温度：'''+weasoup.find('p',{"class":"now"}).b.string+'℃   相对'+weatag.contents[9].b.string+"   "+weatag.contents[9].contents[1].string+ "   "+weatag.contents[11].h5.string+'''</p><p>
  今日天气:'''+weatag.contents[7].span.b.string+'''</p><p>
  今日温度：'''+weatag.contents[7].span.text+'''</p><p>
  '''+str(weatag.contents[11].span)+'</p>'
print(weacont)
mail2qq(weacont)
pushmywchat('今日天气状况',weacont)

