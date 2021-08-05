#coding=utf-8
import requests
import json
# API接口文档：https://git.woa.com/help/menu/api/
_headers = {
    "PRIVATE-TOKEN": "6-8l7GcRuvnz7xVLxiKv"
}

base_url = 'https://git.woa.com'
get_mr_info_url = base_url + '/api/v3/projects/%s/merge_request/%s'
get_group_url = base_url + '/api/v3/groups/{group_id}'
get_project_branch_url = base_url + '/api/v3/projects/{project_id}/repository/branches/{branch_name}'
get_branch_tags_url = base_url + '/api/v3/projects/{project_id}/repository/{branch_name}/tags'
get_all_project_info_url = base_url + '/api/v3/projects'
get_commit_info_url = base_url + '/api/v3/projects/{project_id}/repository/commits/{sha}'
get_tag_list_url = base_url + '/api/v3/projects/{project_id}/repository/tags'
get_tag_branch_list_url = base_url + '/api/v3/projects/{project_id}/repository/{branch_name}/tags'

set_mr_info_url = base_url + '/api/v3/projects/%s/merge_request/%s'
set_mr_reviewers_url = base_url + '/api/v3/projects/{project_id}/merge_request/{mr_id}/review/invite'
set_mr_reviewers_url_path  = base_url + '/api/v3/projects/{project_url}/merge_request/{mr_id}/review/invite'

def get_commit_info_url(project_id, sha):
    r = requests.get(get_commit_info_url.format(project_id=project_id, sha=sha),headers=_headers)
    if r.status_code !=200:
        print('get commit message information error, status_code=%s, project_id=%s, review_iid=%s' % (r.status_code,project_id,review_iid))
        return None
    else:
        print('r.status=',r.status_code)
        return r.json()

def get_mr_info(project_id, mr_id):
    r = requests.get(get_mr_info_url.format(project_id=project_id, mr_id=mr_id), headers=_headers)
    if r.status_code != 200:
        print('get merge request information error, status_code=%s, project_id=%s, mr_id=%s'
 % (r.status_code,project_id,mr_id))
        return None
    else :
        print('...success... r.status_code=%s ' % r.status_code )
    return r.json()

def set_mr_reviewers(project_id, mr_id, reviewers):
    r = requests.post(set_mr_reviewers_url.format(project_id=project_id, mr_id=mr_id), 
                        headers=_headers, data=reviewers)
    if r.status_code != 200:
        print('set mr reviewers error, status_code=%s, project_id=%s, mr_id=%s, request=%s' % 
            (r.status_code, project_id, mr_id, json.dumps(reviewers)))
        return False
    return True

def set_mr_reviewers_byurl(project_url, mr_id, reviewers): 
    r = requests.post(set_mr_reviewers_url_path.format(project_url=project_url, mr_id=mr_id),
                        headers=_headers, data=reviewers)
    if r.status_code != 200:
        print('set mr reviewers error, status_code=%s, project_url=%s, mr_id=%s, request=%s' %
            (r.status_code, project_url, mr_id, json.dumps(reviewers)))
        return False
    return True

def get_group(group_id):
    r = requests.get(get_group_url.format(group_id=group_id), headers=_headers)
    if r.status_code != 200:
        print('get group error, status_code=%s, group_id=%s' % (r.status_code, group_id))
        return None
    else :
        print('...success... r.status_code=%s ' % r.status_code )
    return r.json()

def get_project_branch(project_id, branch):
    r = requests.get(get_project_branch_url.format(project_id=project_id, branch_name=branch), 
                    headers=_headers)
    if r.status_code != 200:
        print('get branch error, status_code=%s, project_id=%s, branch=%s' % 
                (r.status_code, project_id, branch))
        return None
    return r.json()


def get_branch_tags(project_id, branch):
    url = get_branch_tags_url.format(project_id=project_id, branch_name=branch)
    payload = {
        'per_page': 100
    }
    r = requests.get(url, headers=_headers, params=payload)
    if r.status_code != 200:
        print('get branch tags error, status_code=%s, project_id=%s, branch=%s' % 
            (r.status_code, project_id, branch))
        return None
    return r.json()

