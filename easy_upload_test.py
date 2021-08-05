#coding=utf-8

import argparse
import yaml

main_parser = argparse.ArgumentParser()
main_parser.add_argument('--name',default='Great')

def main():
    args = main_parser.parse_args()
    name = args.name
    print('Hello {}'.format(name))

if __name__=='__main__':
    main()

