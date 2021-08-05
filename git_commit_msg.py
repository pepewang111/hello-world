#coding=utf-8
import argparse
import json
import yaml
import itertools
import git_helper

main_parser = argparse.ArgumentParser()
main_parser.add_argument('__trigger_params')

    

def main():
    args = main_parser.parse_args()
    if args.__trigger_params:
        trigger_params = json.loads(args.__trigger_params)

        trigger_header = trigger_params['headers']
        # X-EVENT 值说明，可以参考：https://git.woa.com/help/menu/manual/webhooks.html
        if trigger_header['X-EVENT'] != 'Push Hook':
            print('not Review Hook, just skip: X-EVENT=%s' % trigger_header['X-EVENT'])
            return
        #webhook报文解析获取指定参数
        body = trigger_params['body']

        commit_info = body['commits']
        commit_id = commit_info[0]['id']
        commit_msg = commit_info[0]['message']
        project_id = body['project_id']
        print(commit_msg)

        

if __name__ == '__main__':
    main()
