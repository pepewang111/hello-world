#-*- coding:utf-8 -*-
# sample/filerewrite.py

import argparse
import os

main_parser = argparse.ArgumentParser()
main_parser.add_argument('-f', dest='file',metavar='文件',type=file,required=True)

def main():
    args = main_parser.parse_args()
    print("filename: ", args.file.name)
    with open('helloworld','wb') as fp:
        fp.write(args.file.read())
    info = os.stat('helloworld')
    print('file size: ', info.st_size)
    print('file create time', info.st_ctime)

if __name__=="__main__":
    main()

