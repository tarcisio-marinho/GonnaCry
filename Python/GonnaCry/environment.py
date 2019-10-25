import os
import pwd

def get_desktop_path():
    caminho = os.path.join(os.path.expanduser('~'), '/Desktop/')
    caminho2 = os.path.join(os.path.expanduser('~'), '/Área\\ de\\ Trabalho/')
    if(os.path.isdir(caminho)):
        path = caminho
    elif(os.path.isdir(caminho2)):
        path = caminho2
    else:
        path = os.path.expanduser('~') + '/Desktop/'
    
    return path


def get_username():
    return pwd.getpwuid(os.getuid())[0]


def get_unique_machine_id():
    with open("/etc/machine-id") as f :
        id = f.read()
        if('\n' in id):
            id = id.replace('\n', '')
    
    return id


def get_home_path():
    return os.path.expanduser('~')
