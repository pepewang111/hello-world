#coding=utf-8
import argparse
import json
import yaml
import itertools
import git_helper

main_parser = argparse.ArgumentParser()
main_parser.add_argument('_invite_reviewer',type=int,help='(ac)Invites a user to review the specified merge request\n  1.do it',required=False,default=0)
main_parser.add_argument('_dismissals_reviewer',type=int,help='Removes a specified reviewer from the specified merge request\n  1.do it',required=False,default=0)
main_parser.add_argument('_cancel_reviewer',type=int,help='Removes a reviewer for a specified merge request from the project\n  1.do it',required=False,default=0)
main_parser.add_argument('_query_review_id',type=int,help='Queries the project for a specified merge request review information\n  1.do it',required=False,default=0)
main_parser.add_argument('_query_review_iid',type=int,help='Queries the project for a specified merge request review information\n  1.do it',required=False,default=0)
main_parser.add_argument('_comment_review',type=int,help='The reviewer comments on a specific consolidated request within the project\n  1.do it',required=False,default=0)
main_parser.add_argument('_reopen_review',type=int,help='Resets the review status of a specified merge request in the project. The merge request must be in the reject or feedback modification state\n  1.do it',required=False,default=0)
main_parser.add_argument('_query_mr',type=int,help='Query the Dashboard dimension MR(merge_request)\n  1.do it',required=False,default=0)
main_parser.add_argument('_query_viewed_files',type=int,help='Queries the list of files that are confirmed to have been read in the code review\n  1.do it',required=False,default=0)

main_parser.add_argument('_invite_reviewer_id',help='Project ID or project full path project_full_path',required=False)
main_parser.add_argument('_invite_reviewer_merge_request_id',help='Id of the merge request',required=False,type=int)
main_parser.add_argument('_invite_reviewer_reviewer_id',help='Id of reviewer',required=False,type=int)
main_parser.add_argument('_invite_reviewer_necessary_reviewer_id',help='Id of necessary reviewer',required=False,type=int)








