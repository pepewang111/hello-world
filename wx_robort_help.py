import requests

import json


test_webhook_url ='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=9d96319e-7498-4a5b-b006-1a327aca9aa8'
test_webhook_url2 ='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=84429088-ce12-4f7e-ac67-410b73862c0b'
_headers = {
        "Content-Type": "application/json",
    }
    
def robort_post_info(info,visible_to_user,mentioned_list):
    
    data={'chatid':'wrkSFfCgAAhAMYaRRAMT3UdSHHLNnI4w','visible_to_user':visible_to_user,'msgtype':'text','text':{"content":info,'mentioned_list':mentioned_list}}
    
    r = requests.post(test_webhook_url,headers=_headers,json=data)
    if r.status_code !=200:
        print('faile')   
    else:
        print('success')
        
def robort_post_mr_info(info,visible_to_user,mentioned_list):
    data={'chatid':'wrkSFfCgAAhAMYaRRAMT3UdSHHLNnI4w','visible_to_user':visible_to_user,'msgtype':'text','text':{"content":info,'mentioned_list':mentioned_list}}
    
    r = requests.post(test_webhook_url,headers=_headers,json=data)
    if r.status_code !=200:
        print('faile')
    else:
        print('success')

def get_department_list():
    headers = {
        "Content-Type": "application/json",
    }
    _token = random.choice(_tokens)
    url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=0da7ae69220bcb8fb8d629dd0b54f4cf7fa97d49'
    data = requests.get(url).json()
    
    print(data)
def main(): 

    get_department_list()
if __name__ == '__main__':
    main()
