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
print(project_reviewers)
