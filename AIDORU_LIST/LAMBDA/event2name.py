#!/usr/bin/env python3
#coding: utf-8
# lambdaのeventに入ってくるjsonをユニケージ用（name形式）にパース

import sys
import json

def main():
    line = sys.argv
    file = open(line[1])
    event = json.loads(' '.join(file.readlines()))

    for k, v in event['body'].items():
        print(k, end=" ")
        print(v)

if __name__ == '__main__':
    main()
