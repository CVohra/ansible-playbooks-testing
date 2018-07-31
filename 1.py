import urllib
import urllib2
import requests

url = "http://35.185.69.21/studentapi/student"
data = '{"studentName": "Meghan Mahadev","studentAddr": "Hyderabad","studentAge": "2","studentQulaification": "Nursary","studentPercent": "99%","studentYearPassword": "2017"}'

headers = {
    'Content-Type': 'application/json',
}

data = '{"studentName": "Meghan Mahadev","studentAddr": "Hyderabad","studentAge": "2","studentQulaification": "Nursary","studentPercent": "99%","studentYearPassword": "2017"}'

response = requests.post(url, headers=headers, data=data)
print response.text



