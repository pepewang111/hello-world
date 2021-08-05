from rainbow_sdk.rainbow_client import RainbowClient
print('start here')
init_param = {
    "connectStr":"api.rainbow.oa.com:8080",
    "tokenConfig":{
        "app_id":"a0f6a65b-86e2-4432-b117-fcb557a5ac4a",
        "user_id":"",
        "secret_key":""

        # 没启用配置拉取签名时，user_id、secret_key 传空字符即可
    },
}
rc = RainbowClient(init_param)
print(rc)

res = rc.get_configs(group="DEV.SZ",key="test_config")
print(res)
