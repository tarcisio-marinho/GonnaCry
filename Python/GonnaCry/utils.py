import string
import random
import os

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
