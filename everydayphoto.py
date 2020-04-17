#!/usr/bin/python3 
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header
import requests
from bs4 import BeautifulSoup
from datetime import datetime

#获取今日日期
datemd=datetime.now().strftime("%Y/%m%d")
datemd2=datetime.now().strftime("%Y %m-%d")
#国家地理每日一图
imgsurl='http://www.ngchina.com.cn/photography/photo_of_the_day/'
wchaturl = "https://sc.ftqq.com/[yourid].send"

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
		
def mail2qq(atturl,attcon):
	"""
    发送到我的qq邮箱
    格式为网络图片+文字
    """
	
	message = MIMEMultipart()
	message['From'] = sender
	#邮件主题，正文
	message['Subject'] = Header(subject, 'utf-8')

	######网络图片，正文发送#####
	content = MIMEText('<html><body><img src="'+atturl+'" alt="imageid"><p>'+attcon+'</p></body></html>', 'html', 'utf-8')
	message.attach(content)

	######网络图片，下载后作为附件发送#######
	# message.attach(MIMEText('国家地理每日一图', 'plain', 'utf-8')) #正文
	# #附件下载并写入本地
	# file_att = atturl.split('/')[-1]

	# imgre = requests.get(atturl)
	# open(file_att, "wb").write(imgre.content)
	# print("下载完毕")
	# #邮件附件
	# att1 = MIMEApplication(open(file_att, 'rb').read())
	# att1.add_header('Content-Disposition', 'attachment', filename= file_att.split('\\')[-1])
	# message.attach(att1)

	##### 本地图片上传，正文发送#####
	# content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8')  # 正文
	# message.attach(content)
	# file_att = 'E:\\Git\\test\\a.jpg'
	# file = open(file_att, "rb")
	# img_data = file.read()
	# file.close()
	# img = MIMEImage(img_data)
	# img.add_header('Content-ID', 'imageid')
	# msg.attach(img)
	#####

	######其他类型附件发送#####
	#zipFile = '算法设计与分析基础第3版PDF.zip'
	#zipApart = MIMEApplication(open(zipFile, 'rb').read())
	#zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)
	###

	try:
		smtpObj = smtplib.SMTP() 
		smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
		smtpObj.login(mail_user,mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		smtpObj.quit()
		print ("邮件发送成功")
	except smtplib.SMTPException as err:
		print (err)		
			
imgs=requests.get(imgsurl)
imgssoup=BeautifulSoup(imgs.content,'html.parser')
#查找imgs类型的a
imgurls=imgssoup.findAll('a',{"class":"imgs"})

conurl=''
for imgurl in imgurls:
	if imgurl.img['src'].find(datemd)>0:
		conurl='http://'+imgsurl.split('/')[2]+imgurl['href']
		subject=datemd2+imgurl.parent.div.h5.a.text
		break
if conurl=='':
	print("今日无图")
	pass
else:
	con=requests.get(conurl)
	consoup=BeautifulSoup(con.content,'html.parser')
	atturl=consoup.find('a',{"href":"###"}).img['src']
	auther=consoup.find('div',{"class":"article_con"}).contents[4].text
	attcon=consoup.find('div',{"class":"article_con"}).contents[0].text+"\n      "+auther
	#print(atturl)	
	mail2qq(atturl,attcon)
	print(pushmywchat("每日一图",datemd2+"邮件发送成功，请注意查收"))
