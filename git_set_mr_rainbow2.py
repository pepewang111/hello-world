import argparse
import json
import yaml
import itertools
import git_helper
import get_rainbow_mikit_config
from ruamel.yaml import YAML

main_parser = argparse.ArgumentParser()
main_parser.add_argument('__trigger_params')

project_reviewer_config_file = get_rainbow_mikit_config.get_config('mikit_config2')
project_reviewers = project_reviewer_config_file
print(project_reviewers)
filename = 'get_mr_config.yaml'
with open(filename, 'w') as file_obj:
    file_obj.write(project_reviewers['mikit_config2'])
with open('get_mr_config.yaml',encoding='utf-8') as ff:
    data = yaml.safe_load(ff)
project_reviewers = data

#res = get_rainbow_mikit_config.get_config()
#project_reviewers = yaml.safe_load(res)
#print(project_reviewers)

def get_mr_info(project_id, mr_id):
    mr_info = git_helper.get_mr_info(project_id, mr_id)
    if mr_info is None:
        return None
    return mr_info

def set_mr_reviewers_url(project_url, project_id, mr_id, author_id, target_branch):
    project_url_self = project_url[18:]
    if project_url_self not in project_reviewers:
        print('unknown project_url just skip, project_url=%s' % project_url)
        r = project_reviewers['common']
    if project_url_self in project_reviewers:
        r = project_reviewers[project_url_self]
        
        if target_branch in r:

            r = r[target_branch]
        else:
            r= project_reviewers['common']
        # 过滤创建人

    real_reviewers = [it for it in r['reviewer_ids'] if it != author_id]
    real_necessary_reviewers = [it for it in r['necessary_reviewer_ids'] if it != author_id]
    id_pairs = list(itertools.zip_longest(real_reviewers, real_necessary_reviewers))
    # 设置评审人和必要评审人
    # 接口只支持每次邀请一个评审人和一个必要评审人
    for pair in id_pairs:
        data = {}
        if pair[0] is not None:
            data['reviewer_id'] = pair[0]
        if pair[1] is not None:
            data['necessary_reviewer_id'] = pair[1]
        if not git_helper.set_mr_reviewers(project_id, mr_id, data):
            return False

    print('set mr reviewers=%s, necessary_reviewer=%s' % (str(real_reviewers), str(real_necessary_reviewers)))

def main():
    args = main_parser.parse_args()
    if args.__trigger_params:
        trigger_params = json.loads(args.__trigger_params)
        trigger_header = trigger_params['headers']
        if trigger_header['X-EVENT'] != 'Merge Request Hook':
            print('not merge request, just skip: X-EVENT=%s' % trigger_header['X-EVENT'])
            return

        body = trigger_params['body']
        attributes = body['object_attributes']
        project_id = attributes['target_project_id']
        project_source = attributes['source']
        project_url = project_source['web_url']
        mr_id = attributes['id']
        target_branch = attributes['target_branch']
        author_id = attributes['author_id']
        action = attributes['action']
        
        if action == 'open':
            if set_mr_reviewers_url(project_url, project_id, mr_id, author_id, target_branch):
                print('set reviewers success')
                print('merge request: %s' % attributes['url'])
            else:
                print('set reviewers failure')
                print('merge request: %s' % attributes['url'])
        else:
            print('unregistered action, action=%s' % action)
if __name__ == '__main__':
    main()

