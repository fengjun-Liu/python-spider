import requests

url = "https://sc.ftqq.com/SCU88589T51d420a21b4ff294fe0ac4673bf201235e65c03803268.send?text=测试postman推送消息&desp=从postman发消息到server酱，微信接受"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
