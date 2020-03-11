import requests
import json
import datetime
import random
import string
import time

referrer = input("id account cua bạn: ")
#referrer = "87222f08-869c-4277-8831-cdee903acfce"
timesToLoop = 99999999
retryTimes = 5
sleeptime = 20

def genString(stringLength):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


url = 'https://api.cloudflareclient.com/v0a848/reg'


def run():
    install_id = genString(11)
    body = {"key": "{}=".format(genString(42)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
            "type": "Android",
            "locale": "zh-CN"}

    bodyString = json.dumps(body)

    headers = {'Content-Type': 'application/json; charset=UTF-8',
               'Host': 'api.cloudflareclient.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.12.1'
               }

    r = requests.post(url, data=bodyString, headers=headers)
    return r


for i in range(timesToLoop):
    result = run()
    if result.status_code == 200:
        print(i + 1, "Done: + 1 GB,   wait for 20 seconds :)")
        time.sleep(sleeptime)
    else:
        print(i + 1, "Error")
        for r in range(retryTimes):
            retry = run()
            if retry.status_code == 200:
                print(i + 1, "Retry #" + str(r + 1), ", Done: + 1 GB,   wait for 20 seconds :)")
                time.sleep(timesleep)
                break
            else:
                print(i + 1, "Retry #" + str(r + 1), "Error")
                if r == retryTimes - 1:
                    exit()
