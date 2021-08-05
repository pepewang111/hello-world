#coding=utf-8
import argparse
import json
import re
import random
import git_helper
import requests

main_parser = argparse.ArgumentParser()
main_parser.add_argument('_add_project_id', required=False, type=int)
main_parser.add_argument('_add_git_url', required=False, help='git_repo')
main_parser.add_argument('_add_reviewer_id', required=False, type=int,help='reviewer_id')
main_parser.add_argument('_add_reviewer_name', required=False, help='reviewer_name')
main_parser.add_argument('_add_reviewer_id_in_project', required=False, type=int,help='project_id')
main_parser.add_argument('_add_necessary_reviewer_id', required=False, type=int,help='necessary_reviewer_id')
main_parser.add_argument('_add_necessary_reviewer_name', required=False, help='necessary_reviewer_name')
main_parser.add_argument('_add_necessary_reviewer_id_in_project', required=False, type=int,help='necessary_project_id')

main_parser.add_argument('_modify_project_id', required=False, type=int)


