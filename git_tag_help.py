#coding=utf-8
import argparse
import json
import yaml
import itertools
import git_helper
import wx_robort_help

main_parser = argparse.ArgumentParser()
main_parser.add_argument('__trigger_params')

def main():
    args = main_parser.parse_args()
    if args.__trigger_params:
        trigger_params = json.loads(args.__trigger_params)
        trigger_header = trigger_params['headers']
        if trigger_header['X-EVENT'] != 'Tag Push Hook':
            print('not Tag Push , just skip: X-EVENT=%s' % trigger_header['X-EVENT'])
            return
                
        body = trigger_params['body']
        ref = body['ref'] 
        tag_info = ref[10:]
        info = 'tag=' + tag_info
        info+= '\n'
        repository = body['repository']
        homepage = repository['homepage']
        info = info + 'homepage=' + homepage
        info+= '\n'
        
        commits = body['commits']
        author = commits[0]['author']
        author_name = author['name']
        info = info + 'author_name=' + author_name
        info+= '\n'
        create_from = body['create_from']
        info = info + 'create_from=' + create_from
        info+= '\n'
        
        print('tag=',tag_info)
        tag_info = str(tag_info)
        print(tag_info)        
        erorr_char = 0
        number = 0
        for _char in tag_info:
            if ord(_char)>=48 and ord(_char)<=57:
                continue
            if _char == '.':
                number+=1
                if(number==3):
                    print('.数量过多,tag格式应为a(int).b(int).c(int)')
                    info+='.数量过多,tag格式应为a(int).b(int).c(int)'
                    mentioned_list = [author_name]
                    print(author_name)
                    print(mentioned_list)
                    wx_robort_help.robort_post_info(info,author_name,mentioned_list)
                    break
            else:
                erorr_char = 1
                print('不允许的字符,tag格式应为a(int).b(int).c(int)') 
                info+= '不允许的字符,tag格式应为a(int).b(int).c(int)'
                mentioned_list = [author_name]
                print(author_name)
                print(mentioned_list)
                wx_robort_help.robort_post_info(info,author_name,mentioned_list)
                break
        if number == 2 and erorr_char == 0:
            print('tag格式正确')
            info+= 'tag格式正确'  

if __name__ == '__main__':
    main()

