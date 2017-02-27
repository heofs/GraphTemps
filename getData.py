#! /usr/bin/env python3

def get_data():
    with open('log.txt', 'r') as f:
        lines = f.readlines()
        print(lines)
get_data()
