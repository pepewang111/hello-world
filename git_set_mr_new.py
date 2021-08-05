import argparse
import json
import yaml
import itertools
import git_helper

main_parser = argparse.ArgumentParser()
main_parser.add_argument('__trigger_params')

project_reviewer_config_file = 'project_reviewer_config.yaml'
with open(project_reviewer_config_file, 'r') as f:
    project_reviewers = yaml.safe_load(f)

def get_mr_info(project_id, mr_id):
    mr_info = git_helper.get_mr_info(project_id, mr_id)
    if mr_info is None:
        return None
    return mr_info

def set_mr_reviewers(project_id, mr_id, author_id):
    if project_id in project_reviewers:
        r = project_reviewers[project_id]
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
        return True
    else:
        print('unknown project_id just skip, project_id=%s' % project_id)
        return False

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
        mr_id = attributes['id']
        author_id = attributes['author_id']
        action = attributes['action']

        if action == 'open':
            if set_mr_reviewers(project_id, mr_id, author_id):
                print('set reviewers success')
                print('merge request: %s' % attributes['url'])
            else:
                print('set reviewers failure')
                print('merge request: %s' % attributes['url'])
        else:
            print('unregistered action, action=%s' % action)
if __name__ == '__main__':
    main()
