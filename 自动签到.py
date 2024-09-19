import random
import time

import requests
import json


def class_(cookies,id):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsIjoiMTI0ODE5NDc3NzEwNzcyODEyOCIsInMiOjE3MjY2MzMyMTIsImMiOiIyMzM4MzEyMCIsInUiOiIwIiwiZCI6IjAiLCJpIjoiNjEyMDUyODAiLCJwIjoiMiIsInIiOlsiMTA1Il0sImlhdCI6MTcyNjYzMzM2NCwiZXhwIjoxNzI2NjMzMzk0fQ.RK-C8puaf-zhc27IGJaCcHe-NWehVxCH6FfFoqRZvvU",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.yuketang.cn",
        "priority": "u=1, i",
        "referer": "https://www.yuketang.cn/lesson/fullscreen/v3/1248194777107728128?source=5",
        "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "xtbz": "ykt"
    }

    url = "https://www.yuketang.cn/api/v3/lesson/checkin"
    data = {
        "source": 5,
        "lessonId": id
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    print(response.text)
    print(response)

import requests




def check_class(cookies,headers):
    try:
        url = "https://www.yuketang.cn/api/v3/classroom/on-lesson-upcoming-exam"
        time.sleep(2)
        response = requests.get(url, headers=headers, cookies=cookies).json()
        classid = response["data"]["onLessonClassrooms"][0]["lessonId"]
        return classid
    except:
        print('没有课')
        time.sleep(1)
        check_class(cookies, headers)


headers = {
    "authority": "www.yuketang.cn",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsIjoiMTI0ODIwMTI4MDc2MTk1NjA5NiIsInMiOjE3MjY2MzM5ODcsImMiOiIyMzM4MzEyMCIsInUiOiIwIiwiZCI6IjAiLCJpIjoiNjA1ODUyNzUiLCJwIjoiMiIsInIiOlsiMTA1Il0sImlhdCI6MTcyNjYzNDAyNiwiZXhwIjoxNzI2NjM0MDU2fQ.IaWVL7BH0YbuTpd00WRAHVoWsb3K7xD-m4AyrJt5T3c",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.yuketang.cn",
    "referer": "https://www.yuketang.cn/lesson/fullscreen/v3/1248201280761956096?source=5",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Chromium\";v=\"112\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 QuarkPC/1.7.5.114",
    "xtbz": "ykt"
}


cookies_yh = {
    "django_language": "zh-cn",
    "JG_fcdf8e635093adde6bef42651_PV": "1726633236439|1726633237026",
    "login_type": "WX",
    "csrftoken": "kswk46iBQ2enm5CaL2IB9sPVssix7u60",
    "sessionid": "iu4moac2oy65alsea1pz03rjn56luweu",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%221920368f80b1090-02ad55e52bc15a2-26001051-3686400-1920368f80c1443%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMDM2OGY4MGIxMDkwLTAyYWQ1NWU1MmJjMTVhMi0yNjAwMTA1MS0zNjg2NDAwLTE5MjAzNjhmODBjMTQ0MyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221920368f80b1090-02ad55e52bc15a2-26001051-3686400-1920368f80c1443%22%7D",
    "sajssdk_2015_cross_new_user": "1"
}

cookies = {
    "JG_fcdf8e635093adde6bef42651_PV": "1726633463204|1726633463204",
    "login_type": "WX",
    "csrftoken": "slJflk8HKOjvkuUNZwpPSirnSf1N98zA",
    "sessionid": "ucn3t21xf0bxapb9w0cvedscm94veta6",
    "django_language": "zh-cn"
}
cookies_gj = {
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%221920354b1c413dd-0d1cdda7ed755c-4c657b58-3686400-1920354b1c51813%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyMDM1NGIxYzQxM2RkLTBkMWNkZGE3ZWQ3NTVjLTRjNjU3YjU4LTM2ODY0MDAtMTkyMDM1NGIxYzUxODEzIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221920354b1c413dd-0d1cdda7ed755c-4c657b58-3686400-1920354b1c51813%22%7D",
    "django_language": "zh-cn",
    "JG_fcdf8e635093adde6bef42651_PV": "1726742845772|1726742846802",
    "login_type": "WX",
    "csrftoken": "J33O2EVeqO6wf4tSGSEl5QrgdjAqAfOE",
    "sessionid": "sqd9lv8jrhfg5xfc4fluwumik7gagyw6"
}
import random
cookies_list = [cookies_yh, cookies_gj,cookies]
id = check_class(random.choice(cookies_list), headers)
for i in cookies_list:
    class_(i, id)

