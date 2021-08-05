import sys
print(sys.path)
from rainbow_sdk.rainbow_client import RainbowClient
def get_config(config_key):
    init_param = {
        "connectStr":"api.rainbow.oa.com:8080",
        "tokenConfig":{
            "app_id":"00a872c3-ea3f-46c5-a0eb-a818760beb9b",
            "user_id":"",
            "secret_key":""
        },
    }
    rc = RainbowClient(init_param)
    res = rc.get_configs(group="mikit.set_mr",key=config_key,env_name="test")
    return res

def main():
    res=get_config()
    print(res)
    print('\n')
    print(type(res))

if __name__=='__main__':
    main()

