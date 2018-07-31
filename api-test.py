#!/bin/python

import pycurl
from StringIO import StringIO
import json
import os
import requests
import sys
IP=sys.argv[1]

URL_CHECK="http://"+IP+"/studentapi"
URL_LIST="http://"+IP+"/studentapi/student/list"
URL_POST="http://"+IP+"/studentapi/student"

### Check the API is responding or not
r = requests.get(URL_CHECK)
if r.status_code == 200:
    print 'URL CHECK - SUCCESS'
else:
    print 'URL CHECK - FAILURE'
    os.system('exit 1')


### Check the LIST of Students with API
buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, URL_LIST)
c.setopt(c.WRITEFUNCTION, buffer.write)
c.perform()
c.close()

body = buffer.getvalue()
data = json.loads(body)
httpstat=str(data['httpStatus'])
STAT=int(httpstat[:1])

if STAT == 2:
    print 'STUDENT APP LIST CHECK - SUCCESS'
else:
    print 'STUDENT APP LIST CHECK - FAILURE'
    os.system('exit 1')


### INSERT DATA to Student app from API
headers = {
    'Content-Type': 'application/json',
}

data = '{"studentName": "Meghan Mahadev","studentAddr": "Hyderabad","studentAge": "2","studentQulaification": "Nursary","studentPercent": "99%","studentYearPassword": "2017"}'

response = requests.post(URL_POST, headers=headers, data=data)
resp_string=str(response.status_code)
output=response.text
data = json.loads(output)
STUDENT_ID=data['data']['object']['student_id']
response=int(resp_string[:1])

if response == 2:
    print 'STUDENT APP INSERT DATA - SUCCESS'
else:
    print 'STUDENT APP INSERT DATA - FAILURE'
    os.system('exit 1')


URL_DELETE="http://"+IP+"/studentapi/student/"+str(STUDENT_ID)
response = requests.delete(URL_DELETE, headers=headers)
resp_string =str(response.status_code)
response=int(resp_string[:1])
if response == 2:
    print 'STUDENT APP DELETE DATA - SUCCESS'
else:
    print 'STUDENT APP DELETE DATA - FAILURE'
    os.system('exit 1')


