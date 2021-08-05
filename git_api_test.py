#!/usr/bin/python3
#coding=utf-8
import argparse
import json
import yaml
import itertools
import git_helper

main_parser = argparse.ArgumentParser()
main_parser.add_argument('_action' , help = 'action you want to do(get_group_list ) ' )
main_parser.add_argument('_group_id' , help = 'group id in git')

def get_group_list(group_id):
    group_info = git_helper.get_group(group_id)
    if group_info is None:
        # print('no projects, just skip')
        return False
    return group_info

def main():
    args = main_parser.parse_args()
    print('start here \n')
    if args._action == 'get_group_list' :
        group_info = get_group_list(args._group_id)
        if group_info is None:
            print('get group list failure')
        else:
            print('get group list success')
            
            print(group_info)
            

    else:
        print('unregistered action, action=%s' % args._action)
    print('\ndown!')

if __name__ == '__main__':
    main()

