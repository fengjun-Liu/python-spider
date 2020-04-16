import requests

def pushmywchat(text,desp):
	dd={'text':text,"desp":desp}
	url = "https://sc.ftqq.com/SCU88589T51d420a21b4ff294fe0ac4673bf201235e65c03803268.send"

	payload = {}
	headers= {}
	try:
		response = requests.request("GET", url, params=dd, headers=headers, data = payload)
		response.raise_for_status()
		response.encoding='utf-8'
		return(response.text)
	except:
		return "产生异常"
	
print(pushmywchat("123","456"))
