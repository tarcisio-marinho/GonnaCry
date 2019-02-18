#!/usr/bin/env python



import argparse


parser = argparse.ArgumentParser(description='Build GonnaCry.', add_help=True)
parser.add_argument('-i', '--ip', type=str, required=True, metavar='[FILE]',
    help='Ip address of the server. GonnaCry will try to connect to')
parser.add_argument('-p', '--port', type=str, required=False, metavar='[FILE]',
    help='Port of the server.')
    
args = parser.parse_args()









